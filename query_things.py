

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Base, FoundWords, LetterBank, WordBank, Subject
 
 
engine = create_engine('sqlite:////Users/evanpiermont/Desktop/scrabble/restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# FILTERING WITH JOIN

#q = session.query(MenuItem).join(Restaurant).filter(Restaurant.name == 'Urban Burger').all()
#
#for item in q:
#
#    print "The %s costs %s" % ( item.name, item.price)

#FILTERING


#q = session.query(LetterBank).first()
#currentWordBank = session.query(WordBank).join(LetterBank).filter(LetterBank.name == q.name).all()
#
#qfw = session.query(FoundWords).all()
#                
#cwb = [] #list of the current word bank
#fwl = [] #list of previously found words (update by user)
#                
#for i, item in enumerate(currentWordBank):
#    cwb.append(item.word)
#    print item.word
#                    
#for i, item in enumerate(qfw):
#    fwl.append(item.word)

q = session.query(Subject)[2]
currentWordBank = session.query(LetterBank).join(Subject).filter(Subject.subject_name == q.subject_name).all()


for i in currentWordBank:
    print i.letter1
    print i.letter2
    print i.letter3



#FILTERING AND CHANGING AN ENTRY 

#vb = session.query(MenuItem).join(Restaurant).filter(MenuItem.name == 'Veggie Burger').filter(Restaurant.name == 'Urban Burger').first()
#
#vb.price = '$2.99'
#session.add(vb)
#session.commit
#
#uvb = session.query(MenuItem).filter(MenuItem.name == 'Veggie Burger')
#
#for item in uvb:
#    print item.restaurant.name
#    print item.price
#    print "\n"

#FILTERING AND CHANGING ALL!!! ENTRY

#vb = session.query(MenuItem).filter(MenuItem.name == 'Veggie Burger')
#
#for item in vb:
#    if item.price != '$2.99':
#        item.price = '$2.99'
#        session.add(item)
#
#session.commit()

#FILTE AN ENTRY 

#for item in vb:
#    print item.restaurant.name
#    print item.price
#    print "\n"
    
#spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
#session.delete(spinach)
#session.commit() 
