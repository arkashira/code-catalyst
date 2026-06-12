import json
import os
import tempfile

from generator import generate_scaffold


def test_generate_scaffold_creates_expected_files():
    with tempfile.TemporaryDirectory() as tmp:
        generate_scaffold(tmp, resource="Task")

        # docker-compose.yml exists and contains required services
        compose_path = os.path.join(tmp, "docker-compose.yml")
        assert os.path.isfile(compose_path)
        with open(compose_path, "r", encoding="utf-8") as f:
            compose = json.load(f)
        services = compose.get("services", {})
        assert "postgres" in services
        assert "backend" in services
        assert "frontend" in services
        # backend depends on postgres healthcheck
        assert services["backend"].get("depends_on", {}).get("postgres", {}).get("condition") == "service_healthy"

        # backend files
        backend_dir = os.path.join(tmp, "backend")
        assert os.path.isdir(backend_dir)
        assert os.path.isfile(os.path.join(backend_dir, "package.json"))
        assert os.path.isfile(os.path.join(backend_dir, "server.js"))
        with open(os.path.join(backend_dir, "package.json"), "r", encoding="utf-8") as f:
            backend_pkg = json.load(f)
        assert backend_pkg["name"] == "saas-backend"
        assert "express" in backend_pkg.get("dependencies", {})
        with open(os.path.join(backend_dir, "server.js"), "r", encoding="utf-8") as f:
            server_content = f.read()
        assert "const express = require('express');" in server_content
        assert "app.get('/api/tasks'" in server_content  # resource lowercased + s
        assert "app.post('/api/tasks'" in server_content
        assert "app.put('/api/tasks/:" in server_content
        assert "app.delete('/api/tasks/:" in server_content

        # frontend files
        frontend_dir = os.path.join(tmp, "frontend")
        assert os.path.isdir(frontend_dir)
        assert os.path.isfile(os.path.join(frontend_dir, "package.json"))
        with open(os.path.join(frontend_dir, "package.json"), "r", encoding="utf-8") as f:
            frontend_pkg = json.load(f)
        assert frontend_pkg["name"] == "saas-frontend"
        assert "react-scripts" in frontend_pkg.get("dependencies", {})
        assert os.path.isfile(os.path.join(frontend_dir, "public", "index.html"))
        assert os.path.isfile(os.path.join(frontend_dir, "src", "index.js"))

        # .env.example
        env_path = os.path.join(tmp, ".env.example")
        assert os.path.isfile(env_path)
        with open(env_path, "r", encoding="utf-8") as f:
            env_content = f.read()
        assert "AUTH0_DOMAIN" in env_content
        assert "AUTH0_CLIENT_ID" in env_content
        assert "AUTH0_CLIENT_SECRET" in env_content


def test_generate_scaffold_different_resource():
    with tempfile.TemporaryDirectory() as tmp:
        generate_scaffold(tmp, resource="Project")
        server_path = os.path.join(tmp, "backend", "server.js")
        with open(server_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "/api/projects" in content
        assert "app.get('/api/projects'" in content
        assert "app.post('/api/projects'" in content
        assert "app.put('/api/projects/:" in content
        assert "app.delete('/api/projects/:" in content
