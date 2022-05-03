from email.mime import base
from mtcnn.mtcnn import MTCNN
import cv2
import numpy as np
import os
import csv

# Root path
abs_path = "C:/Users/Vartika/OneDrive/Desktop/face_recog/myvenvpy/"

# MTCNN setup
mtcnnDetector = MTCNN()


# DNN detector setup
modelFile = abs_path + "models/res10_300x300_ssd_iter_140000.caffemodel"
configFile = abs_path + "models/deploy.prototxt.txt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)


images = os.listdir('C:/Users/Vartika/OneDrive/Desktop/face_recog/inputImage')
new_list = []

# ok = True

for image in images:
    img = cv2.imread(os.path.join(
        'C:/Users/Vartika/OneDrive/Desktop/face_recog/inputImage', image))
    height, width = img.shape[:2]
    img1 = img.copy()
    img2 = img.copy()
    img3 = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # # detect faces in the image
    faces1 = mtcnnDetector.detect_faces(img_rgb)

    blob = cv2.dnn.blobFromImage(cv2.resize(
        img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    faces3 = net.forward()

    # for res in faces1:
    #     print(res['box'], "\n")

    # for res in faces3:
    #     print(res)
    cv2.imwrite("interImage.jpg", img)
    # MTCNN
    for result in faces1:
        x, y, w, h = result['box']
        x1, y1 = x + w, y + h
        cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
        new_list.append({x, y, x1, y1})
        # new_image = img[y:y1,x:x1]
        # cv2.imshow("Any",new_image)
    cv2.imwrite(abs_path + "check/" + str(h) + str(w) + "_new.jpg", img)
    new_list.append({"This is the separater...|"})
    # OPENCV DNN
    count = 0
    for i in range(faces3.shape[2]):
        confidence = faces3[0, 0, i, 2]
        if confidence > 0.5:
            box = faces3[0, 0, i, 3:7] * \
                np.array([width, height, width, height])
            (x, y, x1, y1) = box.astype("int")
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 2)
            count += 1
            new_list.append({x, y, x1, y1})

    cv2.imshow("mtcnn", img)

    cv2.imshow("dnn", img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# for obj in new_list:
#     print(obj, "\n")

fields = ['c1', 'c2', 'c3', 'c4']
filename = 'check.csv'

with open(filename, 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    writer.writerows(new_list)

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    firstRow = next(reader)
    for row in reader:
        print("{", row, "}", "\n")
