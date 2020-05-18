from project import db, wa
# from flask_login import UserMixin


#############
## SECTION ##
#############
class Section(db.Model):
        __tablename__ = 'sections'

        __searchable__ = ['letter', 'title']

        id = db.Column(db.Integer, primary_key=True)
        letter = db.Column(db.CHAR, nullable=False, index=True)
        title = db.Column(db.Text, nullable=False, index=True)
        recommendations = db.relationship('Recommendation', backref='sections', lazy='dynamic')

        def __init__(self, letter, title):
            self.letter = letter
            self.title = title

        def __repr__(self):
            return f"Section {self.letter}"

####################
## RECOMMENDATION ##
####################
class Recommendation(db.Model):
    __tablename__ = 'recommendations'

    __searchable__ = ['id', 'title', 'text']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, index=True)
    text = db.Column(db.Text, nullable=False)
    # interpretation = db.Column(db.Text)
    section = db.relationship(Section)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'), nullable=False)

    def __init__(self, title, text, section_id):
        self.title = title
        self.text = text
        # self.interpretation = interpretation
        self.section_id = section_id

    def __repr__(self):
        return f"Recommendation {self.id}"

# a decision - do I include the subheadings within sections? Not all sections include subheadings, and I'm not yet convinced how useful these subheadings will be.


####################
## GLOSSARY TERM ##
####################
class GlossaryTerm(db.Model):
    __tablename__ = 'glossaryterms'

    __searchable__ = ['name', 'description', 'notes']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, default="Add notes") # I don't think the default does anything here.

    def __init__(self, name, description, notes="add notes"):
        self.name = name
        self.description = description
        self.notes = notes

    def __repr__(self):
        return f"Glossary term: {self.term}"
