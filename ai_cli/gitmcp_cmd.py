import argparse
import json
import http.server
from pathlib import Path


def build_index():
    base = Path('.ai')
    result = {}
    if not base.exists():
        return result
    for p in base.rglob('*'):
        if p.is_file():
            result[str(p.relative_to(base))] = p.read_text()
    return result


class MCPHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ('/', '/context'):
            self.send_response(404)
            self.end_headers()
            return
        data = build_index()
        body = json.dumps(data).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(body)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Serve the .ai directory via a simple MCP endpoint'
    )
    parser.add_argument('--port', type=int, default=8000, help='Port to listen on')
    args = parser.parse_args(argv)
    server = http.server.ThreadingHTTPServer(('0.0.0.0', args.port), MCPHandler)
    print(f'Serving .ai on port {args.port}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
