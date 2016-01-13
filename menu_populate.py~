

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from db_setup import Base, LetterBank, FoundWords, Subject, WordBank
 
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

letters0Stage = 'keniad'

letters1Stage = 'poucer'

letters2Stage = 'binlor'

letters3Stage = 'market'


#Letters 0
letters0 = LetterBank(
    name = letters1Stage,
    letter0 = letters0Stage[0],
    letter1 = letters0Stage[1],
    letter2 = letters0Stage[2],
    letter3 = letters0Stage[3],
    letter4 = letters0Stage[4],
    letter5 = letters0Stage[5])


session.add(letters0)
session.commit()

#words

words0 = ['aid', 'aide', 'akin', 'and', 'dank', 'dean', 'deink', 'den', 'die', 'din', 'dine', 'end', 'ide', 'idea', 'ink', 'inked', 'kin', 'kina', 'kind', 'kine', 'knead', 'naked']


for i in words0:
    words00 = WordBank(word = i, letter_bank = letters0)
    session.add(words00)
    session.commit()


#letters1

letters1 = LetterBank(
    name = letters1Stage,
    letter0 = letters1Stage[0],
    letter1 = letters1Stage[1],
    letter2 = letters1Stage[2],
    letter3 = letters1Stage[3],
    letter4 = letters1Stage[4],
    letter5 = letters1Stage[5])


session.add(letters1)
session.commit()

#words

words1 = ['cop', 'cope', 'coper', 'core', 'coup', 'coupe', 'crop', 'croup', 'cue', 'cup', 'cur', 'cure', 'ecru', 'euro', 'ore', 'our', 'per', 'pore', 'pour', 'puce', 'pure', 'recoup', 'repo', 'roe', 'rope', 'roue', 'rue']

for i in words1:
    words11 = WordBank(word = i, letter_bank = letters1)
    session.add(words11)
    session.commit()



#letters2

letters2 = LetterBank(
    name = letters2Stage,
    letter0 = letters2Stage[0],
    letter1 = letters2Stage[1],
    letter2 = letters2Stage[2],
    letter3 = letters2Stage[3],
    letter4 = letters2Stage[4],
    letter5 = letters2Stage[5])


session.add(letters2)
session.commit()

#words

words2 = ['bin', 'boil', 'born', 'broil', 'in', 'ion', 'iron', 'lion', 'lob', 'loin', 'nib', 'nil', 'nob', 'nor', 'oil', 'orb', 'rib', 'rob', 'robin', 'roil']

for i in words2:
    words22 = WordBank(word = i, letter_bank = letters2)
    session.add(words22)
    session.commit()

#letters3

letters3 = LetterBank(
    name = letters3Stage,
    letter0 = letters3Stage[0],
    letter1 = letters3Stage[1],
    letter2 = letters3Stage[2],
    letter3 = letters3Stage[3],
    letter4 = letters3Stage[4],
    letter5 = letters3Stage[5])


session.add(letters3)
session.commit()

#words

words3 =['are', 'ark', 'arm', 'armet', 'art', 'ate', 'ear', 'eat', 'era', 'eta', 'make', 'maker', 'mar', 'mare', 'mark', 'market', 'mart', 'mat', 'mate', 'mater', 'meat', 'met', 'rake', 'ram', 'rat', 'rate', 'reak', 'ream', 'take', 'taker', 'tam', 'tame', 'tamer', 'tar', 'tare', 'tea', 'teak', 'team', 'tear', 'term', 'tram', 'trek'] 
for i in words3:
    words33 = WordBank(word = i, letter_bank = letters3)
    session.add(words33)
    session.commit()




letterbanks = [letters0, letters1, letters2, letters3]

#enter users

for i in range(4): #range upto number of letter banks. user is u+unique
    user1 = Subject(subject_name = 'u'+str(i), letter_bank = letterbanks[i])
    session.add(user1)
    session.commit()

print "added stuff!"

