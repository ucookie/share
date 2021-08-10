# file: run1.py
import io
import numpy as np
from PIL import Image
from tensorflow import keras

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
model = keras.models.load_model('data/fashion.h5')
probability_model = keras.Sequential([model,keras.layers.Softmax()])

if __name__ == "__main__":

    with open('test/0_9.jpg', 'rb') as f:
        img = f.read()
        iobuf = io.BytesIO(img)
        im = Image.open(iobuf)
        im_np = (np.expand_dims(np.array(im),0))
        predictions = probability_model.predict(im_np)
        idx = np.argmax(predictions[0])
        print("图片为:", class_names[idx])