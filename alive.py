from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"running")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8080)  # Listen on all interfaces, port 8000
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Serving on port 8080...")
    httpd.serve_forever()
