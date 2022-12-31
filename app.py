import os

from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
from helpers import apology, login_required, lookup, extract_data, trackFlight
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
import re

# Configure Application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///airlines.db")


# Registering a new user
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # If any field is left blank
        if not username:
            return apology("Please enter a valid username")
        elif not password or not confirmation:
            return apology("Please enter a password")

        # Validating Password
        lower = 0
        lowercase = re.compile("[a-z]")
        upper = 0
        uppercase = re.compile("[A-Z]")
        numbers = 0
        numberpattern = re.compile("[0-9]")

        for chars in password:
            if lowercase.match(chars):
                lower += 1
            elif uppercase.match(chars):
                upper += 1
            elif numberpattern.match(chars):
                numbers += 1

        if len(password) < 8:
            return apology("Password must be atleast 8 characters long")
        if lower < 1 or upper < 1 or numbers < 1:
            return apology("Password must be a combination of lowercase letters, uppercase letters and numbers")

        # If passwords do not match
        if not (password == confirmation):
            return apology("Passwords do not match")

        # If username is already taken
        taken = db.execute("SELECT * FROM users WHERE username = ?", username)
        if taken:
            return apology("Username is already taken")
        else:
            password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            current_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password_hash)
            session["user_id"] = current_user
            return redirect("/")


# Log In function
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash('You were succesfully logged in!')
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


# Log Out function
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# Home page
@app.route("/")
@login_required
def index():
    return render_template("index.html")


# Flight Tickets page
@app.route("/flights", methods=["GET", "POST"])
@login_required
def flights():
   
    if request.method == 'GET':
        return render_template("flights.html")
    else:
        # Get user's input
        source = request.form.get("source").upper().strip()
        destination = request.form.get("destination").upper().strip()
        date = request.form.get("departure")

        passengers = request.form.get("passengers")
        travelClass = request.form.get('class')
        currency = request.form.get("currency")

        if not passengers:
            passengers = 1
        if not travelClass:
            travelClass = 'ECONOMY'
        if not currency: 
            currency = 'INR'

        # Validating input
        if not (source and destination and date):
            return apology("Invalid input")

        # Lookup data
        dataset = lookup(source, destination, date, passengers, travelClass, currency)
        if dataset:
            info = extract_data(dataset)
            return render_template("flights.html", dataset=info, results=len(info), date=date, passengers=passengers)
        else:
            return apology("No results found")


# Tracker
@app.route("/tracker", methods=['GET', 'POST'])
@login_required
def tracker():
    if request.method == 'GET':
        return render_template("tracker.html")
    else:
        # Get user's input
        flightCode = request.form.get("flight-iata").upper().strip()

        # Validating input
        if not flightCode:
            return apology("Invalid input")
        
        dataset = trackFlight(flightCode)
        if dataset:
            # Query database for existing bookmarks
            bookmarks = list()
            users_bookmarks = db.execute("SELECT flight_iata FROM bookmarks WHERE user_id = ?", session["user_id"])
            for bk in users_bookmarks:
                bookmarks.append(bk['flight_iata'])
            print(bookmarks)
            return render_template("tracker.html", dataset=dataset, bookmarks=bookmarks)
        else:
            return apology("No results found")


@app.route("/search")
def search():
    # For the searchbox autocomplete
    q = request.args.get('q') + '%'
    p = request.args.get('p')
    results = db.execute("SELECT * FROM airports WHERE iata LIKE ? OR city LIKE ? OR name LIKE ? LIMIT 4", q, q, q)
    return render_template("search.html", results=results, path=p)


@app.route("/bookmarks", methods=["GET", "POST"])
def bookmarks():
    if request.method == "POST":
        flightCode = request.form.get("flightCode")
        dataset = trackFlight(flightCode)
        user_id = session["user_id"]
        airlines = dataset['airlines']
        dep_iata = dataset['dep_iata']
        depCity = dataset['depCity']
        arr_iata = dataset['arr_iata']
        arrCity = dataset['arrCity']

        # Query the database for existing bookmarks
        codeExists = db.execute("SELECT * FROM bookmarks WHERE flight_iata = ? AND user_id = ?", flightCode, user_id) 
        if (codeExists):
            # Update the flight's information in the database
            db.execute("UPDATE bookmarks SET dep_iata = ?, dep_city = ?, arr_iata = ?, arr_city = ? WHERE user_id = ? and flight_iata = ?", 
                       dep_iata, depCity, arr_iata, arrCity, user_id, flightCode)
        else:
            # Add a new bookmark
            db.execute("INSERT INTO bookmarks VALUES (?, ?, ?, ?, ?, ?, ?)", user_id, 
                       flightCode, airlines, dep_iata, depCity, arr_iata, arrCity)
        
    user_data = db.execute("SELECT * FROM bookmarks where user_id = ?", session["user_id"])
    return render_template("bookmarks.html", dataset=user_data)


@app.route("/remove", methods={"POST", "GET"})
def remove():
    # For removing any existing bookmarks
    if request.method == "POST":
        flightCode = request.form.get("flight-iata")
        db.execute("DELETE FROM bookmarks WHERE flight_iata = ? AND user_id = ?", flightCode, session["user_id"])
    return redirect("/bookmarks")


    