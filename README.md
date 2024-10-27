# Animal Recognition Project

## Overview
This project is an Animal Recognition web application that utilizes a trained machine learning model to identify various animals from uploaded images. The application is built using Flask and TensorFlow, making it easy to deploy and use.

## Features
- Upload an image of an animal.
- Get real-time predictions of the animal type.
- Supports multiple animal classes.

## Technologies Used
- **Flask**: A lightweight web framework for building the web application.
- **TensorFlow**: Used for building and training the machine learning model.
- **Keras**: High-level neural networks API, running on top of TensorFlow.
- **Pillow**: Library for image processing.
- **NumPy**: Library for numerical computations.
- **Git LFS**: For handling large files like datasets.

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/sandeepgoudmacha/animal-Recognition.git
   cd animal-Recognition
2. Create a virtual environment (optional but recommended):

    ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. Install the required packages:

     ```bash
       pip install -r requirements.txt
#### Usage
1. Run the Flask application:

    ```bash
     python app.py
2. Open your web browser and navigate to http://127.0.0.1:5000.

3. Upload an image of an animal to get a prediction.

### Model Training
The model was trained using a dataset of various animals. It utilizes the ResNet50 architecture and is fine-tuned for better performance. The model file is included in the repository as animal_recognition_model.h5.

### File Structure
graphql
.
├── animal_recognition_model.h5  # The trained model
├── app.py                       # The main Flask application
├── requirements.txt             # Python packages required
├── sample_img_of_animals/       # Sample images for testing
├── templates/                   # HTML templates for the web application
├── train_animal_recognition_model.py  # Script to train the model
└── .gitattributes                # Git LFS tracking file

### Contributing
Contributions are welcome! Please open an issue or submit a pull request.
