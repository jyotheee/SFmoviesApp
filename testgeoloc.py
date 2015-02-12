import os
import requests
import json
import unittest
import model


def geocode_zipcode(zipcode):
	
	resp =requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s' %(zipcode))
	g = json.loads(resp.text) 

	lng = g['results'][0]['geometry']['location']['lng']
	lat = g['results'][0]['geometry']['location']['lat']

	zip_coord = (lat, lng)
	
	return zip_coord

def geocode_searchterm(searchterm):
	
	resp =requests.get('https://maps.googleapis.com/maps/api/geocode/json?&address=%s' %(searchterm))
	g = json.loads(resp.text) 

	lng = g['results'][0]['geometry']['location']['lng']
	lat = g['results'][0]['geometry']['location']['lat']

	zip_coord = (lat, lng)

	print "zip_coord:", zip_coord
	
	return zip_coord


class MovieAppTestFunctions(unittest.TestCase):

	def test_coordinates(self):
		zipcode = 94612
		test_coordinate = (37.811315899999997, -122.2682245)

		self.assertEqual(geocode_zipcode(zipcode), test_coordinate)

	def test_searchterm(self):
		searchterm = 'Golden Gate Bridge'
		test_coordinate = (37.8199286, -122.4782551)

		self.assertEqual(geocode_searchterm(searchterm), test_coordinate)


def main():
	unittest.main()

if __name__ == "__main__":
	main()




