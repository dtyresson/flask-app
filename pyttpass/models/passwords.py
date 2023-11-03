from pyttpass.extensions import db
from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField

class Password(db.Model):
    __tablename__ = 'password'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    website = db.Column(db.String(100))
    username = db.Column(db.String(20))
    value = db.Column(db.String(50))
    desc = db.Column(db.Text)

    def __init__(self, name, website, username, value, desc):
        self.name = name
        self.website = website
        self.username = username
        self.value = value
        self.desc = desc

    def __repr__(self):
        return f'<Password "{self.name}">'

class AddPassword(FlaskForm):
    # id used only by update/edit
    id = HiddenField()
    name = StringField('Name')
    website = StringField('Website')
    username = StringField('Username')
    value = StringField('Password')
    desc = StringField('Description')
    submit = SubmitField('Add/Update Record')