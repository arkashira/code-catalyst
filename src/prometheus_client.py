import http.server
import json
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class Metric:
    name: str
    value: float

class PrometheusClient:
    def __init__(self):
        self.metrics = {}

    def register_metric(self, metric):
        self.metrics[metric.name] = metric.value

    def get_metrics(self):
        metrics = []
        for name, value in self.metrics.items():
            metrics.append(f"{name} {value}")
        return metrics

    def handle_request(self, request):
        parsed_url = urlparse(request.path)
        if parsed_url.path == "/metrics":
            metrics = self.get_metrics()
            return "\n".join(metrics)
        else:
            return "404 Not Found"

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        client = PrometheusClient()
        response = client.handle_request(self)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode())

def run_server():
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
