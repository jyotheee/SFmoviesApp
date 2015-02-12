import model
from model import Movie
import csv

def load_movies(session):
    #using Film_Locations_in_San_Francisco.csv

    with open('data/Film_Locations_in_San_Francisco.csv', 'rb') as csvfile:
        moviedata = csv.reader(csvfile, delimiter = ",")
        for row in moviedata:
            mtitle = row[0].decode("utf-8")             #converting byte strings to Unicode strings
            mlocation = row[2].decode("utf-8")
            movie = Movie(title=mtitle, location=mlocation)
            session.add(movie)
        session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_movies(session)
    pass

if __name__ == "__main__":
    session=model.connect()
    main(session)

