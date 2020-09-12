#from app import app
#from db_setup import init_db, db_session
from flask import Flask
from flask import flash, render_template, request, redirect
from Movies import Responses
from Movies import MovieSearchForm
from wtforms import StringField, Form, SelectField
from wtforms.validators import DataRequired
from Movies import Responses

app = Flask(__name__)
newSearch = Responses()
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    search = MovieSearchForm(request.form)
    
    if request.method == 'POST':
        return search_results(search)
    return render_template('home.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    print(search_string)
    if search.data['search'] != '':
        print(search_string)
        newSearch.getMovieAttr(search_string)
        texts = newSearch.getResponse()
        results = texts
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)
    
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()