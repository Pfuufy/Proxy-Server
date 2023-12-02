#!/usr/bin/python3
#
# Helpful links
# https://docs.python.org/3/howto/urllib2.html
# https://docs.python.org/3.10/library/http.server.html#http.server.SimpleHTTPRequestHandler
# https://levelup.gitconnected.com/how-to-build-a-super-simple-http-proxy-in-python-in-just-17-lines-of-code-a1a09192be00

import socketserver
import http.server
import urllib.request
PORT = 8000

class Proxy(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    print("Get request")

    # Grab the URL that was specified as the end URL to be proxied
    url=self.path[1:]
    self.send_response(200)
    self.end_headers()

    try:
      with urllib.request.urlopen(url) as response:

      html = response.read()
      self.wfile.write(html)
    except:
      print("Error parsing output")


server_address = ('', PORT)
httpd = http.server.HTTPServer(server_address, Proxy)
httpd.serve_forever()