from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 8080

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ""
                message += """
                <!DOCTYPE html>
                <html lang="en">
<head>
    <link type="text/css" rel="stylesheet" href="scrabble.css" />
    <script type="text/javascript" language="Javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
    <script type="text/javascript" language="Javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
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
  <tr>
    <td id="letter0"></td>
    <td id="letter1"></td>
    <td id="letter2"></td>
    <td id="letter3"></td>
    <td id="letter4"></td>
    <td id="letter5"></td>
  </tr>
</table>

<form id="contract-input-box">
<input type="text" name="word" id="contract-input">
</form>

 <!--<div id=output>fbfd</div>-->
 <div id='error'></div>
        
    </div>
</body>
</html>"""
                self.wfile.write(message)
                print message
                return
        
            if self.path=="/":
                 self.path="/scrabble.html"

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

def main():
    try:
        server = HTTPServer(('', PORT), MyHandler)
        print 'Server Running on Porn %s' % PORT
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
