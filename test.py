import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('gif_material/Epoch1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (640, 480))
plt.imshow(img)
plt.show()
