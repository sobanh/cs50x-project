from datetime import datetime
from cs50 import SQL
from flask import redirect, render_template, request, session
from functools import wraps
from amadeus import Client, ResponseError
import ssl
from urllib.request import urlopen
import requests

db = SQL("sqlite:///airlines.db")


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def ssl_disabled_urlopen(endpoint):
    context = ssl._create_unverified_context()
    return urlopen(endpoint, context=context)


def lookup(source, destination, date, passengers, travelClass, currency):

    # Query Amadeus API for flight tickets
    amadeus = Client(
        client_id='AMADEUS_API_KEY',
        client_secret='AMADEUS_API_SECRET',
        http=ssl_disabled_urlopen
    )

    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=source,
            destinationLocationCode=destination,
            departureDate=date,
            adults=passengers,
            travelClass=travelClass, 
            max=10,
            nonStop='true',
            currencyCode=currency) 
        return response.data
    except ResponseError:
        return None


def extract_data(dataset):

    # Extracting data from the Amadeus API response
    info = list()
    for data in dataset:    

        # Departure date and time
        text = data['itineraries'][0]['segments'][0]['departure']['at']
        x = text.split("T")

        dateobj = datetime.strptime(x[0], '%Y-%m-%d').date()
        timeobj = datetime.strptime(x[1], '%H:%M:%S').time()
    
        departureDate = dateobj.strftime('%B %d')
        departureTime = timeobj.strftime('%I:%M %p')

        # Arrival date and time
        text = data['itineraries'][0]['segments'][0]['arrival']['at']
        x = text.split("T")

        dateobj = datetime.strptime(x[0], '%Y-%m-%d').date()
        timeobj = datetime.strptime(x[1], '%H:%M:%S').time()
    
        arrivalDate = dateobj.strftime('%B %d')
        arrivalTime = timeobj.strftime('%I:%M %p')
    
        # Airline's name
        code = data['itineraries'][0]['segments'][0]['carrierCode']
        name = db.execute("SELECT name FROM airlines WHERE code = ?", code)

        price = float(data['price']['grandTotal'])

        extract = {
            'source': data['itineraries'][0]['segments'][0]['departure']['iataCode'],
            'destination': data['itineraries'][0]['segments'][0]['arrival']['iataCode'],
            'price': data['price']['currency'] + ' ' + f"{price:,.2f}",
            'departureDate': departureDate,
            'departureTime': departureTime,
            'arrivalTime': arrivalTime,
            'arrivalDate': arrivalDate,
            'name': name[0]['name']
        }
        info.append(extract)
    return info


def trackFlight(flightCode):

    # Query AirLabs API for the live status of a flight
    params = {
        'api_key': 'AIRLABS_API_KEY',
        'flight_iata': flightCode
    }
    method = 'flights'
    api_base = 'https://airlabs.co/api/v9/'
    api_result = requests.get(api_base+method, params)
    api_response = api_result.json()

    try:
        response = api_response['response'][0]
    except (TypeError, ValueError, IndexError):
        return None
    
    # Airline's Name
    airline_iata = response['airline_iata']
    airlines = db.execute("SELECT name from airlines WHERE code = ?", airline_iata)

    # Departure IATA, City and Airport
    dep_iata = response['dep_iata']
    depCity = db.execute("SELECT city FROM airports WHERE iata = ?", dep_iata)
    depAirport = db.execute("SELECT name FROM airports WHERE iata = ?", dep_iata)

    # Arrival IATA, City and Airport
    arr_iata = response['arr_iata']
    arrCity = db.execute("SELECT city FROM airports WHERE iata = ?", arr_iata)
    arrAirport = db.execute("SELECT name FROM airports WHERE iata = ?", arr_iata)

    # Latitude and Longitude
    lat = response['lat']
    lng = response['lng']

    # Altitude, Groundspeed and Heading
    altitude = response['alt']
    speed = response['speed']
    heading = response['dir']

    try: 
        dataset = {
            'flight_iata': flightCode,
            'airlines': airlines[0]['name'],
            'dep_iata': dep_iata,
            'depCity': depCity[0]['city'],
            'depAirport': depAirport[0]['name'], 
            'arr_iata': arr_iata,
            'arrCity': arrCity[0]['city'],
            'arrAirport': arrAirport[0]['name'], 
            'lat': lat,
            'lng': lng, 
            'altitude': f"{altitude:,}", 
            'speed': speed,
            'heading': heading
        }
        return dataset
    except IndexError:
        return None




        