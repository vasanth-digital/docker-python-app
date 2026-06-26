from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "message": "Production Docker Stack, new",
            "service": "api",
            "host": socket.gethostname(),
            "database": os.environ.get('DB_HOST', 'not set'),
            "status": "healthy"
        }
        self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        print(f"[API] {args[0]}")

print("[API] Starting on port 8000...")
HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()