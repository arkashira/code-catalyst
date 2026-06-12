import pytest
from project_wizard import Project, create_project
import os
import shutil

def test_create_project():
    project = Project(
        name="test-project",
        industry="test-industry",
        core_feature="test-core-feature",
        pricing_model="test-pricing-model",
        target_audience="test-target-audience",
    )

    create_project(project)

    assert os.path.exists("test-project")
    assert os.path.exists("test-project/src")
    assert os.path.exists("test-project/tests")
    assert os.path.exists("test-project/README.md")
    assert os.path.exists("test-project/pyproject.toml")

    shutil.rmtree("test-project")

def test_main():
    # Test main function with arguments
    import sys
    sys.argv = ["project_wizard.py", "--name", "test-project", "--industry", "test-industry", "--core-feature", "test-core-feature", "--pricing-model", "test-pricing-model", "--target-audience", "test-target-audience"]
    from project_wizard import main
    main()

    assert os.path.exists("test-project")
    assert os.path.exists("test-project/src")
    assert os.path.exists("test-project/tests")
    assert os.path.exists("test-project/README.md")
    assert os.path.exists("test-project/pyproject.toml")

    shutil.rmtree("test-project")
