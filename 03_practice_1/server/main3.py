# file: main3.py
import io
import web

import numpy as np
from PIL import Image
from tensorflow import keras

urls = (
    "/healthz", "healthz",
    "/classify", "classify")

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
model = keras.models.load_model('data/fashion.h5')
probability_model = keras.Sequential([model,keras.layers.Softmax()])

class healthz:
    def GET(self):
        return 'ok'

def do(img):
    iobuf = io.BytesIO(img)
    im = Image.open(iobuf)
    im_np = (np.expand_dims(np.array(im),0))
    predictions = probability_model.predict(im_np)
    idx = np.argmax(predictions[0])
    return class_names[idx]

class classify:
    def POST(self):
        form = web.input(image={})
        img_byte = io.BytesIO.read(form['image'].file)
        return do(img_byte)

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8888)
