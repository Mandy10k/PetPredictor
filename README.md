# PetPredictor - Cat/Dog Image Classifier

![PetPredictor Logo](/project_directory/static/images/pP_logo.png)

PetPredictor is a web-based application that uses a trained convolutional neural network (CNN) to classify uploaded images as either a cat or a dog. The project is built using Flask for the backend and incorporates HTML, CSS, and JavaScript for the frontend. This README provides an overview of the project, instructions for use, and details on how to set up and run the application.

## Features

- Image classification as cat or dog.
- Simple and intuitive user interface.
- Responsive design for a seamless experience on various devices.

## How to Use

1. **Visit the Website:**
   - Open your web browser and navigate to the [PetPredictor](https://mandy10k.github.io/PetPredictor/).

2. **Upload an Image:**
   - Click on the "Choose File" button to select an image for classification.

3. **Supported Image Formats:**
   - PetPredictor supports common image formats, including JPG, JPEG, PNG, BMP, and WEBP.

4. **Upload and Predict:**
   - Click the "Upload and Predict" button to submit the image for classification.

5. **View Result:**
   - The prediction result will be displayed on the right side of the page.

6. **Interpret Result:**
   - Interpret the result to determine whether the image is classified as a cat or a dog.

## Setup and Installation

To run the PetPredictor application locally, follow these steps:

```bash
git clone https://github.com/your-username/PetPredictor.git
cd PetPredictor
pip install -r requirements.txt
python app.py
```
Make sure to replace the placeholder URLs, paths, and project-specific details with your actual information.

## Application Access

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.
<p align = "center">
 <img src="/Users/Mandy/GitHub/PetPredictor/project_directory/static/images/deployed.png" alt="DCGAN" width="60%">
</p>
## Folder Structure

- `static/`: Contains static files such as images and styles.
- `templates/`: Contains HTML templates for the frontend.
- `model/`: Contains the trained CNN model.
- `app.py`: Flask application script.
- `requirements.txt`: List of Python dependencies.

## Contributing

If you'd like to contribute to PetPredictor, please follow the [Contribution Guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors).

## License

This project is licensed under the MIT License.

Feel free to reach out if you have any questions or feedback!



