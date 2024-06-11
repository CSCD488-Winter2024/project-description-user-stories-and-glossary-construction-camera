#For automatic annotation
from ultralytics import YOLO
import os

# Load the YOLOv8 model
model = YOLO('yolov8m_custom.pt')

# Perform inference on an image
results = model('C:/Users/artur/Desktop/training data/test footage/test image', show=False, conf=0.3, iou=0.6)

# Extract bounding boxes, classes, names, and confidences
boxes = results[0].boxes.xywhn.tolist()
classes = results[0].boxes.cls.tolist()
#names = results[0].names
#confidences = results[0].boxes.conf.tolist()



path = "C:/Users/artur/Desktop/training data/test footage/test image"
dir_list = os.listdir(path)
fileLen = len(dir_list)

for i in range(fileLen):
    fileName = dir_list.pop(0)[:-5]
    fileDirectory = "C:/Users/artur/Desktop/training data/test footage/test weights/" + fileName + ".txt"

    print(fileDirectory)

    boxes = results[i].boxes.xywhn.tolist()
    classes = results[i].boxes.cls.tolist()
    length = len(boxes)


    f = open(fileDirectory, "w")

    for i in range(length):
        f.write(str(classes.pop())[:-2] + " " + str(boxes.pop())[1:-1].replace(',', '') + "\n")

    f.close()



# Iterate through the results
#for box, cls, conf in zip(boxes, classes, confidences):
#    x1, y1, x2, y2 = box
#    confidence = conf
#    detected_class = cls
#    name = names[int(cls)]
