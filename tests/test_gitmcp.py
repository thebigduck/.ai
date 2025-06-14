import json
import os
import tempfile
import threading
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

import ai_cli.gitmcp_cmd as gitmcp


def test_gitmcp_serves_ai_directory():
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            # prepare .ai directory
            base = Path('.ai/1-context')
            base.mkdir(parents=True, exist_ok=True)
            context_file = base / 'project_context.md'
            context_file.write_text('hello')

            server = ThreadingHTTPServer(('127.0.0.1', 0), gitmcp.MCPHandler)
            port = server.server_address[1]
            t = threading.Thread(target=server.handle_request)
            t.start()
            try:
                with urllib.request.urlopen(f'http://127.0.0.1:{port}/context') as resp:
                    data = json.load(resp)
                assert '1-context/project_context.md' in data
                assert data['1-context/project_context.md'] == 'hello'
            finally:
                server.server_close()
                t.join()
        finally:
            os.chdir(cwd)
