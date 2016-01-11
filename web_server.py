from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from random import randint

from db_setup import LetterBank, FoundWords, WordBank, Base

import cgi

PORT = 8080

numWordsFound = 0

currentLetterBank = randint(0,1) #random from 0 to the number of letter banks we have

engine = create_engine('sqlite:////Users/evanpiermont/Desktop/scrabble/restaurantmenu.db') #location of the db

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

q = session.query(LetterBank)[currentLetterBank] #get the current letterbank, based on random above (change to vary based on user)
currentWordBank = session.query(WordBank).join(LetterBank).filter(LetterBank.name == q.name).all()

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self): #this creates the inital html page.
        
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                qfw = session.query(FoundWords).delete() #each new page will reset the current list of found words. 
                

                message = ""
                message += """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <link type="text/css" rel="stylesheet" href="scrabble.css" />
                    <script type="text/javascript" language="Javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
                    <script src="scrabble.js" language="Javascript" type="text/javascript"></script>
                        
                    <title> </title>
                </head>
                <body>
                    <div id='background'>
                        
                        
                <table class="letter_table">
                    <col width="10%" />
                    <col width="10%" />
                    <col width="10%" />
                    <col width="10%" />
                    <col width="10%" />
                    <col width="10%" />
                  <tr> """
                message += """
                    <td id=letter0>%s</td>
                    <td id="letter1">%s</td>
                    <td id="letter2">%s</td>
                    <td id="letter3">%s</td>
                    <td id="letter4">%s</td>
                    <td id="letter5">%s</td>
                  </tr>
                </table>
                
                <form method='POST' enctype='multipart/form-data' action='/hello_words' id="contract-input-box">
                <input type="text" autocomplete="off" autofocus="autofocus" name="word" id="contract-input"><input type="submit" value="Submit" id=submit>
                </form>
                """ % (q.letter0, q.letter1, q.letter2, q.letter3, q.letter4, q.letter5)

 
                message += """
                </div>
                </body>
                </html>"""
                
                self.wfile.write(message)
                print message
                return
        

            try:
                #Check the file extension required and
                #set the right mime type

                sendReply = False
                if self.path.endswith(".html"):
                        mimetype='text/html'
                        sendReply = True
                if self.path.endswith(".jpg"):  
                        mimetype='image/jpg'
                        sendReply = True
                if self.path.endswith(".gif"):
                        mimetype='image/gif'
                        sendReply = True
                if self.path.endswith(".js"):
                        mimetype='application/javascript'
                        sendReply = True
                if self.path.endswith(".css"):
                        mimetype='text/css'
                        sendReply = True

                if sendReply == True:
                        #Open the static file requested and send it
                        f = open(curdir + sep + self.path) 
                        self.send_response(200)
                        self.send_header('Content-type',mimetype)
                        self.end_headers()
                        self.wfile.write(f.read())
                        f.close()
                return

            except IOError:
                self.send_error(404,'File Not Found: %s' % self.path)
                
    def do_POST(self): #creates the page after a word has been submited.
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('word') #content from the form is saved in messagecontent[0]
                
                qfw = session.query(FoundWords).all()
                
                cwb = [] #list of the current word bank
                fwl = [] #list of previously found words (update by user)
                                
                for i, item in enumerate(currentWordBank):
                    cwb.append(item.word)
                    print item.word
                                    
                for i, item in enumerate(qfw):
                    fwl.append(item.word)
                
                
                if messagecontent[0] in cwb: #make sure that the content is a valid word, save if yes, discard if no
                    if messagecontent[0] not in fwl: #make sure the content is not a duplicate
                        found1 = FoundWords(word = messagecontent[0]) #commits the found word
                        session.add(found1)
                        session.commit()
                
                fw = ""
                qfw = session.query(FoundWords).all() #outputs all current found words
                
                first = True
                for item in qfw:
                    if first:
                        first = False
                        fw += item.word.upper()
                    else:
                        fw += "</span>, <span class=redtext>" + item.word.upper()
                              
                
                message = ""
                message += """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <link type="text/css" rel="stylesheet" href="scrabble.css" />
                    <script type="text/javascript" language="Javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
                    <script src="scrabble.js" language="Javascript" type="text/javascript"></script>
                        
                    <title> </title>
                </head>
                <body>
                    <div id='background'>
                        
                        
                <table class="letter_table">
                    <col width="10%" />
                    <col width="10%" />
                    <col width="10%" />
                    <col width="10%" />
                    <col width="10%" />
                    <col width="10%" />
                  <tr> """
                message += """
                    <td id=letter0>%s</td>
                    <td id="letter1">%s</td>
                    <td id="letter2">%s</td>
                    <td id="letter3">%s</td>
                    <td id="letter4">%s</td>
                    <td id="letter5">%s</td>
                  </tr>
                </table>
                
                <form method='POST' enctype='multipart/form-data' action='/hello_words' id="contract-input-box">
                <input type="text" autocomplete="off" autofocus="autofocus" name="word" id="contract-input"><input type="submit" value="Submit" id=submit>
                </form>
                """ % (q.letter0, q.letter1, q.letter2, q.letter3, q.letter4, q.letter5) #places letters in the correct boxes

                message += "<div id=output>You've found:<span class=redtext> %s</span>.</div>" % fw #renders output letters according to the above sript (db of found words)
               
                message += """
                </div>
                </body>
                </html>"""
                
                self.wfile.write(message)
                print message
        except:
            pass

def main():
    try:
        server = HTTPServer(('', PORT), MyHandler)
        print 'Server Running on Port %s' % PORT
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
