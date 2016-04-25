import MySQLdb
from flask import Flask, render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secret string here'

userpass = 'mysql://saranettle:pato1117@'
basedir = saranettle.mysql.pythonanywhere-services.com
dbname   = '/saranettle$cocktailsdb'
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


# each table in the database is a class
class Cocktail(db.Model):
    __tablename__ = 'cocktails'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    alcohol = db.Column(db.String)
    ingredients = db.Column(db.String)

    def __init__(self, name, alcohol, ingredients):
        self.name = name
        self.alcohol = alcohol
        self.ingredients = ingredients

    def __repr__(self):
        return '<Cocktail %s>' % self.name

@app.route('/')
def home():
    cocktails = Cocktail.query.all()
    return render_template('main.html', cocktails=cocktails)

@app.route('/<alcohol>')
def alcohol(alcohol):
    cocktails = Cocktail.query.all()
    primalcohols = Cocktail.query.filter_by(alcohol=alcohol).all()
    return render_template('alcohol.html', cocktails=cocktails, primalcohols=primalcohols, alcohol=alcohol)

@app.route('/Other')
def other():
        cocktails = Cocktail.query.all()
        return render_template('other.html', cocktails=cocktails)


@app.route('/drink/<name>')
def drinks(name):
    cocktails = Cocktail.query.all()
    drink = Cocktail.query.filter_by(name=name).first()
    return render_template('drink.html', cocktails=cocktails, name=name, drink=drink)


#if __name__ == '__main__':
#    app.run(debug=True)
