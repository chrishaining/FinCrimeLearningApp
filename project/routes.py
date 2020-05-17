from project import app
from project.models import Section, Recommendation, GlossaryTerm
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/fatf_recommendations')
def fatf_recommendations():
    recommendations = Recommendation.query.all()
    return render_template('fatf_recommendations.html', recommendations=recommendations)

@app.route('/glossary')
def glossary():
    glossaryTerms = GlossaryTerm.query.all()
    return render_template('glossary.html', glossaryTerms=glossaryTerms)
