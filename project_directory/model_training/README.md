# Cat/Dog Image Classifier using Convolutional Neural Network (CNN)

This project implements a Cat/Dog image classifier using a Convolutional Neural Network (CNN) in TensorFlow and Keras. The classifier is trained on a dataset of cat and dog images and provides predictions on new images uploaded to the system.

## Features

- Image classification as cat or dog.
- Utilizes Convolutional Neural Network (CNN) architecture.
- Provides training and evaluation insights.
- Simple and intuitive interface for uploading and predicting images.

## Model Architecture

The initial model architecture consists of three convolutional layers with max-pooling, followed by dense layers for classification. The model is trained using the Adam optimizer and binary crossentropy loss.

## Overfitting Observation

The first model (`first_cnnModel.h5`) showed signs of overfitting, leading to reduced performance on validation data.

## Improved Model

To mitigate overfitting, an improved model is implemented with additional Batch Normalization and Dropout layers.

## Training and Evaluation

Both the initial and improved models are trained for 10 epochs, with training and validation accuracy/loss visualized using Matplotlib.

## Result Interpretation

The model predicts whether an image is a cat or a dog based on the training. The prediction result is displayed as "Model predicts image as Cat" or "Model predicts image as Dog."

## Save the Model

Both the initial and improved models are saved as `first_cnnModel.h5` and `second_cnnModel.h5`, respectively.

## Visualization

Training history, including accuracy and loss, is visualized using Matplotlib.

## Dependencies

- TensorFlow
- Keras
- Matplotlib
- OpenCV

## License
This project is licensed under the MIT License.
Feel free to reach out if you have any questions or feedback!