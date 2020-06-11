from flask import Flask, render_template, request
from rank import *
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    rankClass = Rank().search
    searchResults = rankClass(text)

    if searchResults:
    	return render_template('results.html', myList=searchResults)
    else:
    	return render_template('page_not_found.html')

if __name__=='__main__':
    app.run()