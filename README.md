# SFmoviesApp

This app was built as a part of the uber coding challenge. It lists all the movies that have been filmed in the city of San Francisco and maps the locations in the city where they were shot at. Users can select the movie by typing in the input form field. They can then click on the desired movie and view the movie locations on the map.

##Technology stack

The frontend was built using backbone MVC framework. It uses Backbone.js, Underscore.js, jQuery and GoogleMaps API. 

Backend consists of a SQLite database, SQLAlchemy and a Flask framework for python. Data is downloaded from from [DataSF:FilmLocations] https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am? into a cvs file. The database is seeded (seed.py) from this CSV file and stored as a Movie model (model.py) into the database table.

##Links

