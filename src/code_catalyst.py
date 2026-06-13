#!/usr/bin/env python3
"""
code_catalyst: Generate a project skeleton from a product brief.
"""

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Any


@dataclass
class ProductBrief:
    product_name: str
    target_users: str
    core_features: List[str]
    validation_evidence: str
    tech_stack: List[str] = field(default_factory=lambda: ["Python", "Flask", "SQLite"])

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ProductBrief":
        return ProductBrief(
            product_name=data["product_name"],
            target_users=data["target_users"],
            core_features=data["core_features"],
            validation_evidence=data["validation_evidence"],
        )

    @staticmethod
    def from_json_file(path: Path) -> "ProductBrief":
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return ProductBrief.from_dict(data)


def generate_skeleton(brief: ProductBrief, output_dir: Path) -> Path:
    """
    Generate a project skeleton in output_dir based on the given ProductBrief.
    Returns the path to the created project directory.
    """
    start = time.time()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    src_dir = output_dir / "src"
    tests_dir = output_dir / "tests"
    docs_dir = output_dir / "docs"
    for d in (src_dir, tests_dir, docs_dir):
        d.mkdir(exist_ok=True)

    # README
    readme_path = output_dir / "README.md"
    readme_content = f"# {brief.product_name}\n\n"
    readme_content += f"## Target Users\n{brief.target_users}\n\n"
    readme_content += "## Core Features\n" + "\n".join(f"- {f}" for f in brief.core_features) + "\n\n"
    readme_content += f"## Validation Evidence\n{brief.validation_evidence}\n\n"
    readme_content += "## Tech Stack\n" + "\n".join(f"- {s}" for s in brief.tech_stack) + "\n"
    readme_path.write_text(readme_content, encoding="utf-8")

    # Basic authentication module
    auth_path = src_dir / "auth.py"
    auth_content = """\"\"\"Simple token-based authentication module.\"\"\"

SECRET_TOKEN = "secret"

def authenticate(token: str) -> bool:
    \"\"\"Return True if token matches the secret token.\"\"\"
    return token == SECRET_TOKEN
"""
    auth_path.write_text(auth_content, encoding="utf-8")

    # Sample database schema
    db_path = src_dir / "db_schema.sql"
    db_content = """-- Sample SQLite schema
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
    db_path.write_text(db_content, encoding="utf-8")

    # Sample tests
    test_auth_path = tests_dir / "test_auth.py"
    test_auth_content = """import pytest
from src.auth import authenticate

def test_auth_success():
    assert authenticate("secret") is True

def test_auth_failure():
    assert authenticate("wrong") is False
"""
    test_auth_path.write_text(test_auth_content, encoding="utf-8")

    # Ensure generation is fast
    elapsed = time.time() - start
    if elapsed > 5:
        raise RuntimeError(f"Skeleton generation took {elapsed:.2f}s, exceeding 5 seconds")

    return output_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a project skeleton from a product brief.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--json", type=Path, help="Path to JSON file with product brief.")
    group.add_argument("--interactive", action="store_true", help="Fill a form interactively.")
    parser.add_argument("--output", type=Path, default=Path("./generated_project"),
                        help="Output directory for the skeleton.")
    args = parser.parse_args()

    if args.json:
        brief = ProductBrief.from_json_file(args.json)
    else:
        # Interactive form
        print("Enter product details:")
        product_name = input("Product name: ").strip()
        target_users = input("Target users: ").strip()
        core_features = input("Core features (comma separated): ").strip()
        validation_evidence = input("Validation evidence: ").strip()
        brief = ProductBrief(
            product_name=product_name,
            target_users=target_users,
            core_features=[f.strip() for f in core_features.split(",") if f.strip()],
            validation_evidence=validation_evidence,
        )

    generate_skeleton(brief, args.output)
    print(f"Project skeleton generated at {args.output.resolve()}")


if __name__ == "__main__":
    main()
