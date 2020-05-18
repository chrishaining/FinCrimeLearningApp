from project import app, db
from project.models import Section, Recommendation, GlossaryTerm
from flask import render_template, redirect, url_for, request
from project.forms import GlossaryTermForm #, RecommendationForm

############################
### show homepage ###
############################
@app.route('/')
def home():
    return render_template('home.html')

############################
### show recommendations ###
############################
@app.route('/fatf_recommendations')
def fatf_recommendations():
    recommendations = Recommendation.query.all()
    return render_template('fatf_recommendations.html', recommendations=recommendations)

###########################
### edit recommendation ###
###########################
# @app.route('/<recommendation_id>/update', methods=['GET', 'POST'])
# def update_recommendation(recommendation_id):
#
#     recommendation = Recommendation.query.get_or_404(recommendation_id)
#
#     form = RecommendationForm()
#
#     if form.validate_on_submit():
#         glossary_term.title = form.title.data
#         glossary_term.text = form.text.data
#         db.session.commit()
#         return redirect(url_for('fatf_recommendations', recommendation_id=recommendation_id))
#
#     elif request.method == 'GET':
#         form.title.data = recommendation.title
#         form.text.data = recommendation.text
#
#     return render_template('fatf_recommendations.html', form=form)


#####################
### show glossary ###
#####################
@app.route('/glossary')
def glossary():
    glossaryTerms = GlossaryTerm.query.all()
    return render_template('glossary.html', glossaryTerms=glossaryTerms)

############################
### create glossary term ###
############################

# I will create this using just @app.route decorator, but may create a glossary blueprint. At the moment, I'm also going to have a separate template, though I want to get it into a modal in the glossary template
@app.route('/create_glossary_term', methods=['GET','POST'])
def create_glossary_term():
    form = GlossaryTermForm()

    if form.validate_on_submit():
        new_glossary_term = GlossaryTerm(name=form.name.data, description=form.description.data, notes=form.notes.data)
        db.session.add(new_glossary_term)
        db.session.commit()
        return redirect(url_for('glossary'))

    return render_template('create_glossary_term.html', form=form)



############################
### update glossary term ###
############################
@app.route('/<glossary_term_id>/update', methods=['GET', 'POST'])
def update_glossary_term(glossary_term_id):

    glossary_term = GlossaryTerm.query.get_or_404(glossary_term_id)

    form = GlossaryTermForm()

    if form.validate_on_submit():
        glossary_term.name = form.name.data
        glossary_term.description = form.description.data
        glossary_term.notes = form.notes.data
        db.session.commit()
        return redirect(url_for('glossary', glossary_term_id=glossary_term.id))

    elif request.method == 'GET':
        form.name.data = glossary_term.name
        form.description.data = glossary_term.description
        form.notes.data = glossary_term.notes

    return render_template('create_glossary_term.html', form=form)


############################
### delete glossary term ###
############################
@app.route('/<int:glossary_term_id>/delete', methods=['GET', 'POST'])
def delete_glossary_term(glossary_term_id):

    glossary_term = GlossaryTerm.query.get_or_404(glossary_term_id)

    db.session.delete(glossary_term)
    db.session.commit()
    return redirect(url_for('glossary'))
