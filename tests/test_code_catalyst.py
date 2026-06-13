import json
import os
import time
import tempfile
from pathlib import Path

import pytest

from code_catalyst import ProductBrief, generate_skeleton


def _create_sample_json(tmp_path: Path) -> Path:
    data = {
        "product_name": "TestApp",
        "target_users": "Developers",
        "core_features": ["Feature A", "Feature B"],
        "validation_evidence": "Survey results",
    }
    json_path = tmp_path / "brief.json"
    json_path.write_text(json.dumps(data), encoding="utf-8")
    return json_path


def test_generate_skeleton_from_json(tmp_path: Path):
    json_path = _create_sample_json(tmp_path)
    brief = ProductBrief.from_json_file(json_path)
    output_dir = tmp_path / "output"
    generate_skeleton(brief, output_dir)

    # Check directories
    assert (output_dir / "src").exists()
    assert (output_dir / "tests").exists()
    assert (output_dir / "docs").exists()

    # Check README contains product name
    readme = output_dir / "README.md"
    assert readme.exists()
    content = readme.read_text(encoding="utf-8")
    assert "TestApp" in content
    assert "Developers" in content
    assert "- Feature A" in content
    assert "- Feature B" in content
    assert "Survey results" in content

    # Check auth module
    auth = output_dir / "src" / "auth.py"
    assert auth.exists()
    assert "def authenticate" in auth.read_text(encoding="utf-8")

    # Check database schema
    db_schema = output_dir / "src" / "db_schema.sql"
    assert db_schema.exists()
    assert "CREATE TABLE users" in db_schema.read_text(encoding="utf-8")


def test_generate_skeleton_from_dict(tmp_path: Path):
    brief = ProductBrief(
        product_name="MyApp",
        target_users="Users",
        core_features=["Login", "Dashboard"],
        validation_evidence="Beta tests",
    )
    output_dir = tmp_path / "output2"
    generate_skeleton(brief, output_dir)

    assert (output_dir / "src" / "auth.py").exists()
    assert (output_dir / "src" / "db_schema.sql").exists()


def test_generation_time(tmp_path: Path):
    brief = ProductBrief(
        product_name="FastApp",
        target_users="Everyone",
        core_features=["Fast Feature"],
        validation_evidence="Speed test",
    )
    output_dir = tmp_path / "fast_output"
    start = time.time()
    generate_skeleton(brief, output_dir)
    elapsed = time.time() - start
    assert elapsed < 5, f"Skeleton generation took {elapsed:.2f}s, expected <5s"
