# README is not yet complete since we have only barely started implementing the project

# AI/ML Construction Camera
## The project is a box with a camera installed that will overlook a construction site. It has an AI installed that will learn and identify workers that are not wearing PPE, notifying the correct personel so they can rectify the situation. It will notify them through a website and simple sms message sent to their phones.
### An AI camera that watches over construction sites and identifies workers without PPE on.
Every year hundreds of construction workers are hurt and some die from PPE related accidents that are easily preventable. This will help to reduce said accidents by ensuring workers wear the neccesary gear when on the site. By simply installing a box and logging in, you can watch over the site without having to be there. Multiple cameras can also be connected to make a perimeter around the site if needed. 
### Installation
Comsumer - 
For installation, simply connect the box at a desired vantage point, connect it to power, and login using the website to connect it to your phone and account.

Dev -
  Raspberry PI portion: You will need a rasberry pi (RPI5 will work best) with some type of camera add-on.  The RPI will need to have rasberry pi OS installed.  You will then simply clone the repo onto it, then run the bash script to get it setup. (script is not yet 
  made)

  Webserver portion: The Web server works on a linux server.  The server is built on 3 main scripts, the python http server, the python flask api, and the video transfer script.  To begin, intially you need to clone the repo and go to the Web-Server folder.  From there    we will first create the MariaDb database within a docker container. To do that follow the instructions on this URL, the api will be in the api.py file. https://hackernoon.com/getting-started-with-mariadb-using-docker-python-and-flask-pa1i3ya3                            Once that has been setup and the credentials have been changed in the api.py foler that part should be done.  At that part the website should be ready to run locally, to do this you will run the server.py http server and the api.py flask api.  This will be done by     
  using "python3 <fileName.py>" for each of those files in different terminals.  Once this is done the website should be available through localhost. From here you can work on devlopment thorugh localhost. 
  
  Hosting portion: To host this website for devices outside the network we will need to do a few more additional steps.  The first being finding the servers public IP, and opening ports for the website.  To find your public IP you can use a website (anyone found when 
  you search "whats my public IP").   From there we need to open a few ports, I used port 8000 for http server, port 80 for nginx, port 6000 for the flask api, and port 5000 for the file transfer script (we will talk about this after this).  Do that through your router 
  settings page.  Once that is done we will also need to create a reverse proxy using nginx.  To do this we will install nginx and create a config file for it.  This file will listen on port 80 of your public IP and redirect requests depending if they are requesting the 
  api or http server. This config pretty much gives directions to request depending on if they are are aiming to make http requests or api request (since they are on different ports).  Once this is done you should be up and running for devices not on your local network. 
  Depending on your servers config you may have to disable some security features of your file wall or selinux, but will differ for each linux distrobution. 

  Video Transfer Portion: This is a single script that also uses flask to export videos from the RPI to the server.  It uses flask, and is ran by using "python3 /videos/server.py" (in the repo it does have the same name as the http server, but is in the videos folder). 
  Once its running it should import the videos that are taken from the RPI and display them on the video page after login. 
  
### Prerequisites
An account will have to be made on the website to ensure you can connect your cameras after you install them. The camera will require power as well to operate. No other set-up will need to be done. 
### Add-ons
TODO: List which add-ons are included in the project, and the purpose each add-on serves in your app.
### Installation Steps
TODO: Describe the installation process (making sure you mention bundle install).
Instructions need to be such that a user can just copy/paste the commands to get things set up and
running.
### Functionality
TODO: Write usage instructions. Structuring it as a walkthrough can help structure this section,
and showcase your features.
### nown Problems
TODO: Describe any known issues, bugs, odd behaviors or code smells.
Provide steps to reproduce the problem and/or name a file or a function where the problem lives.
### Contributing
TODO: Leave the steps below if you want others to contribute to your project.
1. Fork it!
2. Create your feature branch: git checkout -b my-new-feature
3. Commit your changes: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request :D
### Additional Documentation
TODO: Provide links to additional documentation that may exist in the repo, e.g.,
* Sprint reports
* User links
### License
If you haven't already, add a file called LICENSE.txt with the text of the appropriate license.
We recommend using the MIT license: https://choosealicense.com/licenses/mit/
