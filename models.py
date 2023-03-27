import string
from datetime import  datetime
from random import  choices
from url import db
from flask import render_template,url_for,request

class urls(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    orginal_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5),unique = True)
    date_created = db.Column(db.DateTime,default = datetime.now)

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()


    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters,k = 5))

        link = self.query.filter_by(short_url = short_url).first()

        if link:
            return self.generate_short_link()
        return short_url
