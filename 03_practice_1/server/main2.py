# file: main2.py
import io
import web

urls = (
    "/healthz", "healthz",
    "/classify", "classify")

class healthz:
    def GET(self):
        return 'ok'

class classify:
    def POST(self):
        form = web.input(image={})
        img_byte = io.BytesIO.read(form['image'].file)
        print(img_byte)
        return 'ok'

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8888)
