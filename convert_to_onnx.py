import tf2onnx
import tensorflow as tf
import onnx
model = tf.keras.models.load_model('model.h5', compile=False)
onnx_model, _ = tf2onnx.convert.from_keras(model)
onnx.save(onnx_model, 'model_test.onnx')
print('Convert model to onnx successfully!')
