from http.server import HTTPServer, BaseHTTPRequestHandler

# Import der Konfigurationsdatei (Installation mit "pip install pyyaml")
import yaml

# Einlesen der Konfigurationsdatei
with open("configuration.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'configuration[HELLO_WORLD]')


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()