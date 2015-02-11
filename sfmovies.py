from flask import Flask, render_template, redirect, request, flash, url_for, jsonify
import jinja2
import json
import model
from model import Movie

app = Flask(__name__)
app.secret_key = "secretkey"
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/movies")
def getmoviesfromdb():
    movie_list = model.dbsession.query(model.Movie).limit(20).all()
    
    # make a dictionary of all the movies
    output = {}
    for movie in movie_list:
    	if movie.title in output:
    		output[movie.title].append(movie.location)
    	else:
    		output[movie.title] = [movie.location]

    # make an array of objects from the above dictionary
    outlist = []
    for k,v in output.items():
    	moviedict = {}
    	moviedict['title'] = k
    	moviedict['location'] = v
    	outlist.append(moviedict)

    return jsonify(collection=outlist)
    #return jsonify(collection=[i.json_view() for i in movie_list])

def json_view(self):
	return {title: self.title, location: self.location}
    
    
if __name__ == '__main__':
    app.run()
