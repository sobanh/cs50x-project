import os

from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from helpers import lookup

# Configure Application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/flights")
def flights():
    dataset = lookup()
    return render_template("flights.html", dataset=dataset, results=len(dataset))

@app.route("/search")
def search():
    return render_template("search.html")