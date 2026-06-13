import json
import os
from dataclasses import dataclass
from typing import List

@dataclass
class Service:
    name: str
    image: str
    ports: List[int]

def generate_docker_compose(services):
    docker_compose = {
        "version": "3",
        "services": {}
    }
    for service in services:
        docker_compose["services"][service.name] = {
            "image": service.image,
            "ports": [f"{port}:{port}" for port in service.ports]
        }
    return docker_compose

def generate_backend_code(resource_name):
    backend_code = f"""
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello from {resource_name}!')

def run_server():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting httpd on port 80...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
"""
    return backend_code

def generate_frontend_code(resource_name):
    frontend_code = f"""
print("Hello from {resource_name}!")
"""
    return frontend_code

def generate_auth0_config():
    auth0_config = {
        "domain": "example.auth0.com",
        "clientId": "example-client-id",
        "clientSecret": "example-client-secret"
    }
    return auth0_config

def main():
    services = [
        Service("postgres", "postgres:latest", [5432]),
        Service("backend", "node:latest", [80]),
        Service("frontend", "node:latest", [3000]),
        Service("auth0", "auth0/auth0:latest", [80])
    ]
    docker_compose = generate_docker_compose(services)
    with open("docker-compose.yml", "w") as f:
        json.dump(docker_compose, f, indent=4)
    resource_name = "example"
    backend_code = generate_backend_code(resource_name)
    os.makedirs("backend", exist_ok=True)
    with open("backend/index.py", "w") as f:
        f.write(backend_code)
    frontend_code = generate_frontend_code(resource_name)
    os.makedirs("frontend", exist_ok=True)
    with open("frontend/index.py", "w") as f:
        f.write(frontend_code)
    auth0_config = generate_auth0_config()
    with open("auth0.json", "w") as f:
        json.dump(auth0_config, f, indent=4)

if __name__ == "__main__":
    main()
