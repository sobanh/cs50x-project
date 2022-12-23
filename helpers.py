from datetime import datetime
from cs50 import SQL

db = SQL("sqlite:///airlines.db")

dataset= [
    
{'type': 'flight-offer', 'id': '1', 'source': 'GDS', 'instantTicketingRequired': False, 'nonHomogeneous': False, 'oneWay': False, 'lastTicketingDate': '2022-12-23', 'numberOfBookableSeats': 9, 'itineraries': [{'duration': 'PT3H20M', 'segments': [{'departure': {'iataCode': 'BOM', 'terminal': '2', 'at': '2022-12-23T23:05:00'}, 'arrival': {'iataCode': 'DXB', 'terminal': '1', 'at': '2022-12-24T00:55:00'}, 'carrierCode': 'SG', 'number': '13', 'aircraft': {'code': '7M8'}, 
                                         'operating': {'carrierCode': 'SG'}, 
                                         'duration': 'PT3H20M', 
                                         'id': '3', 
                                         'numberOfStops': 0, 
                                         'blacklistedInEU': False}]}], 
          'price': {'currency': 'EUR', 
                    'total': '170.43', 
                    'base': '125.00', 
                    'fees': [{'amount': '0.00', 'type': 'SUPPLIER'}, 
                             {'amount': '0.00', 'type': 'TICKETING'}], 
                    'grandTotal': '170.43'}, 
         'pricingOptions': {'fareType': ['PUBLISHED'], 'includedCheckedBagsOnly': True}, 
         'validatingAirlineCodes': ['GP'], 
         'travelerPricings': [{'travelerId': '1', 
                               'fareOption': 'STANDARD', 
                               'travelerType': 'ADULT', 
                               'price': {'currency': 'EUR', 'total': '170.43', 'base': '125.00'}, 
                               'fareDetailsBySegment': [{'segmentId': '3', 
                                                        'cabin': 'ECONOMY', 
                                                        'fareBasis': 'UOWSVRIN', 
                                                        'class': 'U', 
                                                        'includedCheckedBags': {'weight': 30, 'weightUnit': 'KG'}}]}]}, 

    {'type': 'flight-offer', 'id': '2', 'source': 'GDS', 
         'instantTicketingRequired': False, 
         'nonHomogeneous': False, 
         'oneWay': False, 
         'lastTicketingDate': '2022-12-22', 
         'numberOfBookableSeats': 9, 
         'itineraries': [{'duration': 'PT3H30M', 
                            'segments': [{'departure': {'iataCode': 'BOM', 'terminal': '2', 'at': '2022-12-23T05:15:00'}, 
                                            'arrival': {'iataCode': 'DXB', 'terminal': '2', 'at': '2022-12-23T07:15:00'}, 
                                            'carrierCode': 'FZ', 
                                            'number': '446', 
                                            'aircraft': {'code': '73H'}, 
                                            'operating': {'carrierCode': 'FZ'}, 
                                            'duration': 'PT3H30M', 
                                            'id': '4', 
                                            'numberOfStops': 0, 
                                            'blacklistedInEU': False}]}], 
         'price': {'currency': 'EUR', 
                    'total': '171.51', 
                    'base': '97.00', 
                    'fees': [{'amount': '0.00', 'type': 'SUPPLIER'}, 
                             {'amount': '0.00', 'type': 'TICKETING'}], 
                    'grandTotal': '171.51'}, 
         'pricingOptions': {'fareType': ['PUBLISHED'], 'includedCheckedBagsOnly': True}, 
         'validatingAirlineCodes': ['FZ'], 
         'travelerPricings': [{'travelerId': '1', 'fareOption': 'STANDARD', 'travelerType': 'ADULT', 'price': {'currency': 'EUR', 'total': '171.51', 'base': '97.00'}, 'fareDetailsBySegment': [{'segmentId': '4', 'cabin': 'ECONOMY', 'fareBasis': 'UOLP7IN1', 'class': 'U', 'includedCheckedBags': {'weight': 30, 'weightUnit': 'KG'}}]}]}, 
    
    {'type': 'flight-offer', 'id': '3', 'source': 'GDS', 'instantTicketingRequired': False, 'nonHomogeneous': False, 'oneWay': False, 'lastTicketingDate': '2022-12-23', 'numberOfBookableSeats': 1, 'itineraries': [{'duration': 'PT27H45M', 'segments': [{'departure': {'iataCode': 'BOM', 'terminal': '2', 'at': '2022-12-23T20:10:00'}, 'arrival': {'iataCode': 'HYD', 'at': '2022-12-23T21:40:00'}, 'carrierCode': 'AI', 'number': '619', 'aircraft': {'code': '319'}, 'operating': {'carrierCode': 'AI'}, 'duration': 'PT1H30M', 'id': '5', 'numberOfStops': 0, 'blacklistedInEU': False}, {'departure': {'iataCode': 'HYD', 'at': '2022-12-24T19:40:00'}, 'arrival': {'iataCode': 'DXB', 'terminal': '1', 'at': '2022-12-24T22:25:00'}, 'carrierCode': 'AI', 'number': '951', 'aircraft': {'code': '32N'}, 'operating': {'carrierCode': 'AI'}, 'duration': 'PT4H15M', 'id': '6', 'numberOfStops': 0, 'blacklistedInEU': False}]}], 'price': {'currency': 'EUR', 'total': '189.27', 'base': '159.00', 'fees': [{'amount': '0.00', 'type': 'SUPPLIER'}, {'amount': '0.00', 'type': 'TICKETING'}], 'grandTotal': '189.27'}, 'pricingOptions': {'fareType': ['PUBLISHED'], 'includedCheckedBagsOnly': True}, 'validatingAirlineCodes': ['AI'], 'travelerPricings': [{'travelerId': '1', 'fareOption': 'STANDARD', 'travelerType': 'ADULT', 'price': {'currency': 'EUR', 'total': '189.27', 'base': '159.00'}, 'fareDetailsBySegment': [{'segmentId': '5', 'cabin': 'ECONOMY', 'fareBasis': 'ULOWHYAE', 'class': 'Q', 'includedCheckedBags': {'weight': 30, 'weightUnit': 'KG'}}, {'segmentId': '6', 'cabin': 'ECONOMY', 'fareBasis': 'ULOWHYAE', 'class': 'U', 'includedCheckedBags': {'weight': 30, 'weightUnit': 'KG'}}]}]}, 
    
    {'type': 'flight-offer', 'id': '4', 'source': 'GDS', 'instantTicketingRequired': False, 'nonHomogeneous': False, 'oneWay': False, 'lastTicketingDate': '2022-12-23', 'numberOfBookableSeats': 1, 'itineraries': [{'duration': 'PT3H15M', 'segments': [{'departure': {'iataCode': 'BOM', 'terminal': '2', 'at': '2022-12-23T20:10:00'}, 'arrival': {'iataCode': 'DXB', 'terminal': '1', 'at': '2022-12-23T21:55:00'}, 'carrierCode': 'AI', 'number': '983', 'aircraft': {'code': '788'}, 'operating': {'carrierCode': 'AI'}, 'duration': 'PT3H15M', 'id': '1', 'numberOfStops': 0, 'blacklistedInEU': False}]}], 'price': {'currency': 'EUR', 'total': '195.27', 'base': '159.00', 'fees': [{'amount': '0.00', 'type': 'SUPPLIER'}, {'amount': '0.00', 'type': 'TICKETING'}], 'grandTotal': '195.27'}, 'pricingOptions': {'fareType': ['PUBLISHED'], 'includedCheckedBagsOnly': True}, 'validatingAirlineCodes': ['AI'], 'travelerPricings': [{'travelerId': '1', 'fareOption': 'STANDARD', 'travelerType': 'ADULT', 'price': {'currency': 'EUR', 'total': '195.27', 'base': '159.00'}, 'fareDetailsBySegment': [{'segmentId': '1', 'cabin': 'ECONOMY', 'fareBasis': 'ULOWBMAE', 'class': 'U', 'includedCheckedBags': {'weight': 30, 'weightUnit': 'KG'}}]}]}, 
    
    {'type': 'flight-offer', 'id': '5', 'source': 'GDS', 'instantTicketingRequired': False, 'nonHomogeneous': False, 'oneWay': False, 'lastTicketingDate': '2022-12-23', 'numberOfBookableSeats': 9, 'itineraries': [{'duration': 'PT3H20M', 'segments': [{'departure': {'iataCode': 'BOM', 'terminal': '2', 'at': '2022-12-23T16:25:00'}, 'arrival': {'iataCode': 'DXB', 'terminal': '1', 'at': '2022-12-23T18:15:00'}, 'carrierCode': 'UK', 'number': '201', 'aircraft': {'code': '321'}, 'operating': {'carrierCode': 'UK'}, 'duration': 'PT3H20M', 'id': '2', 'numberOfStops': 0, 'blacklistedInEU': False}]}], 'price': {'currency': 'EUR', 'total': '196.08', 'base': '160.00', 'fees': [{'amount': '0.00', 'type': 'SUPPLIER'}, {'amount': '0.00', 'type': 'TICKETING'}], 'grandTotal': '196.08'}, 'pricingOptions': {'fareType': ['PUBLISHED'], 'includedCheckedBagsOnly': True}, 'validatingAirlineCodes': ['UK'], 'travelerPricings': [{'travelerId': '1', 'fareOption': 'STANDARD', 'travelerType': 'ADULT', 'price': {'currency': 'EUR', 'total': '196.08', 'base': '160.00'}, 'fareDetailsBySegment': [{'segmentId': '2', 'cabin': 'ECONOMY', 'fareBasis': 'VOINYV', 'brandedFare': 'ECOYV', 'class': 'V', 'includedCheckedBags': {'weight': 30, 'weightUnit': 'KG'}}]}]}]


def lookup():
    info = list()

    for data in dataset:
        #source
        #destintaion
        #price
        
        #departure time
        text = data['itineraries'][0]['segments'][0]['departure']['at']
        x = text.split("T")

        dateobj = datetime.strptime(x[0], '%Y-%m-%d').date()
        timeobj = datetime.strptime(x[1], '%H:%M:%S').time()
    
        departureDate = dateobj.strftime('%B %d')
        departureTime = timeobj.strftime('%I:%M %p')

        #arrival time
        text2 = data['itineraries'][0]['segments'][0]['arrival']['at']
        x2 = text2.split("T")

        dateobj2 = datetime.strptime(x2[0], '%Y-%m-%d').date()
        timeobj2 = datetime.strptime(x2[1], '%H:%M:%S').time()
    
        arrivalDate = dateobj2.strftime('%B %d')
        arrivalTime = timeobj2.strftime('%I:%M %p')

        #duration
        durationformat = (data['itineraries'][0]['duration'][2:].lower())
        duration = str()
        for char in durationformat:
            if char == 'h': 
                duration += (char + ' ')
            else:
                duration += (char)
    
        #airline name
        code = data['itineraries'][0]['segments'][0]['carrierCode']
        name = db.execute("SELECT name FROM airlines WHERE code = ?", code)

        #logo
        logo = db.execute("SELECT logo FROM airlines WHERE code + ?", code)
        abcd = {
            'source' : data['itineraries'][0]['segments'][0]['departure']['iataCode'],
            'destination' : data['itineraries'][0]['segments'][0]['arrival']['iataCode'],
            'price' : data['price']['currency'] + ' ' + data['price']['grandTotal'],
            'departureDate' : departureDate,
            'departureTime': departureTime,
            'arrivalTime' : arrivalTime,
            'arrivalDate' : arrivalDate,
            'duration' : duration, 
            'name' : name[0]['name'],
            'logo' : logo[0]['logo']
        }
        info.append(abcd)
    return info