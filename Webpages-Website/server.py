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
        elif self.path == '/changePassword.html': 
            # Serve the changePassword.html file
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('changePassword.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/changePhoneNumber.html': 
            # Serve the changePhoneNumber.html file
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('changePhoneNumber.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/changeUsername.html': 
            # Serve the changeUsername.html file
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('changeUsername.html', 'rb') as file:
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

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_params = parse_qs(post_data.decode('utf-8'))

        if self.path == '/connect.php':
            # Here you can handle the POST request to connect.php
            # For simplicity, let's just print the received data
            print(post_params)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'success')  # Send a success response
        
        elif self.path == '/changePasswordScript.php':
            # Handle the POST request for changePassword.php
            # Process the post_params as needed
            print("POST request received from changePassword.php:")
            print(post_params)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'success')

        elif self.path == '/changeUsernameScript.php':
            # Handle the POST request for changeUserName.php
            # Process the post_params as needed
            print("POST request received from changeUsernameScript.php:")
            print(post_params)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'success')

        elif self.path == '/changePhoneNumberScript.php':
            # Handle the POST request for connect.php
            # Process the post_params as needed
            print("POST request received from changePhoneNumberScript.php:")
            print(post_params)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'success')
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

