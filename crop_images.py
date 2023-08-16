import os
import cv2
import numpy as np
images = []
save_dir = 'cropped_images'
if os.path.exists(save_dir) == False:
    os.mkdir(save_dir)
imgs_path = [os.path.join('gif_material',i) for i in os.listdir('gif_material')]

imgs_path = sorted(imgs_path, key=lambda x: int(x.split('Epoch')[1].split('.')[0]))
for img in imgs_path:
    name = int(img.split('Epoch')[1].split('.')[0])
    images = cv2.imread(img)
    img = images[134:361, 50:461, :]
    filename = save_dir + f'/Epoch{name}.png'
    cv2.imwrite(filename, img)

    

