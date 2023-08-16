import tf2onnx
import tensorflow as tf
import onnx
# Specify the path of the input model
model = tf.keras.models.load_model('model.h5', compile=False)
onnx_model, _ = tf2onnx.convert.from_keras(model)
# Specify the path of the output onnx model (2nd parameter)
onnx.save(onnx_model, 'model_test.onnx')
print('Convert model to onnx successfully!')
