import model
from model import Movie
import csv

#importing movie info from data/Film_Locations_in_San_Francisco.csv
def load_movies(session):
    with open('data/Film_Locations_in_San_Francisco.csv', 'rb') as csvfile:
        moviedata = csv.reader(csvfile, delimiter = ",")
        for row in moviedata:
            mtitle = row[0].decode("utf-8")             #converting byte strings to Unicode strings
            mlocation = row[2].decode("utf-8")
            movie = Movie(title=mtitle, location=mlocation)
            session.add(movie)
        session.commit()

def main(session):
    # Loading all the movies from the CSV file to the database session
    load_movies(session)
    pass

if __name__ == "__main__":
    session=model.connect()
    main(session)

