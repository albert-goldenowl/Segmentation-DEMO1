<b>Semantic Segmentation</b> is the task that model will assign class to each pixel of an image. It provides much more detailed information about the image. To step into the world of segmentation, let's get started with a simple (but not really) project that segment shapes.
This repo provides an end-to-end pipeline to develope semantic segmentation models.

![mygif](https://github.com/albert-goldenowl/Segmentation-DEMO1/assets/140538269/d422dc65-6526-442e-8cab-4ae64449b215)

### Requires:
Shape Semantic Segmentation requires:
<ul>
<li><b>TensorFlow</b> (for building models).</li>
<li><b>OpenCV</b> (for image processing).</li>
<li><b>Matplotlib</b> (for visualization).</li>
<li><b>Numpy</b> (for working with multi-dimensional arrays).</li>
<li><b>PyQt5</b> (for GUI).</li>
<li><b>onnx</b> (for working with onnx files).</li>
<li><b>onnxruntime</b> (for much faster inference).</li>
<li><b>tf2onnx</b> (for converting TensorFlow model file to onnx 
format). </li>
<li><b>albumentations</b> (for image augmentation).</li>
<li><b>moviepy (optional)</b> (for making video).</li>
<li><b>imageio (optional)</b> (for making gif).</li>
</ul>

### Install required libraries for those who want to build from scratch
```
pip install tensorflow==2.12.1
pip install opencv-python
pip install matplotlib
pip install numpy
pip install pyqt5
pip install onnx
pip install onnxruntime
pip install tf2onnx
pip install albumentations
pip install moviepy
pip install imageio
```

> :clipboard: **Note**: please install TensorFlow==2.12.1 (cause lastest TensorFlow has a conflict with tf2onnx).

### Install required libraries for those who only want to use the completed program with UI

```
pip install tensorflow
pip install opencv-python
pip install matplotlib
pip install numpy
pip install pyqt5
pip install onnxruntime
```

## For those who care about the pipeline
### Collect data
```
python collect_images.py
```
You can specify the path to the folder you want to store colleted images. If that folder is not exist, it will be created. Press S to take a photo and Q to quit. My script will automatically name the photo you've taken. Note that it only captures things inside the green-border rectangle.
### Annotate data
I used [CVAT](https://www.cvat.ai/) to annotating images. Please export annotations using *CamVid 1.0* format. The default mask's color of each shape is as follows:
<ul>
<li style='color:rgb(250, 50, 83)'>Square: rgb(250, 50, 83)</li>
<li style='color:rgb(36, 179, 83)'>Circle: rgb(36, 179, 83)</li>
<li style='color:rgb(42, 125, 209)'>Triangle: rgb(42, 125, 209)</li>
<li style='color:rgb(115, 51, 128)'>Star: rgb(115, 51, 128)</li>
</ul>

In case your masks have other colors, please change the attribute of shape's colors in class **Dataset** in ```model.ipynb```(cause the **Dataset** class base on the color of mask to create the one-hot encoding mask).

### Build model and train

I builded the model based on the UNet architecture, with Depthwise Convolution from MobileNet to reduce number of parameters and speed up the inference process.
```model.ipynb``` has all the helper functions, classes as well as model. I recommend using [Kaggle](https://www.kaggle.com/) for training model. Kaggle provides free GPU use up to 30 hours/week. All you need to do is upload the notebook to Kaggle, and use it free powerful GPUs to train the model to save a lot of time. 

You can download the model and zip file contains predictions through epochs after done running ```model.ipynb``` on Kaggle.

> :clipboard: **Note**: Please change all paths in ```model.ipynb``` to your current workspace.
### Convert to onnx format
For much faster inference that can use in real-time applications, I recommend converting the .h5 format to .onnx format. It can speed up the inference time to 10x!!!

Specify the path of the input TensorFlow model and the path of the output onnx model in ```convert_to_onnx.py```, then run the script. You should see the onnx model at the path you specified after that.

```
python convert_to_onnx.py
```

### Streaming
This will read your camera.
```
python mainUI.py
```
### Optional: export predictions through epochs to see the learning process of the model

When you're done running the notebook file on Kaggle. You can download the zip file contains the predictions through epochs. You should copy all the images and paste to *gif_material*. Then, crop the images to center then generate gif or mp4 on your choice. The input images default at folder *gif_material*. The cropped images will be placed at *cropped_images*. You can change the folders' path anytime.
### Crop images 
```
python crop_images.py
```
After cropping images, you can generate gif or mp4 file on your choice.
#### Gif Generator
```
python gif_generator.py
```
#### MP4 Generator
```
python video_generator.py
```
> :clipboard: **Note**: Check carefully the input path.
## For those who only want to use the completed program with UI
This will read your camera.
```
python mainUI.py
```
> :clipboard: **Note**: You can change the color of each shape.
