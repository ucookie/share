import numpy as np
from tensorflow import keras

from PIL import Image

if __name__ == "__main__":
    model = keras.models.load_model('../data/fashion.h5')
    probability_model = keras.Sequential([model,keras.layers.Softmax()])

    im = Image.open("1_2.jpg")
    img = (np.expand_dims(np.array(im),0))
    predictions = probability_model.predict(img)
    print("结果:", np.argmax(predictions[0]))
