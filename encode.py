from imutils import paths
import pickle
import face_recognition
import cv2
import os
import csv
from more_itertools import unique_everseen
import tkinter as tk
from mtcnn.mtcnn import MTCNN

mtcnnDetector = MTCNN()

root = tk.Tk()
#abs_path = "C:/Users/Vartika/OneDrive/Desktop/face_recog/"


def closeFunction():
    root.destroy()


imagePaths = list(paths.list_images("images"))

knownEncodings = []
knownNames = []
root.title("Encoding Faces")
root.configure(background='#232b30')
root.geometry('400x160')


label = tk.Label(root, text="Finishing...Please do not exit",
                 fg="white", bg="#009999", width=50, height=4).grid(row=0)
pl2 = tk.Label(root, text="hello", fg="white", bg="#009999",
               width=50, height=3).grid(row=1)
quitLabel = tk.Label(root, text="Exit", width=22, height=6,
                     fg='white', bg="#420b0b").grid(row=2, columnspan=2)

#print(len(imagePaths))


def encodeFaces():
    for (i, imagePath) in enumerate(imagePaths):
        #print("Entered Loop {} time\n".format(i))
        l2 = tk.Label(root, text=("Processing Images {} of {}".format(
            i+1, len(imagePaths))), fg="white", bg="#009999", height=3, width=50).grid(row=1)
        root.update_idletasks()
        combinedText = imagePath.split(os.path.sep)[-2]
        nameAndID = combinedText.split(" ")
        roll_no = nameAndID[0]
        name = nameAndID[1]
        # Loading input image and converting to RGB from BGR
        image = cv2.imread(imagePath)
        scale_factor = 80
        width = int(image.shape[1]*scale_factor/100)
        height = int(image.shape[0]*scale_factor/100)
        dim = (width, height)

        # resizing
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        rgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detecting the boundaries of the faces present in image
        faceBoundaries = mtcnnDetector.detect_faces(rgbImage)
        #pseudo = face_recognition.face_locations(rgbImage, model="hog")
        #boxes = face_recognition.face_locations(rgbImage, model="hog")
        new_list = []
        for result in faceBoundaries:
            x, y, w, h = result['box']
            inTuple = (y, x+w, y+h, x)
            new_list.append(inTuple)
        # print(new_list)

        faceEncodings = face_recognition.face_encodings(rgbImage, new_list)

        # Now assigning the name & ID to each encodings
        for encoding in faceEncodings:
            knownEncodings.append(encoding)
            knownNames.append(combinedText)
        row = [roll_no, name]
        with open('data2.csv', 'a+', newline="") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

        csvFile.close()

        # Adding the facial encodings and name to the disk
    data = {"encodings": knownEncodings, "names": knownNames}
    encodingsFile = open("encodings.pickle", "wb")
    encodingsFile.write(pickle.dumps(data))
    encodingsFile.close()
    with open('data2.csv', 'r') as f1, open('data.csv', 'w', newline="") as out_file:
        write = csv.writer(out_file)
        write.writerow(['Roll No', 'Name'])
        out_file.writelines(unique_everseen(f1))
    os.remove('data2.csv')
    msg = tk.Label(root, text="Task Done", fg="white",
                bg="Green", width=60, height=4).grid(row=0)
    quitWindow = tk.Button(root, text="Exit", command=closeFunction, width=20,
                        height=3, fg="white", bg="#631f1f").grid(row=2, columnspan=2)

    # make encodings for each face in the image
    #encodings = face_recognition.face_encodings(rgbImage,faceBoundaries)


root.after(100, encodeFaces)
root.resizable(False, False)
root.mainloop()
