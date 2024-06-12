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
   ![image](https://github.com/CSCD488-Winter2024/project-description-user-stories-and-glossary-construction-camera/assets/124394194/38915928-d790-439d-89ee-853b52ab95b8)


#### Api Script & MariaDB
 - API resides in the api.py file
 - This uses flask as the framwork and uses a containerized MariaDB as the database
 - For information about the containerized db go to the link in the installation file.
 - The api.py file includes all the api endpoints that interact with the db and the video files.
 - The file has two main parts, the first of which being the setup/connection credentials:  
   ![image](https://github.com/CSCD488-Winter2024/project-description-user-stories-and-glossary-construction-camera/assets/124394194/0210ae70-bb7c-47a8-a291-6d715de8d973)
 - The second part is all the endpoints:  
   ![image](https://github.com/CSCD488-Winter2024/project-description-user-stories-and-glossary-construction-camera/assets/124394194/e65b8530-79ae-4527-9732-6aa48058ec9b)
 - Each time you restart the machine, you will have to start the MariaDB container using '''sudo docker start containerID'''


#### Reverse Proxy Server
  - We also use nginx as a reverse proxy to direct requests wether they are api or http requests
  - This setup will ultimately be dependent on your system, and will need to be setup occordingly.
  - In basic sense it will listen for requests on a port and redirect them to the port specified by the request. 



### RPI
  - One main file, '''final.py''', which is in charge of running the ML model, the webcam, recording, organzing files, and sending violations videos.
  - The software takes in two parameters. The first parameter is designed to account for innaccurately trained models or inproperly trained models. If the model isn't perfectly trained, and does not detect every single component accurately, then this parameter gives the model some leeway so that it may still be usable.
  - The second parameter is similar to the first. It is in charge of the overall violations for the entire video. At 0.50, if 50% of the video contained violations, then the video is tagged as a violation and sent to the IP address.
  - The '''results''' variable is what houses the prediction results from running the model on the recorded video. It also takes parameters. These parameters can be modified or additional parameters may be added. These can be found at: https://docs.ultralytics.com/modes/predict/.
  - The function also contains a for loop which iterates over every frame and counts the total detections for each class. The two classes are Hat and Person. The math portion then calculates whether the total amount of detections versus the deviation is too high, which triggers the violation portion of the script.
  - The rest of the script is in charge of recording video and creating directories.
