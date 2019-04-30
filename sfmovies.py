from flask import Flask, render_template, redirect, request, flash, url_for, jsonify
import jinja2
import json
import model
from model import Movie
import sys

app = Flask(__name__)
app.secret_key = "secretkey"
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    gmaps = {}
    mapskeyvalue = app.config.get('mapskey')
    gmaps['key'] = mapskeyvalue
    return render_template("index.html", mapskey=gmaps)

@app.route("/movies")
def getmoviesfromdb():
    movie_list = model.dbsession.query(model.Movie).all()
    
    # make a dictionary of all the movies in the database. Each movie can map to many locations
    output = {}
    for movie in movie_list:
        if movie.title in output:
            output[movie.title].append(movie.location)
        else:
            output[movie.title] = [movie.location]

    # make an array of objects from the above dictionary to send to frontend view
    outlist = []
    for k,v in output.items():
        moviedict = {}
        moviedict['title'] = k
        moviedict['location'] = v
        outlist.append(moviedict)

    return jsonify(collection=outlist)    
    
if __name__ == '__main__':
    app.config['mapskey'] = sys.argv[1]
    app.run()
