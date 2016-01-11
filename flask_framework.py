from flask import Flask, request, render_template
app = Flask(__name__)

from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from random import randint

from db_setup import LetterBank, FoundWords, WordBank, Subject, Base

import cgi

engine = create_engine('sqlite:////Users/evanpiermont/Desktop/scrabble/restaurantmenu.db') #location of the db


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


currentLetterBank = randint(0,2) #random from 0 to the number of letter banks we have
q = session.query(LetterBank)[currentLetterBank] #get the current letterbank, based on random above (change to vary based on user)

@app.route('/')
@app.route('/login')
def Login():
    return render_template('login.html')


@app.route('/hello')
def WordPage():
    return render_template('scrabble.html', q=q)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)



