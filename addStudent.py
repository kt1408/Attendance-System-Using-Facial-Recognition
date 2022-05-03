import cv2
import os
import numpy as np
import pandas as pd
import face_recognition
from imutils.video import VideoStream
import tkinter as tk
from tkinter import Message, Text
from PIL import Image, ImageTk
import re
import glob
from pathlib import Path
from mtcnn.mtcnn import MTCNN

# abs_path = os.path.dirname(os.path.abspath(__file__))
# print("Hello\n",abs_path)

mtcnnDetector = MTCNN()

window = tk.Tk()
window.title("Smart attendance system")
abs_path = "C:/Users/Vartika/OneDrive/Desktop/face_recog/"


window.geometry('730x480')
window.configure(background='black')


message = tk.Label(window, text="Enter Your Data", fg="white", bg="#0099ff",
                   width=32, height=2, font=('times', 30, ' bold ')).grid(row=0)

lbl = tk.Label(window, text="Enter ID :", width=12, height=2,
               fg="white", bg="#cc0066", font=("arial", 16))
lbl.place(x=80, y=120)

txt = tk.Entry(window, width=20, fg="black", bg="white", font=("arial", 16))
txt.place(x=270, y=135)

lbl2 = tk.Label(window, text="Enter Name :", width=12, height=2,
                fg="white", bg="#cc0066", font=("arial", 16))
lbl2.place(x=80, y=200)

txt2 = tk.Entry(window, width=20, fg="black", bg="white", font=("arial", 16))
txt2.place(x=270, y=210)

lbl3 = tk.Label(window, text="Message : ", width=12, height=2,
                fg="white", bg="#cc0066", font=("arial", 16))
lbl3.place(x=80, y=290)

message = tk.Label(window, text="Enter Name , ID", width=20,
                   height=3, fg="white", bg="#cc0066", font=("arial", 16))
message.place(x=270, y=275)

lbl4 = tk.Label(window, text="Total Pictures :", fg="white",
                bg="#cc0066", font=("arial", 16))
lbl4.place(x=545, y=270)

entry = tk.Entry(window, fg="black", width=10,
                 bg="white", font=("arial", 16))
entry.place(x=545, y=315)
entry.insert(0, 20)


def function6():
    window.destroy()
    os.system('python ./main.py')


def functionClose():
    window.destroy()


def clear():
    txt.delete(0, 'end')
    res = "Cleared"
    message.configure(text=res, bg='#a7bfcf', fg='green')


def clear2():
    txt2.delete(0, 'end')
    res = "Cleared"
    message.configure(text=res, bg="#a7bfcf", fg='green')


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


#video_capture = cv2.VideoCapture(0)


def TakeImages():
    id = (txt.get())
    name = (txt2.get())
    value = int(entry.get())
    if(is_number(id) and name.isalpha()):
        os.chdir( 'images')
        dirname = id + " " + name
        if(os.path.isdir(dirname)):
            files = os.listdir(dirname)
            paths = [os.path.join(dirname, basename) for basename in files]
            latest_file = max(paths, key=os.path.getctime)
            print(latest_file)
            Num = re.split("[_.]", latest_file)[-2]
            sampleNum = int(Num)
        else:
            sampleNum = 0

        Path(dirname).mkdir(parents=True, exist_ok=True)
        os.chdir(dirname)
        vs = VideoStream(src=0).start()
        #vs = VideoStream(src=0, resolution=(920, 920)).start()
        v = sampleNum

        tot = 0
        while(True):
            frames = vs.read()
            frames = cv2.flip(frames, 1)
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            rgb = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
            faces = mtcnnDetector.detect_faces(rgb)
            for result in faces:
                x, y, w, h = result['box']
                left = x
                top = y
                right = x + w
                bottom = y + h
                res = "Taking Pictures {}/{}".format(tot+1, value)
                message.configure(text=res, bg="#a7bfcf", fg='green')
                window.update_idletasks()
                sampleNum = sampleNum+1
                tot += 1
                # saving the captured face in the dataset folder images
                cv2.imwrite(name + "_ID_"+id + '_sample_' + str(sampleNum) +
                            ".jpg", frames[top-60:bottom+40, left-60:right+60])
                cv2.rectangle(frames, (left, top),
                              (right, bottom), (0, 255, 0), 2)
                cv2.imshow('Taking photos',
                           frames[top-60:bottom+40, left-60:right+60])
                # incrementing sample number
                # display the frame
            #cv2.imshow('Taking photos',frame)
            # wait for 200 miliseconds
            if cv2.waitKey(200) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 21
            elif sampleNum > v+value-1:
                break
        cv2.destroyAllWindows()
        vs.stream.release()
        res = "Images Saved for ID : " + id + "\nName : " + name
        message.configure(text=res, fg='white', bg='green')
        os.chdir('..')
        os.chdir('..')
        #os.system('python ./encode_faces.py')

    else:
        if(is_number(id) == False):
            res = "Enter Numeric Id"
            message.configure(text=res, bg='#631f1f', fg='white')
        if(name.isalpha() == False):
            res = "Enter Alphabetical Name"
            message.configure(text=res, bg='#631f1f', fg='white')


clearButton = tk.Button(window, text="Clear", command=clear,
                        width=10, fg="white", bg="#cc0066", font=("arial", 16))
clearButton.place(x=545, y=123)
clearButton2 = tk.Button(window, text="Clear", command=clear2,
                         width=10, fg="white", bg="#cc0066", font=("arial", 16))
clearButton2.place(x=545, y=203)
takeImg = tk.Button(window, text="Add images", command=TakeImages,
                    width=12, height=2, fg="white", bg="#00cc00", font=("arial", 16))
takeImg.place(x=50, y=380)
quitWindow = tk.Button(window, text="Back", command=function6,
                       width=12, height=2, fg="white", bg="#3399ff", font=("arial", 16))
quitWindow.place(x=300, y=380)
quitWindow = tk.Button(window, text="Exit", command=functionClose,
                       width=12, height=2, fg="white", bg="#cc0000", font=("arial", 16))
quitWindow.place(x=550, y=380)

window.resizable(False, False)
window.mainloop()
