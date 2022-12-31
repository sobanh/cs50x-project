
# CS50x Final Project - FlightRadar
FlightRadar is a simple web application that allows the user to track the live status of any flights. 

## Description

This application interfaces with Amadeus and AirLabs APIs to provide the user with information such as flight tickets, departure details, arrival details and the live status of the flights.

The Tracker page in the app includes a Google Map that shows the latest updated co-ordinates of a flight. It also allows the user to bookmark any flight for quick lookups. Provided with geo-location data is altitude, heading, and groundspeed information.

## Tools Used
- HTML 
- CSS
- JavaScript
- Python
- Flask
- SQLite

## Implementation

This web app was structured in HTML with the help of Jinja templates. It has a total of 9 HTML files stored in the templates folder. Each file is an extension of `layout.html` which forms the basic structure of all the pages in the application. 

CSS (Cascading Style Sheets) was used to describe the presentation of each HTML element. The design has been made as responsive as possible with the help of media queries.

An autocomplete feature for the search box was implemented with the help of JavaSvript. It queries the SQL database `airlines.db` for corresponding cities or airports based on the user's input. 

The backend server of this application has been implemented in Python. `app.py` is the main file that communicates with the front end of the application. Some helper functions are included in `helpers.py` to aid the process.

The SQLite database consists of four tables namely: airlines, airports, bookmarks and users. As the names suggest the IATA codes, along with other useful information, of various airlines and airports all over the world have been stored in `airlines` and `airports`. \
`bookmarks` is used to record the details of any flight the user wishes to keep a track of. 

## Features 

### 1. Flights
The first page of the application is the Flights page. It has a search box wherein the user can type in the IATA code of the source and destinations along with the departure date to find the cheapest flight tickets for a particular route. This data is provided by the Amadeus API.

![Flights](/static/preview/flights.png)

If however the user does not know the IATA code of a city, they can simply type in the airport or the city's name and then click on the IATA code that appears in the dropdown section.

![Autocomplete](/static/preview/autocomplete.png)

Once the user enters a valid input and clicks the Search button they are redirected to a the results page.

![Results](/static/preview/results.png)


### 2. Tracker
The second page of the application is called Tracker which allows the user to check the live status of a flight. This data is provided by the AirLabs API. 
To query the database enter the IATA code of the flight. On valid input the server responds with live co-ordinates of the flight marked on a Google Map, departure and arrival details along with flight attitude.
 
![Tracker](/static/preview/tracker.png)
![Tracker](/static/preview/tracker2.png)

As you can see, this page has a button that allows the user to bookmark the flight for future reference.

### 3. Bookmarks

The final page of this application is the Bookmarks page. It contains a list of all the flights bookmarked by the user. These can be easily tracked by the clicking the Track button.
![Bookmarks](/static/preview/bookmark.png)

If the user clicks the Track button they are redirected to the Tracker page. 

![Track](/static/preview/track.png)


## Responsive Design
With the ever increasing number of mobile users a responsive web design is an important factor in web development. As such, an attempt was made to style the HTML elements to be as responsive as possible. 

| Flights | Bookmarks | Tracker |
|--------------|--------------|-------------|
|![](/static/preview/responsive1.png)|![](/static/preview/responsive2.png)|![](/static/preview/responsive3.png)|


## About the Course
This is [CS50X](https://cs50.harvard.edu/x/2022/) , Harvard University's introduction to the intellectual enterprises of computer science and the art of programming for majors and non-majors alike, with or without prior programming experience. An entry-level course taught by Professor David J. Malan, CS50x teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, Python, SQL, and JavaScript plus CSS and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. The on-campus version of CS50x , CS50, is Harvard's largest course.

