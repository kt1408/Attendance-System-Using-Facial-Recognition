from tkinter import *
import os
from tkinter import filedialog
import pandas as pd

abs_path = "C:/Users/Vartika/OneDrive/Desktop/face_recog/myvenvpy/src"
root = Tk()

root.configure(background="black")


def function1():
    os.system(
        'python C:/Users/Vartika/OneDrive/Desktop/face_recog/myvenvpy/src/encode.py')


def function2():
    os.system('python ./face_recognition.py')


def function3():
    os.startfile(os.getcwd() + "/Readme.doc")


def function4():
    root.destroy()


def function5():
    root.destroy()
    os.system(
        'python C:/Users/Vartika/OneDrive/Desktop/face_recog/myvenvpy/src/addStudent.py')


def function6():
    root.destroy()
    # os.system('python ./firstpage.py')


def total():
    os.system('python ./totalatt.py')


def option():
    root.destroy()
    global root1
    root1 = Tk()
    root1.configure(background="black")
    root1.title("Smart Attendance system")
    Label(root1, text="")


root.title("AUTO ATTENDANCE SYSTEM")
Label(root, text="AUTO ATTENDANCE SYSTEM", font=("castellar", 20), fg="white", bg="#009999",
      height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Train", font=("arial", 20), bg="#0b4233", fg='white',
       command=function1).grid(row=6, columnspan=2, sticky=W+E+N+S, padx=5, pady=5)
# Button(root,text="Take Attendance(Image)",font=("arial",20),bg="#0b4233",fg='white',command=function2).grid(row=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root, text="Take Attendance", font=("arial", 20), bg="#0b4233", fg='white',
       command=function3).grid(row=3, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Show attendance", font=('arial', 20), bg="#0b4233", fg="white",
       command=option).grid(row=5, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Help", font=('arial', 20), bg="#0b4233", fg="white",
       command=function5).grid(row=9, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
# Button(root,text="Add",font=('arial',20),bg="#0b4233",fg="white",command=function7).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root, text="Exit", font=('arial', 20), bg="#420b0b", fg="white",
       command=function6).grid(row=10, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
