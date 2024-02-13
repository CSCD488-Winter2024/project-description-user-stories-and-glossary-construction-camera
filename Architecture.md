R1 - The device will send some sort of packet to the web server, then using SMTP it will send out a alert
to the listed emails.

R2 - On top of having an alert sent, we will also use transfer a video of the violation sent 
to the webserver and store it in a database.

R3 - We will use some sort of ping-like packet to alert the system to start up and shut down.  This alert
will come from the overviewers deivce.

R4 - We will use some sort of database, that looks essentially like a file system, that saves the videos.
Each day will have its own folder and will be stored for 1 week.

R5 - Will will have a script that compresses the video files and sents it through SMTP to the desired person.

R6 - Errors will be sent to the webserver and then forwarded to the maintence personal.

R7 - Data on the device has to be accessable locally for the maintence personal.

R8 - Updates will need to be installed via cables, this is to keep the device secure and not allow
any changes from the web. 
