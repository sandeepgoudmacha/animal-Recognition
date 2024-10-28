from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf
from PIL import Image

app = Flask(__name__)

# Load the saved model
# from tensorflow.keras.models import load_model

# Load and re-save the model locally with the latest TensorFlow/Keras
model = load_model("animal_recognition_model.h5")
model.save("animal_recognition_model_compatible.h5")

# Class names based on the dataset
class_names = ['butterfly', 'cat', 'cow', 'dog', 'elephant', 'goat', 'hen', 'horse', 'spider', 'squirrel']

def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet.preprocess_input(img_array)
    return img_array

# Home route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    img = Image.open(file.stream)
    processed_image = preprocess_image(img)

    # Make prediction
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions, axis=1)[0]
    animal_name = class_names[predicted_class]

    return jsonify({"animal_name": animal_name})

if __name__ == '__main__':
    app.run(debug=True)
