from flask import Flask, request, redirect, url_for, render_template
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


# create an array with all subject names, taken from database
#sub = session.query(Subject).all()
#subjectnames = []
#
#for i in sub:
#    subjectnames.append(i.subject_name)
#
#
#currentLetterBank = randint(0,3) #random from 0 to the number of letter banks we have
#q = session.query(LetterBank).join(Subject).filter(Subject.subject_name ==
#                                                   'u0').one()  #get the current letterbank 

@app.route('/')
@app.route('/login')
def Login():
    return render_template('login.html', v=True)


@app.route('/hello', methods=['GET', 'POST'])
def LetterPage():

    if request.method == 'POST':
           subject_id=request.form['subject_id_input']
    
           sub = session.query(Subject).all()
           subjectnames = []
           for i in sub:
               subjectnames.append(i.subject_name)

           if subject_id in subjectnames:
               q = session.query(LetterBank).join(Subject).filter(Subject.subject_name ==
                                                                    subject_id).one()  #get the current letterbank 
               return render_template('scrabble.html', q=q, subject_id =
                                      subject_id, v=False, fw='poop')  
           # v is false means that output in not rendered. fw is found words.
           
           else:
               return render_template('login.html', v=False)
    else:
           return render_template('login.html', v=True)        

@app.route('/word', methods=['GET', 'POST'])
def WordPage():

    if request.method == 'POST':
        subject_id=request.form['subject_id']
        newWord=request.form['word']
        q = session.query(LetterBank).join(Subject).filter(Subject.subject_name ==
                                                            subject_id).one()  #get the current letterbank
        currentWordBank = session.query(WordBank).join(LetterBank).filter(LetterBank.name == q.name).all()
        qfw = session.query(FoundWords).all()
               
        cwb = [] #list of the current word bank
        fwl = [] #list of previously found words (update by user)
                        
        for item in currentWordBank:
            cwb.append(item.word)
                            
        for item in qfw:
            fwl.append(item.word)
        
        
        if newWord in cwb: #make sure that the content is a valid word, save if yes, discard if no
            if newWord not in fwl: #make sure the content is not a duplicate
                found1 = FoundWords(word = newWord, subject = subject_id) #commits the found word
                session.add(found1)
                session.commit()
        
        fw = [] 
        qfw = session.query(FoundWords).filter(FoundWords.subject == subject_id).all() #outputs all current found words
        
        for item in qfw:
            fw.append(item.word.upper())


        return render_template('scrabble.html', q=q, subject_id =
                                      subject_id, v=True, fw=fw) 
    else:
        return render_template('login.html', v=True)




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)



