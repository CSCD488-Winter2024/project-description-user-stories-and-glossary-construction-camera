# Installation Intructions:
- Initially we need to git clone the repo, to do this use the command: '''git clone <repo url>'''

## Webserver/Website Installations:
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

## Raspberry PI Installations:
