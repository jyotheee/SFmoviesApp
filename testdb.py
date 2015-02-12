import os
os.environ['DATABASE_URL'] = "sqlite:///movies_test.db"

import unittest
import model
from model import Movie

class TestDBFunctions(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		#reset test database
		model.dbsession.execute('DELETE FROM movies') 

	def test_db_entry_test(self):

		movie = Movie(title='Test Film Name', location='LocationSF1');
		model.dbsession.add(movie);
		model.dbsession.commit();

		movie_check = model.dbsession.query(model.Movie).filter_by(title='Test Film Name').one()

		self.assertEqual(movie_check.title, 'Test Film Name')
		self.assertEqual(movie_check.location, 'LocationSF1')


def main():
	unittest.main()

if __name__ == "__main__":
	main()

