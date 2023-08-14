import cv2
import os
from config import frameshape
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import pydensecrf.densecrf as dcrf
from pydensecrf.utils import unary_from_softmax
import onnxruntime as ort


frame_shape = frameshape
target_shape = (256, 256, 3)
half_width = target_shape[0] // 2
half_height = target_shape[1] // 2
x0 = frame_shape[0] // 2 - half_width
y0 = frame_shape[1] // 2 - half_height
x1 = frame_shape[0] // 2 + half_width
y1 = frame_shape[1] // 2 + half_height


ort_session = ort.InferenceSession('model.onnx')
input_name = ort_session.get_inputs()[0].name
output_name = ort_session.get_outputs()[0].name
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
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
background = -1
crf = -1
prev_time = 0 
new_time = 0
while True:
    ret, frame = cam.read()
    sample_window = frame[y0:y0+target_shape[1], x0:x0+target_shape[0]].copy()

    input_to_model = cv2.cvtColor(sample_window, cv2.COLOR_BGR2RGB)
    input_to_model = input_to_model.astype(np.float32) / 255.0
    input_to_model = np.expand_dims(input_to_model, axis=0)
    y_pred = ort_session.run([output_name], {input_name: input_to_model})
    res = np.argmax(y_pred[0][0], axis=-1)
    mask_output = create_img(res)
    if crf == 1:
        d = dcrf.DenseCRF2D(256, 256, 5)
        f = y_pred[0][0].transpose((2, 0, 1)).reshape(5, -1)
        unary = unary_from_softmax(f)
        unary = np.ascontiguousarray(unary)
        im_rgb = np.ascontiguousarray(cv2.cvtColor(sample_window, cv2.COLOR_BGR2RGB))
        d.setUnaryEnergy(unary)
        d.addPairwiseGaussian(sxy=(5, 5), compat=3, kernel=dcrf.DIAG_KERNEL, normalization=dcrf.NORMALIZE_SYMMETRIC)
        d.addPairwiseBilateral(sxy=(5,5), srgb=(13, 13, 13), rgbim=im_rgb, compat=10, kernel=dcrf.DIAG_KERNEL, normalization=dcrf.NORMALIZE_SYMMETRIC)
        Q = d.inference(5)
        res = np.argmax(Q, axis=0).reshape((256, 256))
        mask_output = create_img(res)
        cv2.putText(frame, 'CRF On', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
    else:
        cv2.putText(frame, 'CRF Off', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

    cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
    if background == -1:
        cv2.putText(frame, 'Black mode', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        
    else:
        cv2.putText(frame, 'Background mode', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        mask_output = create_img_bg(sample_window, res)
    frame[y0:y0+target_shape[1], x0:x0+target_shape[0]] = mask_output
    frame = cv2.flip(frame, 1)
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



        
        