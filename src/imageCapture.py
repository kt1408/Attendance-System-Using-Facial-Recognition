from PIL import ImageGrab
import numpy as np
import time
import datetime
import cv2

startTime = time.time()
now = datetime.datetime.now()
today = now.day
month = now.month

tempDelay = 15

while True:
    if time.time() > time.time() + tempDelay:
        break

delay = 30
close_time = time.time() + delay

while True:
    img = ImageGrab.grab(bbox=None)
    img.save('inputImage/new1.jpg')
    if time.time() > close_time:
        break
