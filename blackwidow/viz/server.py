import tornado.ioloop
import os.path

import tornado.web

from blackwidow import config

PARENT_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(PARENT_DIR, 'static')
HTML_FILE = os.path.join(STATIC_DIR, 'graph.html')

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render(HTML_FILE)

class DataHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(self.json_data)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/json", DataHandler)
], static_path=STATIC_DIR)

def serve(data, port=None):
    """
    Render graph visualization
    """
    DataHandler.json_data = data
    application.listen(port or config.PORT)
    print("Navigate to http://localhost:%d/ to view the package graph" % config.PORT)
    tornado.ioloop.IOLoop.current().start()
