"""
Simple server for loading d3 json files
Adapted from networkx example at:
    https://github.com/networkx/networkx/blob/master/examples/javascript/http_server.py
"""
import SimpleHTTPServer, BaseHTTPServer
import socket
import thread
import webbrowser
import os

def serve(directory, filename, port):
    base_url = "127.0.0.1"
    os.chdir(directory)
    httpd = StoppableHTTPServer(
        (base_url, port), 
        SimpleHTTPServer.SimpleHTTPRequestHandler
    )
    thread.start_new_thread(httpd.serve, ())
    webbrowser.open('http://%s:%s/%s' % (base_url, port, filename))
    raw_input("Press <RETURN> to stop server\n")
    httpd.stop()


class StoppableHTTPServer(BaseHTTPServer.HTTPServer):

    def server_bind(self):
        BaseHTTPServer.HTTPServer.server_bind(self)
        self.socket.settimeout(1)
        self.run = True

    def get_request(self):
        while self.run:
            try:
                sock, addr = self.socket.accept()
                sock.settimeout(None)
                return (sock, addr)
            except socket.timeout:
                pass

    def stop(self):
        self.run = False

    def serve(self):
        while self.run:
            self.handle_request()
