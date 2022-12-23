from cs50 import SQL
import json

db = SQL("sqlite:///airlines.db")

# with open("airports.json") as file:
#     jsonobj = json.load(file)
#     for data in jsonobj:
#         try:
#             name = jsonobj[data]["name"]
#             iata = jsonobj[data]["iata"]
#             city = jsonobj[data]["city"]
#             state = jsonobj[data]["state"]
#             country = jsonobj[data]["country"]
#         except (KeyError, ValueError, TypeError):
#                 continue
#         if (name != "") and (iata != "") and (city != "") and (state != "") and (country != "") and (name and iata and city and state and country):
#             db.execute("INSERT INTO airports VALUES (?, ?, ?, ?, ?)", name, iata, city, state, country)
#         else: 
#             continue