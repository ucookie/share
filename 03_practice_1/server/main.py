import web
from io import BufferedRandom

urls = (
    "/healthz", "healthz",
    "/classify", "classify")

class healthz:
    def GET(self):
        return 'ok'
class classify:
    def POST(self):
        # web.header('Content-Type', 'text/plain')
        form = web.input(image={})
        print(form['image'].filename, type(form['image'].file))
        img_byte = BufferedRandom.read(form['image'].file)
        with open('image.jpg', 'wb') as f:
            f.write(img_byte)
        return 'ok'

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8888)
