from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            # Serve the index.html file
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/videoPage.html':
            # Serve the videoPage.html file
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('videoPage.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/profile.html': 
            # Serve the profile.html file
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('profile.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()


def runStart(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    runStart()
