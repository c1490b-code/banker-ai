from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from banker_ai.accounts.service import list_accounts
from banker_ai.transactions.service import list_transactions
from banker_ai.ai.agent import agent


class Handler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_json({
                "name": "Banker AI",
                "version": "0.1.0",
                "status": "online",
            })

        elif self.path == "/accounts":
            self.send_json({"accounts": list_accounts()})

        elif self.path == "/transactions":
            self.send_json({"transactions": list_transactions()})

        else:
            self.send_json({"error": "Not found"}, 404)

    def do_POST(self):
        if self.path != "/ai":
            self.send_json({"error": "Not found"}, 404)
            return

        length = int(self.headers.get("Content-Length", 0))
        payload = json.loads(self.rfile.read(length))

        message = payload.get("message", "")
        intent = agent.understand(message)

        self.send_json({
            "assistant": "Banker AI",
            "intent": intent,
            "message": message,
        })


def run(host="0.0.0.0", port=None):
    import os

    if port is None:
        port = int(os.environ.get("PORT", "8080"))

    print(f"Banker AI listening on http://{host}:{port}")
    HTTPServer((host, port), Handler).serve_forever()
