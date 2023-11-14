import os
import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Loading the trained CNN model
model = load_model('model/second_cnnModel.h5') #change the directory path accordingly

def predict_image(file_path):
    img = image.load_img(file_path, target_size=(256, 256))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    result = model.predict(img)
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join('static/images', uploaded_file.filename)   #change the directory path accordingly
            uploaded_file.save(file_path)
            result = predict_image(file_path)
            prediction = 'Dog' if result > 0.5 else 'Cat'
            return render_template('index.html', prediction=prediction, image_path=file_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
