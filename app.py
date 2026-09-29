from http.server import BaseHTTPRequestHandler, HTTPServer
from suma import suma

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(f"Hola DevOps! 2 + 3 = {suma(2, 3)}\n".encode())

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 3000), Handler).serve_forever()