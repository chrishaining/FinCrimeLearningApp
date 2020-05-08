from project import db
from flask_login import UserMixin

class Recommendation(db.Model, UserMixin):
    __tablename__ = 'recommendations'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    interpretation = db.Column(db.Text, nullable=False)
    section = db.relationship(Section)

    def __init__(self, text, interpretation, section_id):
        self.text = text
        self.interpretation = interpretation
        self.section_id = section_id

    def __repr__(self):
        return f"Recommendation {self.id}"

class Section(db.Model, UserMixin):
        __tablename__ = 'sections'
        id = db.Column(db.Integer, primary_key=True)
        letter = db.Column(db.Char, nullable=False)
        title = db.Column(db.Text, nullable=False)
        recommendations = db.relationship('Recommendation', backref='text', lazy=True)

        def __init__(self, letter, title):
            self.letter = letter
            self.title = title

        def __repr__(self):
            return f"Section {self.letter}"

# a decision - do I include the subheadings within sections? Not all sections include subheadings, and I'm not yet convinced how useful these subheadings will be.
