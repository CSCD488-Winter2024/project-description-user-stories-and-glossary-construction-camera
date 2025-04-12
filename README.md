# AI/ML Construction Camera

## Overview
The AI/ML Construction Camera is a smart monitoring system designed to oversee construction sites and ensure worker compliance with personal protective equipment (PPE) regulations. The device is housed in a weather-resistant box containing a camera and AI model, capable of identifying workers not wearing appropriate PPE. Notifications are sent via a web platform and SMS to designated personnel for quick intervention.

## Project Objective
To improve construction site safety by reducing preventable PPE-related injuries and fatalities. The system enables remote monitoring and management through a user-friendly web interface, with optional multi-camera setups for full perimeter coverage.

## Key Features
- AI-powered detection of PPE violations
- Real-time alerts via web and SMS
- Remote site access through secure login
- Scalable to multiple camera setups

## Installation Guide
Refer to `installation.md` for complete instructions.

### Consumer Installation
1. Mount the device at a strategic vantage point.
2. Connect to a power source.
3. Log in via the website to link the device to your account and phone.

### Developer Installation

#### Raspberry Pi Setup
- Hardware: Raspberry Pi (RPI 5 recommended) with camera module.
- Software:
  1. Install Raspberry Pi OS.
  2. Clone the repository.
  3. Run the provided bash setup script (TBD).

#### Web Server Setup
- Environment: Linux server
- Components:
  - Python HTTP server (`server.py`)
  - Flask API (`api.py`)
  - Video transfer script (`videos/server.py`)
- Setup Steps:
  1. Clone the repository and navigate to the `Web-Server` directory.
  2. Follow instructions to set up MariaDB in Docker:  
     [HackerNoon Guide](https://hackernoon.com/getting-started-with-mariadb-using-docker-python-and-flask-pa1i3ya3)
  3. Configure database credentials in `api.py`.
  4. Start services with:
     ```
     python3 server.py
     python3 api.py
     python3 videos/server.py
     ```
  5. Access the website via `localhost`.

#### Hosting Configuration
- Determine your public IP (e.g., via "What is my IP" websites).
- Open the necessary ports on your router:
  - Port 8000: HTTP server
  - Port 80: nginx
  - Port 6000: Flask API
  - Port 5000: File transfer
- Install and configure nginx for reverse proxying.
- Adjust firewall or SELinux settings based on your distribution.

#### Video Transfer
- Flask-based script (`videos/server.py`) sends RPI video files to the server.
- Videos become viewable on the video page after user login.

## Prerequisites

### User Requirements
- Website account (connected to MariaDB container)
- Power supply for the camera box

### Required Packages

#### Web Server
- MariaDB with C-Connector
- Docker
- nginx
- Python3 with the following packages:
  - flask  
  - moviepy.editor  
  - http.server  
  - urllib.parse  
  - json  
  - mariadb  

#### Raspberry Pi
- Python3 with the following packages:
  - ultralytics  
  - requests  
  - numpy  
  - opencv-python  

Note: Additional camera-specific packages may be required.

## Functionality
This system captures and analyzes video feeds to detect PPE violations, which are then uploaded to a secure website for review by authorized users. A login is required to view violation footage and manage devices.

## Known Issues
- User credential editing functionality is currently broken.
- Limited mobile responsiveness on the web interface.
- No unified script to run all server processes.
- Video storage is file-based; database integration is under consideration.

## Contributing
We welcome contributions:
1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push the branch: `git push origin my-new-feature`
5. Submit a pull request.

## Additional Documentation
**Initial Contributors:**  
- Conner Hanson: [@connerhanson](https://github.com/connerhanson)  
- Artur: [@theartur2000](https://github.com/theartur2000)  
- Moses

## License
Refer to `LICENSE.txt` for licensing details.  
Recommended license: [MIT License](https://choosealicense.com/licenses/mit/)
