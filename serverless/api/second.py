from http.server import BaseHTTPRequestHandler
from os.path import join
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = "ali walid file "
        message1 = "welcome in my serverless "

        self.wfile.write(message.encode())
        self.wfile.write(message1.encode())

        return 

