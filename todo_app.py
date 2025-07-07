#!/usr/bin/env python3
"""
Simple Todo App using Python's built-in http.server.

Usage:
    python3 todo_app.py
Then open http://localhost:8000/ in your browser.
"""

import http.server
import json
from urllib.parse import parse_qs, urlparse

TASKS = []

class TodoHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(
                b"<h1>Todo App</h1><p>Add tasks with /add?task=Task.</p><p>List tasks with /list.</p>"
            )
        elif parsed.path == '/add':
            qs = parse_qs(parsed.query)
            task = qs.get('task', [''])[0]
            if task:
                TASKS.append(task)
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(f"Added task: {task}".encode())
            else:
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Missing task parameter.')
        elif parsed.path == '/list':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(TASKS).encode())
        else:
            self.send_response(404)
            self.end_headers()


def run(port: int = 8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, TodoHandler)
    print(f'Serving on http://localhost:{port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
