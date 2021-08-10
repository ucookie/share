# file: main1.py
import web

urls = (
    "/healthz", "healthz",
    "/classify", "classify")

class healthz:
    def GET(self):
        return 'ok'

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8888)
