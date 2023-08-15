import cv2
import os
from config import frameshape
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time
import onnxruntime as ort


frame_shape = frameshape
target_shape = (256, 256, 3)
half_width = target_shape[0] // 2
half_height = target_shape[1] // 2
x0 = frame_shape[0] // 2 - half_width
y0 = frame_shape[1] // 2 - half_height
x1 = frame_shape[0] // 2 + half_width
y1 = frame_shape[1] // 2 + half_height

def create_img(mask_output):
    r = np.zeros((256, 256), dtype=np.uint8)
    g = np.zeros((256, 256), dtype=np.uint8)
    b = np.zeros((256, 256), dtype=np.uint8)
    r[mask_output == 1] = 250
    r[mask_output == 2] = 36
    r[mask_output == 3] = 42
    r[mask_output == 4] = 115

    g[mask_output == 1] = 50
    g[mask_output == 2] = 179
    g[mask_output == 3] = 125
    g[mask_output == 4] = 51

    b[mask_output == 1] = 83
    b[mask_output == 2] = 83
    b[mask_output == 3] = 209
    b[mask_output == 4] = 128

    output = np.stack([b, g, r], axis=-1)
    return output
def create_img_bg(roi, mask_output):
    b, g, r = cv2.split(roi)
    r[mask_output == 1] = 250
    r[mask_output == 2] = 36
    r[mask_output == 3] = 42
    r[mask_output == 4] = 115

    g[mask_output == 1] = 50
    g[mask_output == 2] = 179
    g[mask_output == 3] = 125
    g[mask_output == 4] = 51

    b[mask_output == 1] = 83
    b[mask_output == 2] = 83
    b[mask_output == 3] = 209
    b[mask_output == 4] = 128

    output = np.stack([b, g, r], axis=-1)
    return output

cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
background = -1
prev_time = 0 
new_time = 0
while True:
    ret, frame = cam.read()
    # frame = cv2.resize(frame, (1280, 720))
    # frame = cv2.flip(frame, 1)
    new_time = time.time()
    fps = str(int(1 / (new_time - prev_time)))
    cv2.putText(frame, str(int(fps)), (5, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)
    prev_time = new_time
    cv2.imshow('cam', frame)
    k = cv2.waitKey(1)
    if k == ord('c'):
        crf = -crf
    if k == ord('b'):
        background = -background
    if k == ord('q'):
        break



        
        