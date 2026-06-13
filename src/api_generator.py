from dataclasses import dataclass
from typing import List, Dict
from src.data_model import Table, Column, DataModel
import json

@dataclass
class Endpoint:
    method: str
    path: str
    description: str

class ApiGenerator:
    def __init__(self, data_model: DataModel):
        self.data_model = data_model
        self.endpoints = []

    def generate_endpoints(self) -> List[Endpoint]:
        for table in self.data_model.get_tables():
            self.endpoints.append(Endpoint("GET", f"/{table.name}", f"Get all {table.name}"))
            self.endpoints.append(Endpoint("POST", f"/{table.name}", f"Create a new {table.name}"))
            self.endpoints.append(Endpoint("GET", f"/{table.name}/{{id}}", f"Get {table.name} by id"))
            self.endpoints.append(Endpoint("PUT", f"/{table.name}/{{id}}", f"Update {table.name} by id"))
            self.endpoints.append(Endpoint("DELETE", f"/{table.name}/{{id}}", f"Delete {table.name} by id"))
        return self.endpoints

    def generate_swagger(self) -> str:
        swagger = {
            "swagger": "2.0",
            "info": {
                "title": "API Documentation",
                "description": "API Documentation",
                "version": "1.0.0"
            },
            "paths": {}
        }
        for endpoint in self.endpoints:
            path = endpoint.path
            method = endpoint.method
            description = endpoint.description
            if path not in swagger["paths"]:
                swagger["paths"][path] = {}
            swagger["paths"][path][method.lower()] = {
                "summary": description,
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                }
            }
        return json.dumps(swagger, indent=4)
