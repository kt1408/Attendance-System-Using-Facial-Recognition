from PIL import ImageGrab
import numpy as np
import time
import datetime
import cv2
from PIL import Image

now = datetime.datetime.now()
# today = now.day
# month = now.month

tempDelay = 5

startTime = time.time()

# print("Delay started")
while True:
    if time.time()>startTime + tempDelay:
        break


# print("actual starting")
delay = 20
close_time = time.time() + delay
imgCount = 0
while True:
    img = ImageGrab.grab(bbox=None)
    img.save("inputImage/" + "captured_" + str(imgCount) + ".jpg")
    imgCount+=1
    if time.time() > close_time:
        break


# print("process finished")

counter = 0



