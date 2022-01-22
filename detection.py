import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def run_detection(picture):
    yolo = cv2.dnn.readNet('./model_data/yolov4.weights',
                           './model_data/yolov4.cfg')
    yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    yolo.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    with open("./model_data/coco.names", 'r') as file:
        classes = file.read().splitlines()

    img = cv2.imread('./pictures/'+str(picture))

    width = img.shape[1]
    height = img.shape[0]

    blob = cv2.dnn.blobFromImage(img, 1/255, (320, 320), (0, 0, 0),
                                 swapRB=True, crop=False)

    yolo.setInput(blob)
    output_layers_names = yolo.getUnconnectedOutLayersNames()
    layeroutput = yolo.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []
    start_time = datetime.now()

    for out in layeroutput:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    people = 0
    for i in indices.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_id])
        conf = str(round(confidences[i], 2))
        color = colors[i]
        if class_ids[i] == 0:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, label+" "+conf, (x, y+20), font, 2, color, 2)
            people += 1

    end_time = datetime.now()
    time = end_time-start_time

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title('Liczba wykrytych osób: '+str(people)+', czas: '+str(
        time.total_seconds())+'s')
    plt.show()
