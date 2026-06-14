import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class ProjectBlueprint:
    name: str
    target_users: str
    core_features: list
    validation_evidence: str

def generate_project_skeleton(blueprint: ProjectBlueprint) -> Dict:
    return {
        "folder_structure": {
            "name": blueprint.name,
            "src": {
                "main.py": "",
                "auth.py": "",
                "database.py": ""
            },
            "tests": {
                "test_main.py": "",
                "test_auth.py": "",
                "test_database.py": ""
            }
        },
        "README": f"# {blueprint.name}\n\nTarget Users: {blueprint.target_users}\n\nCore Features: {', '.join(blueprint.core_features)}\n\nValidation Evidence: {blueprint.validation_evidence}",
        "tech_stack": ["Python", "JSON"],
        "basic_auth_module": {
            "username": "admin",
            "password": "password"
        },
        "sample_database_schema": {
            "users": {
                "id": "int",
                "name": "str",
                "email": "str"
            }
        }
    }

def upload_json(json_data: str) -> ProjectBlueprint:
    data = json.loads(json_data)
    return ProjectBlueprint(
        name=data["name"],
        target_users=data["target_users"],
        core_features=data["core_features"],
        validation_evidence=data["validation_evidence"]
    )

def fill_form(name: str, target_users: str, core_features: list, validation_evidence: str) -> ProjectBlueprint:
    return ProjectBlueprint(
        name=name,
        target_users=target_users,
        core_features=core_features,
        validation_evidence=validation_evidence
    )
