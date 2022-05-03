from tkinter import *
import os
from tkinter import filedialog
import pandas as pd

abs_path = "C:/Users/Vartika/OneDrive/Desktop/face_recog/myvenvpy/src"
root = Tk()

root.configure(background="black")


def trainModel():
    os.system('python encode.py')

def takeAttendance():
    os.system('python imageCapture.py')
    os.system('python recognizeFaces.py')    


def addData():
    root.destroy()
    os.system('python addStudent.py')




def function4():
    root.destroy()


def onlyImage():
    root.destroy()
    os.system(
        'python imageCapture.py')

def backFunction():
    root1.destroy()
    os.system('python ./main.py')


def closeFunction():
    root.destroy()
    


def showAttendance():
    file_path  = filedialog.askopenfilename(initialdir =os.getcwd() + "/Attendance")
    if file_path:
        os.startfile(file_path)

def showTotalAttendance():
    os.system('python ./totalAttendance.py')        


def attendance():
    root.destroy()
    global root1
    root1 = Tk()
    root1.configure(background="black")
    root1.title("Smart Attendance system")
    Label(root1, text="AUTO ATTENDANCE SYSTEM",font=("castellar",20),fg="white",bg="#0099ff",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
    Button(root1,text="Daily attendance",font=("arial",20),bg="#cc0066",fg='white',command=showAttendance).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
    Button(root1,text="Total attendance",font=("arial",20),bg="#cc0066",fg='white',command=showTotalAttendance).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
    Button(root1,text="Back",font=('arial',20),bg="#6600cc",fg="white",command=backFunction).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
    root1.mainloop()

root.title("AUTO ATTENDANCE SYSTEM")
Label(root, text="AUTO ATTENDANCE SYSTEM", font=("castellar", 20), fg="white", bg="#0099ff",
      height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Train", font=("arial", 20), bg="#cc0066", fg='white',
       command=trainModel).grid(row=6, columnspan=2, sticky=W+E+N+S, padx=5, pady=5)
#Button(root,text="Capture Image",font=("arial",20),bg="#0b4233",fg='white',command=total).grid(row=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root, text="Take Attendance", font=("arial", 20), bg="#cc0066", fg='white',
       command=takeAttendance).grid(row=3, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Show attendance", font=('arial', 20), bg="#cc0066", fg="white",
       command=attendance).grid(row=5, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Take Screenshot", font=('arial', 20), bg="#cc0066", fg="white",
       command=onlyImage).grid(row=9, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root,text="Add Student Data",font=('arial',20),bg="#cc0066",fg="white",command=addData).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root, text="Exit", font=('arial', 20), bg="#6600cc", fg="white",
       command=closeFunction).grid(row=10, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

root.resizable(False, False)
root.mainloop()

