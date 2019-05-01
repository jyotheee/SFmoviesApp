# SFmoviesApp

This app was built as a part of the uber coding challenge. It lists all the movies that have been filmed in the city of San Francisco and maps the locations in the city where they were shot at. Users can select the movie by typing in the input form field. They can then click on the desired movie and view the movie locations on the map.

##Technology stack

The frontend was built using backbone MVC framework. It uses Backbone.js, Underscore.js, jQuery and GoogleMaps API. There are three views to the Backbone model. The first view is to display the entire list of movies from the backend into a DOM element. This view provides an autocomplete feature on the form field that listens to 'keyup' events. Each movie displayed in the list has a separate view. This view listens to click events on its name and send the information to the maps view, which is the third one. The maps view geolocates the address and adds a marker on the map.

Backend consists of a SQLite database, SQLAlchemy and a Flask framework for python. Data is downloaded from [DataSF:FilmLocations] (https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?) into a csv file. The database is seeded (seed.py) from this CSV file and stored as a 'Movie' model (model.py) into the database table. Queries are written with SQLAlchemy to fetch the data and convert them into JSON objects (RESTful) to be sent as a collection to the frontend view. 

##Experience

I have no previous exposure to Backbone.js. It was a good learning experience for me to build this app using Backbone. I've also never use GoogleMaps API before. This is also the first time writing unit test cases in Python

##Enhancements

Geolocations for the movie shot locations were calculated in the front end view. This makes the app slow to load the markers on the Google Maps, especially if the number of locations are greater than 5. One way to avoid this delay is to calculate the geolocations in the backend and store it in the database for easier access.

I've read about frontend testing frameworks such as Mocha.js for testing Backbone interactions. Given more time, I would have implemented this framework. 

##Links

[Amazon EC2 SFMoviesApp] (http://35.167.205.240:8000/)

[Hackbright Project] (https://github.com/jyotheee/playWithRTC)

[LinkedIn DevelopHer Hackathon 2014] (https://github.com/jyotheee/Picky)

[LinkedIn] (https://www.linkedin.com/in/jyothimadhavapeddy)

