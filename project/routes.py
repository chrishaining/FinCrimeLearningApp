from project import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/fatf_recommendations')
def fatf_recommendations():
    return render_template('fatf_recommendations.html')

@app.route('/abbreviations')
def abbreviations():
    return render_template('abbreviations.html')
