import numpy as np
import cv2
import time
import os
from datetime import datetime
from ultralytics import YOLO
import requests

# Function to upload a file to an HTTP server
def upload_to_server(filepath, server_url):
    try:
        with open(filepath, 'rb') as file:
            files = {'file': (os.path.basename(filepath), file, 'video/avi')}
            response = requests.post(server_url, files=files)
        if response.status_code == 200:
            print(f"File {filepath} successfully uploaded to server.")
        else:
            print(f"Failed to upload file {filepath} to server: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Failed to upload file {filepath} to server: {e}")

# Prompt the user to input parameters
print("Adjust the following parameters with two test videos, one with definite violations, and one without any violations.")
print("The program should correctly identify violations in the two control videos, then be applied to a real example.")
print("\nEnter error deviation in a decimal percentage (IDEAL = 0.5)")
deviation = float(input())

print("\nEnter total violation threshold (how lax the program will act towards total violations) in decimal (PER VIDEO)")
violationThreshold = float(input())

# Initialize YOLO model
model = YOLO("yolov8m_custom.pt")

# Define the codec and duration for recording
fourcc = cv2.VideoWriter_fourcc(*'XVID')
duration = 10  # Duration to record in seconds
server_url = "http://73.239.65.156:5000/upload"

# Function to create directories based on current date and time
def create_directories():
    now = datetime.now()
    base_dir = now.strftime('%B')
    day_dir = now.strftime('%d')
    hour_dir = now.strftime('%H')
    path = os.path.join(base_dir, day_dir, hour_dir)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# Function to process a single video file
def process_video(video_file):
    print(f"Processing video: {video_file}")
    start = time.time()

    # Run batched inference on the video
    results = model(video_file, save=False, show=False, conf=0.5, iou=0.5, vid_stride=15)

    totalImg = 0
    totalViolations = 0
    totalDetections = 0
    totalDetectionsClass0 = 0
    totalDetectionsClass1 = 0

    for r in results:
        totalImg += 1
        c0, c1 = (sum(int(cls) == i for cls in r.boxes.cls) for i in range(2))
        totalDetections += len(r.boxes.cls)
        totalDetectionsClass0 += c0
        totalDetectionsClass1 += c1
        print(f"Hat = {c0}\tPerson = {c1}")
        if len(r.boxes.cls) > 0 and c0 / float(len(r.boxes.cls)) < deviation:
            print("Possible violation!")
            totalViolations += 1

        print(f"Total for Tensor: {len(r.boxes.cls)}")

    if totalDetections > 0:
        hats_detection_percentage = (totalDetectionsClass0 / totalDetections) * 100
        people_detection_percentage = (totalDetectionsClass1 / totalDetections) * 100
        print(f"Hats: {hats_detection_percentage}%, People: {people_detection_percentage}%")

    if totalImg > 0:
        violations_percentage = (totalViolations / totalImg) * 100
        print(f"Violations detected in {violations_percentage}% of video and the violation threshold is {violationThreshold * 100}%")

        if (totalViolations / totalImg) > violationThreshold:
            print("=====HIGH LIKELYHOOD OF VIOLATION DETECTED IN VIDEO=====")
            upload_to_server(video_file, server_url)
        else:
            upload_to_server(video_file, server_url)
    else:
        print("No frames were processed in this video.")

    end = time.time()
    print(f"Time elapsed for video {video_file}: {end - start} seconds")

# Initialize video capture
device = 1
cap = cv2.VideoCapture(device)

# If capture failed to open, try again
if not cap.isOpened():
    cap.open(device)

while True:
    # Create directories and get the file path
    directory_path = create_directories()
    now = datetime.now()
    filename = now.strftime('%Y-%m-%d_%H-%M-%S') + '.avi'
    filepath = os.path.join(directory_path, filename)

    # Create VideoWriter object for the new video file
    out = cv2.VideoWriter(filepath, fourcc, 20.0, (640, 480))

    start_time = time.time()

    # Only attempt to read if it is opened
    if cap.isOpened():
        while True:
            re, img = cap.read()
            # Only display the image if it is not empty
            if re:
                cv2.imshow("video output", img)
                # Write the frame to the video file
                out.write(img)
            # If it is empty abort
            else:
                print("Error reading capture device")
                break

            # Break the loop if 'Esc' key is pressed
            k = cv2.waitKey(10) & 0xFF
            if k == 27:
                cap.release()
                out.release()
                cv2.destroyAllWindows()
                exit()

            # Break the loop after the specified duration
            if time.time() - start_time > duration:
                break

        out.release()  # Release the current video file
        process_video(filepath)  # Process the video immediately after recording
    else:
        print("Failed to open capture device")
        break

cap.release()
cv2.destroyAllWindows()
