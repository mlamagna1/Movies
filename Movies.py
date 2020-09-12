import requests
import json
from pprint import PrettyPrinter
from wtforms import StringField, Form, SelectField
from wtforms.validators import DataRequired

class Responses:
    def __init__(self):
        self.movieData = {}

    def getMovieAttr(self,fname):
        pp = PrettyPrinter()
        data_URL = 'http://www.omdbapi.com/?apikey='+'66405531'
        year = ''
        movie = fname 
        print(fname)
        params = {
            't':movie,
            'type':'movie',
            'y':year,
            'plot':'full'
        }
        response = requests.get(data_URL,params=params).json()
        #pp.pprint(response)
    
        #print(type(response))
        #print(response['Rated'])
        self.setResponse(response)
        #pp.pprint(getResponse())



    def setResponse(self,response):
        self.movieData = response
        pp = PrettyPrinter()
        #pp.pprint(self.movieData)
    def getResponse(self):
        return self.movieData

class MovieSearchForm(Form):
    #choices = ""
    #select = SelectField('Search for Movie:')
    search = StringField('')