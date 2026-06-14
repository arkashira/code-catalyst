from project_blueprint import generate_project_skeleton, upload_json, fill_form
import json

def test_generate_project_skeleton():
    blueprint = fill_form("Test Project", "Developers", ["Feature 1", "Feature 2"], "Validation Evidence")
    skeleton = generate_project_skeleton(blueprint)
    assert skeleton["folder_structure"]["name"] == "Test Project"
    assert skeleton["README"].startswith("# Test Project")
    assert skeleton["tech_stack"] == ["Python", "JSON"]
    assert skeleton["basic_auth_module"]["username"] == "admin"
    assert skeleton["sample_database_schema"]["users"]["id"] == "int"

def test_upload_json():
    json_data = '{"name": "Test Project", "target_users": "Developers", "core_features": ["Feature 1", "Feature 2"], "validation_evidence": "Validation Evidence"}'
    blueprint = upload_json(json_data)
    assert blueprint.name == "Test Project"
    assert blueprint.target_users == "Developers"
    assert blueprint.core_features == ["Feature 1", "Feature 2"]
    assert blueprint.validation_evidence == "Validation Evidence"

def test_fill_form():
    blueprint = fill_form("Test Project", "Developers", ["Feature 1", "Feature 2"], "Validation Evidence")
    assert blueprint.name == "Test Project"
    assert blueprint.target_users == "Developers"
    assert blueprint.core_features == ["Feature 1", "Feature 2"]
    assert blueprint.validation_evidence == "Validation Evidence"

def test_generate_project_skeleton_edge_case():
    blueprint = fill_form("", "", [], "")
    skeleton = generate_project_skeleton(blueprint)
    assert skeleton["folder_structure"]["name"] == ""
    assert skeleton["README"].startswith("# ")
    assert skeleton["tech_stack"] == ["Python", "JSON"]
    assert skeleton["basic_auth_module"]["username"] == "admin"
    assert skeleton["sample_database_schema"]["users"]["id"] == "int"
