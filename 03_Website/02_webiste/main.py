#Import 
from http.server import HTTPServer, BaseHTTPRequestHandler

# Klasse Website mit Konstruktor und Methode start
class Website:
    def __init__(self):
        print("Website Klasse wird initialisiert")
        self.server = HTTPServer(("localhost", 8000), WebsiteHandler)

    def start(self):
        print("Server läuft auf http://localhost:8000")
        self.server.serve_forever()

# Händler was wird wiedergegeben
class WebsiteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
            <html>
                <body>
                    <h1>Login</h1>
                    <form method="post">
                        Username: <input type="text" name="username"><br>
                        Password: <input type="password" name="password"><br>
                        <input type="submit" value="Login">
                    </form>
                </body>
            </html>
        """)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = dict(x.split('=') for x in post_data.split('&'))
        
        username = params.get('username')
        password = params.get('password')
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        if username == "admin" and password == "password":
            self.wfile.write(b"<h1>Login successful</h1>")
        else:
            self.wfile.write(b"<h1>Login failed</h1>")

# Hauptfunktion
def main():
    try:
        print("Terminal Logging: Starte Website")
        gui = Website()
        gui.start()

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()