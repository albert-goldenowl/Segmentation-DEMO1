import imageio
import os
imgs_path = [os.path.join('cropped_images',i) for i in os.listdir('gif_material')]
images = []
imgs_path = sorted(imgs_path, key=lambda x: int(x.split('Epoch')[1].split('.')[0]))
for filename in imgs_path:
    images.append(imageio.imread(filename))
imageio.mimsave('mygif.gif', images)