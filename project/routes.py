from project import app, db
from project.models import Section, Recommendation, GlossaryTerm
from flask import render_template, redirect, url_for
from project.forms import GlossaryTermForm


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

# I will create this using just @app.route decorator, but may create a glossary blueprint. At the moment, I'm also going to have a separate template, though I want to get it into a modal in the glossary template
@app.route('/create_glossary_term', methods=['GET','POST'])
def create_glossary_term():
    form = GlossaryTermForm()

    if form.validate_on_submit():
        newGlossaryTerm = GlossaryTerm(name=form.name.data, description=form.description.data, notes=form.notes.data)
        db.session.add(newGlossaryTerm)
        db.session.commit()
        return redirect(url_for('glossary'))

    return render_template('create_glossary_term.html', form=form)
