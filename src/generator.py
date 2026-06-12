import json
import os
from typing import Dict


def _write_json(path: str, data: Dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def generate_scaffold(output_dir: str, resource: str = "Item") -> None:
    """
    Generate a minimal SaaS scaffold with:
    - docker-compose.yml (Postgres, Node/Express backend, React frontend)
    - Backend: Express server with CRUD endpoints for the given resource
    - Frontend: placeholder React app
    - Auth0 environment variables placeholders
    """
    # docker-compose.yml
    compose = {
        "version": "3.8",
        "services": {
            "postgres": {
                "image": "postgres:15-alpine",
                "environment": {
                    "POSTGRES_USER": "saas",
                    "POSTGRES_PASSWORD": "saas",
                    "POSTGRES_DB": "saasdb",
                },
                "ports": ["5432:5432"],
                "healthcheck": {
                    "test": ["CMD", "pg_isready", "-U", "saas"],
                    "interval": "10s",
                    "timeout": "5s",
                    "retries": 5,
                },
            },
            "backend": {
                "build": "./backend",
                "ports": ["5000:5000"],
                "environment": {
                    "DATABASE_URL": "postgresql://saas:saas@postgres:5432/saasdb",
                    "AUTH0_DOMAIN": "${AUTH0_DOMAIN}",
                    "AUTH0_CLIENT_ID": "${AUTH0_CLIENT_ID}",
                    "AUTH0_CLIENT_SECRET": "${AUTH0_CLIENT_SECRET}",
                },
                "depends_on": {
                    "postgres": {"condition": "service_healthy"},
                },
            },
            "frontend": {
                "build": "./frontend",
                "ports": ["3000:3000"],
                "environment": {
                    "REACT_APP_AUTH0_DOMAIN": "${AUTH0_DOMAIN}",
                    "REACT_APP_AUTH0_CLIENT_ID": "${AUTH0_CLIENT_ID}",
                },
                "depends_on": ["backend"],
            },
        },
    }

    _write_json(os.path.join(output_dir, "docker-compose.yml"), compose)

    # Backend
    backend_dir = os.path.join(output_dir, "backend")
    backend_pkg = {
        "name": "saas-backend",
        "version": "1.0.0",
        "main": "server.js",
        "license": "MIT",
        "dependencies": {"express": "^4.18.2", "pg": "^8.11.0"},
        "scripts": {"start": "node server.js"},
    }
    _write_json(os.path.join(backend_dir, "package.json"), backend_pkg)

    # Use PascalCase for resource name in routes
    resource_lower = resource.lower()
    resource_plural = f"{resource_lower}s"
    server_js = f"""const express = require('express');
const {{ Pool }} = require('pg');

const app = express();
app.use(express.json());

const pool = new Pool({{
  connectionString: process.env.DATABASE_URL,
}});

// Initialize table (runs once)
async function initDB() {{
  const client = await pool.connect();
  try {{
    await client.query(`CREATE TABLE IF NOT EXISTS {resource_plural} (
      id SERIAL PRIMARY KEY,
      name TEXT NOT NULL,
      description TEXT
    )`);
  }} finally {{
    client.release();
  }}
}}
initDB();

// CRUD endpoints for {resource}
app.get('/api/{resource_plural}', async (req, res) => {{
  const {{ rows }} = await pool.query(`SELECT * FROM {resource_plural} ORDER BY id`);
  res.json(rows);
}});

app.post('/api/{resource_plural}', async (req, res) => {{
  const {{ name, description }} = req.body;
  const {{ rows }} = await pool.query(
    `INSERT INTO {resource_plural} (name, description) VALUES ($1, $2) RETURNING *`,
    [name, description]
  ));
  res.status(201).json(rows[0]);
}});

app.put('/api/{resource_plural}/:id', async (req, res) => {{
  const {{ id }} = req.params;
  const {{ name, description }} = req.body;
  const {{ rows }} = await pool.query(
    `UPDATE {resource_plural} SET name = $1, description = $2 WHERE id = $3 RETURNING *`,
    [name, description, id]
  ));
  if (rows.length === 0) return res.sendStatus(404);
  res.json(rows[0]);
}});

app.delete('/api/{resource_plural}/:id', async (req, res) => {{
  const {{ id }} = req.params;
  const {{ rowCount }} = await pool.query(
    `DELETE FROM {resource_plural} WHERE id = $1`,
    [id]
  ));
  if (rowCount === 0) return res.sendStatus(404);
  res.sendStatus(204);
}});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Backend listening on {{PORT}}`));
"""
    os.makedirs(backend_dir, exist_ok=True)
    with open(os.path.join(backend_dir, "server.js"), "w", encoding="utf-8") as f:
        f.write(server_js)

    # Frontend (minimal React placeholder)
    frontend_dir = os.path.join(output_dir, "frontend")
    frontend_pkg = {
        "name": "saas-frontend",
        "version": "0.1.0",
        "private": True,
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "react-scripts": "5.0.1",
        },
        "scripts": {
            "start": "react-scripts start",
            "build": "react-scripts build",
            "test": "react-scripts test",
            "eject": "react-scripts eject",
        },
        "browserslist": {
            "production": [">0.2%", "not dead", "not op_mini all"],
            "development": [
                "last 1 chrome version",
                "last 1 firefox version",
                "last 1 safari version",
            ],
        },
    }
    _write_json(os.path.join(frontend_dir, "package.json"), frontend_pkg)

    # public/index.html
    public_dir = os.path.join(frontend_dir, "public")
    os.makedirs(public_dir, exist_ok=True)
    with open(os.path.join(public_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SaaS App</title>
</head>
<body>
    <noscript>You need JavaScript to run this app.</noscript>
    <div id="root"></div>
</body>
</html>
""")

    # src/index.js
    src_dir = os.path.join(frontend_dir, "src")
    os.makedirs(src_dir, exist_ok=True)
    with open(os.path.join(src_dir, "index.js"), "w", encoding="utf-8") as f:
        f.write("""import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  return (
    <div>
      <h1>SaaS Starter</h1>
      <p>Edit src/index.js and save to reload.</p>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
""")

    # .env.example (optional)
    with open(os.path.join(output_dir, ".env.example"), "w", encoding="utf-8") as f:
        f.write("""# Auth0 configuration
AUTH0_DOMAIN=your-tenant.auth0.com
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
""")

