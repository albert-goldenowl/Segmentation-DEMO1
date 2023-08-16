<b>Semantic Segmentation</b> is the task that model will assign class to each pixel of an image. It provides much more detailed information about the image. To step into the world of segmentation, let's get started with a simple (but not really) project that segment shapes.
This repo provides an end-to-end pipeline to develope semantic segmentation models.
### Requires:
Shape Semantic Segmentation requires:
<ul>
<li><b>TensorFlow</b> (for building models).</li>
<li><b>OpenCV</b> (for image processing).</li>
<li><b>Matplotlib</b> (for visualization)</li>
<li><b>Numpy</b> (for working with multi-dimensional arrays).</li>
<li><b>PyQt5</b> (for GUI).</li>
<li><b>onnx</b> (for working with onnx files).</li>
<li><b>onnxruntime</b> (for much faster inference).</li>
<li><b>tf2onnx</b> (for converting TensorFlow model file to onnx 
format). </li>
<li><b>albumentations</b> (for image augmentation)</li>
<li><b>moviepy (optional)</b> (for making video)</li>
<li><b>imageio (optional)</b> (for making gif)</li>
</ul>

### Install required libraries for who want to build from scratch
```
pip install tensorflow
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
### Install required libraries for who only want to use the released program

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
You can specify the path to the folder you want to store colleted images. If that folder is not exist, it will be created. Press S to save photo and Q to quit. My script will automatically name the photo you've taken. Note that it only captures inside the green-border rectangle.
### Annotate data
I used [CVAT](https://www.cvat.ai/) to annotating images.
### Build model and train
I recommend using [Kaggle](https://www.kaggle.com/) for training model. Kaggle provides free GPU use up to 30 hours/week. All you need to do is upload the notebook to Kaggle, and use it free powerful GPUs to train the model to save a lot of time. 
### Convert to onnx format
For much faster inference that can use in real-time applications, I recommend converting the .h5 format to .onnx format. It can speed up the inference time to 10x!!!
```

```
## For those who only want to use the released program
```
python mainUI.py
```
### Optional: export predictions through epochs to see the learning process of the model
#### Gif Generator
```
python gif_generator.py
```
#### MP4 Generator
```
python video_generator.py
```
