import cv2
import os
import moviepy.video.io.ImageSequenceClip
fps = 10
imgs_path = [os.path.join('cropeed_images',i) for i in os.listdir('gif_material')]

imgs_path = sorted(imgs_path, key=lambda x: int(x.split('Epoch')[1].split('.')[0]))
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(imgs_path, fps=10)
clip.write_videofile('myvideo.mp4')