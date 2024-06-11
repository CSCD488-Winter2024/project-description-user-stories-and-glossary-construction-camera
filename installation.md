# Installation Intructions:
- Initially we need to git clone the repo, to do this use the command: '''git clone <repo url>'''

## Webserver/Website Installations:
### Localhost/Developement setup
 - To start with webserver installation we need to navigate into the webserver folder.
 - Once done, make sure you have a install of python3 using your desired package manager.
 - After making sure you have a python3 installation, install docker, mariaDB and the mariaDB-c-connector, again using your desired package manager.
 - Once that is done follow the instructions from this url to setup the dockerized mariaDB database with connection the the api.py api file: https://hackernoon.com/getting-started-with-mariadb-using-docker-python-and-flask-pa1i3ya3
 - Make sure the credentials in the api.py file matched the ones you used while setting up the DB
 - Make sure all these python packages are installed using '''pip install <package>''':
   - flask
   - moviepy.editor
   - http.server
   - urllib.parse
   - json
   - mariaDB/c-connector
 - At this point you should be able to run the web server locally by running these commands:
  - '''python3 server.py''' & '''python3 api.py'''
 - Remember to be in the python virtual enviorment when running the api (detailed in the url above).
 - To access the website at this point just put localhost:portNumber into your browser url.


### How to make it available to off network devices 
 - We will first need to open your selected ports for the http server, api script, nginx, and the video transfer script. For me I used 8000, 5000, 80, 6000 in the same order as they were listed.
 - Next we'll need a reverse proxy to direct the requests to either the http server or the api script. 
 - To do this we are gonna need to do a few more steps, start off by installing nginx using your chosen package manager.
 - Now we are gonna make a config file for nginx that will act as our reverse proxy, this will listen to port 80 on our public IP and redirect the request to either localhost:8000 (http server) or localhost:5000 (api port) depending on the url ex.) "beginningOfURL/optionalPage" for the http server and "beginningOfURL/api" for the api.
 - Once this has been made, you should be able to run the previous commands to start the server, which at that point should be available to devices outside the network by inputting your public IP address.
 - If you cannot connect at this point you may need to modify your firewall or selinux secuirty depending on your linux distrobution, chatgpt is a great tool for figureing this out!

### Setting up the File transfer script - server side
 - All we need to do for this is run the script in the videos/server.py (yes it has the same file name as the http server, but is in a different folder) use this command: '''python3 videos/server.py'''
 - For this we will need port 6000 (or whatever port you chose) open which should have been done above.
 - This will also need setup on the RPI side, but we will explain that below. 

## Raspberry PI Installations:
 - Install Raspberry OS on the RPI
 - From the Scripts folder, move '''final.py''' along with '''yolov8m_custom.pt''' into their own directory. The script may need to be modified, since it uses absolute paths.
 - Run '''final.py''' and when it prompts for the parameters, enter 0.5 for both. It may not detect the webcam, in which case you may need to modify the camera it uses in the script. It is an int which corresponds to a USB port.
 - The IP in the script may also need to be modified depending on the IP of the server.
