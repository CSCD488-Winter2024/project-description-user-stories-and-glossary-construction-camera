# Overrall Description 
On most job sites PPE (personal protective equipment) is required by law or at least highly encouraged, 
due to the risk and danger of the work environment.  Many accidents are easily avoidable by simply wearing appropriate 
PPE devices, but that doesn’t guarantee the employees will wear them.  The intended users for our system would 
be employers and government agencies. Employers do not always enforce PPE usage on their employees or the employees 
themselves choose to not wear PPE while on the job.  This will protect negligent employers from possible OSHA 
violations and workplace misconduct while keeping the employees safe and reducing injuries.  The device acts as a 
safety net over the employees to protect them by detecting and identifying faults and notifying the correct 
authority.  A cellphone sized box with a camera and an I/O cable for power and network connection.  The program will 
be built using Python, Rust, Javascript, HTML, React JS, GPT3, Tensorflow/OpenCV, YOLO.  Raspberry PI4 Model B, 
Camera(Specs TBD), Housing box, physical Conner's server. The current alternative is to employ a ‘PPE lifeguard’ 
to watch over the job site and enforce employees to wear gear. This requires labor, time, resources, 
and constant vigilance, not to mention the unreliability of it if he makes friends. Having a machine watch over 
them would eliminate all of these human faults.


# Minimal Description
We envision the product to be a self-sustaining automated safety system that will help ensure the safety of 
the employees on any site by keeping track if they are wearing PPE at all times.. Simply install the box at a 
vantage point, and the AI learning software installed inside will use a camera to identify any workers that are not 
wearing appropriate PPE. Once detected, a video or screenshot will be uploaded to a phone or email alerting the 
supervisor of the employee, allowing them to take action as they wish.


# User Stories

## Functional Requirements

### Employees

As an employee I want to get alerts when a violation is detected so I or other employees can fix the problem. 

As an employee I want to be able to validate these violation by being able to reveiw the violation/video. 

### Business/Consultant/Overviewer - The person who actually employs the use of the device. 

As the overviewer I want to be able to start/stop the device

As the overviewer I want to be able to login and view the violation videos

As the overviewer I want to get alerts when a violation is made. 

As the overviewer I want to be able to request and get sent the video files of the violations. 

### Technition

As a technition I want to get error data without being on site.

As a technition I want to be able to export data from the device using physical cables

As a technition I want to be able to update/import data to the device using a physical cable


## Non-Functional requirements

Detection of violations of PPE rules.

Records of these violations, whether that be videos, descriptions, or notifications. 

Low cost for this system.

Easy setup for these systems. 

Minimum knowledge of computer systems to get it running.

Reliability of these systems 


# Glossary
PPE: Personal Protective Equipment.
Raspberry Pi: Microcontroller/Microcomputer that is the main circuit board brain that will process 
and calculate everything.

Camera: Device that allows the Pi to see visual data.

Housing Box: 3d printed or otherwise container/case for the Pi and the camera mount.

Server: Additional computer that the Pi will send data to, to allow the data to be seen and processed outside 
of the Pi itself.

I/O: Input/Output to and from the Pi.

OSHA: Occupational Safety and Health Administration. Agency that oversees worker safety.

AI/Machine Learning: Mathematical algorithm that is utilized in order to process camera data and analyze 
it to determine if any faults have occured.

YOLO/OpenCV/TensorFlow: Open source libraries for computer vision.

Python/Rust/JavaScript/HTML/React/Flask: Programming languages for development of application and website.

GPT3: AI library for data generation and lookup.



