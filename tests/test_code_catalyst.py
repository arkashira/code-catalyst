import pytest
from code_catalyst import generate_docker_compose, generate_backend_code, generate_frontend_code, generate_auth0_config, Service
import json
import os
import sys
sys.path.insert(0, '../src')

def test_generate_docker_compose():
    services = [
        {"name": "postgres", "image": "postgres:latest", "ports": [5432]},
        {"name": "backend", "image": "node:latest", "ports": [80]},
        {"name": "frontend", "image": "node:latest", "ports": [3000]},
        {"name": "auth0", "image": "auth0/auth0:latest", "ports": [80]}
    ]
    docker_compose = generate_docker_compose([Service(**service) for service in services])
    assert "version" in docker_compose
    assert "services" in docker_compose
    for service in services:
        assert service["name"] in docker_compose["services"]

def test_generate_backend_code():
    resource_name = "example"
    backend_code = generate_backend_code(resource_name)
    assert f"Hello from {resource_name}!" in backend_code

def test_generate_frontend_code():
    resource_name = "example"
    frontend_code = generate_frontend_code(resource_name)
    assert f"Hello from {resource_name}!" in frontend_code

def test_generate_auth0_config():
    auth0_config = generate_auth0_config()
    assert "domain" in auth0_config
    assert "clientId" in auth0_config
    assert "clientSecret" in auth0_config

def test_main():
    # Run the main function and check if the files are generated
    from code_catalyst import main
    main()
    assert os.path.exists("docker-compose.yml")
    assert os.path.exists("backend/index.py")
    assert os.path.exists("frontend/index.py")
    assert os.path.exists("auth0.json")
    # Remove the generated files
    os.remove("docker-compose.yml")
    os.remove("backend/index.py")
    os.remove("frontend/index.py")
    os.remove("auth0.json")
    os.rmdir("backend")
    os.rmdir("frontend")
