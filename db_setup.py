

# from flask_sqlalchemy import SQLAlchemy

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class LetterBank(Base):
    __tablename__ = 'letter_bank'

    id = Column(Integer, primary_key=True)
    name = Column(String(6), nullable=False)
    letter0 = Column(String(1), nullable=False)
    letter1 = Column(String(1), nullable=False)
    letter2 = Column(String(1), nullable=False)
    letter3 = Column(String(1), nullable=False)
    letter4 = Column(String(1), nullable=False)
    letter5 = Column(String(1), nullable=False)
    #words = Column(String(250), nullable=False)

class FoundWords(Base):
    __tablename__ = 'found_words'

    id = Column(Integer, primary_key=True)
    word = Column(String(6), nullable=False)
    #words = Column(String(250), nullable=False)

class WordBank(Base):
    __tablename__ = 'word_bank'

    word = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    letter_bank_id = Column(Integer, ForeignKey('letter_bank.id'))
    letter_bank = relationship(LetterBank)


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(5))
    letter_bank_id = Column(Integer, ForeignKey('letter_bank.id'))
    letter_bank = relationship(LetterBank)



engine = create_engine('sqlite:////Users/evanpiermont/Desktop/scrabble/restaurantmenu.db')


Base.metadata.create_all(engine)

