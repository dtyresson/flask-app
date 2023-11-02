from pyttpass.extensions import db

class Password(db.Model):
    __tablename__ = 'password'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    website = db.Column(db.String(100))
    value = db.Column(db.String(100))
    desc = db.Column(db.Text)

    def __init__(self, name, website, value, desc):
        self.name = name
        self.website = website
        self.value = value
        self.desc = desc

    def __repr__(self):
        return f'<Password "{self.name}">'