# Developer Guidelines
## These guidlines will explain the structure of this project and how it works  
  
## This project has two main parts, the Raspberry Pi part, and the Web server part we will explain each individually.   
The whole updated project is available from main

### Web Server
 - Resides in the Webpages-Website folder
 - The web server has 3 main parts:
   - Python HTTP server and pages
   - Flask API script and MariaDB database
   - Video Transfer script
  
#### HTTP Server
 - Resides in the server.py file in the Webpages-Website folder. 
 - This is the server that sets the paths for each page and sets the initial page to the login page.
 - It is very basic and is whats used to host the website on local host.
 - If a page is added we would need to implement it into this file.
 - ![image](https://github.com/CSCD488-Winter2024/project-description-user-stories-and-glossary-construction-camera/assets/124394194/38915928-d790-439d-89ee-853b52ab95b8)


#### Api Script & MariaDB
 - API resides in the api.py file
 - This uses flask as the framwork and uses a containerized MariaDB as the database
 - For information about the containerized db go to the link in the installation file.
 - The api.py file includes all the api endpoints that interact with the db and the video files.
 - The file has two main parts, the first of which being the setup/connection credentials: ![image](https://github.com/CSCD488-Winter2024/project-description-user-stories-and-glossary-construction-camera/assets/124394194/0210ae70-bb7c-47a8-a291-6d715de8d973)
 - The second part is all the endpoints: ![image](https://github.com/CSCD488-Winter2024/project-description-user-stories-and-glossary-construction-camera/assets/124394194/e65b8530-79ae-4527-9732-6aa48058ec9b)
 - Each time you restart the machine, you will have to start the MariaDB container using '''sudo docker start <containerID>'''



### RPI
