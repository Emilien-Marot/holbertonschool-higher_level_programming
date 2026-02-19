#!/usr/bin/env python3
import http.server
import json


class MyHTTPRequestHandler (http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        json_page = False
        response_code = 200
        if self.path == "/":
            response = "Hello, this is a simple API!"
        elif self.path == "/data":
            response = json.dumps({
                "name": "John",
                "age": 30,
                "city": "New York"})
            json_page = True
        elif self.path == "/info":
            response = json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"})
            json_page = True
        elif self.path == "/status":
            response = "OK"
        else:
            response = "404 Not Found"
            response_code = 404
        self.send_response(response_code)
        if json_page:
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", len(response))
        self.end_headers()
        self.wfile.write(response.encode('utf8'))


def run(server_class=http.server.HTTPServer,
        handler_class=MyHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


a = run()
