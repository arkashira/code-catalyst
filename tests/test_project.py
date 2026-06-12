import os
import json
from project import Project, create_project
import pytest

def test_create_project(tmp_path):
    project = Project(
        name='test-project',
        industry='test-industry',
        core_feature='test-core-feature',
        pricing_model='test-pricing-model',
        target_audience='test-target-audience'
    )
    create_project(project)
    assert os.path.exists('test-project')
    assert os.path.exists(os.path.join('test-project', 'src'))
    assert os.path.exists(os.path.join('test-project', 'tests'))
    assert os.path.exists(os.path.join('test-project', 'README.md'))
    assert os.path.exists(os.path.join('test-project', 'github.json'))
    with open(os.path.join('test-project', 'README.md'), 'r') as f:
        assert f.read() == '# test-project\nIndustry: test-industry\nCore Feature: test-core-feature\nPricing Model: test-pricing-model\nTarget Audience: test-target-audience\n'
    with open(os.path.join('test-project', 'github.json'), 'r') as f:
        assert json.load(f) == {
            'name': 'test-project',
            'description': 'test-project SaaS MVP project',
            'keywords': ['test-industry', 'test-core-feature'],
            'license': 'MIT'
        }

def test_main(tmp_path):
    import sys
    import io
    import argparse
    from project import main
    sys.argv = ['project.py', '--name', 'test-project', '--industry', 'test-industry', '--core-feature', 'test-core-feature', '--pricing-model', 'test-pricing-model', '--target-audience', 'test-target-audience']
    main()
    assert os.path.exists('test-project')
    assert os.path.exists(os.path.join('test-project', 'src'))
    assert os.path.exists(os.path.join('test-project', 'tests'))
    assert os.path.exists(os.path.join('test-project', 'README.md'))
    assert os.path.exists(os.path.join('test-project', 'github.json'))

def test_project_dataclass():
    project = Project(
        name='test-project',
        industry='test-industry',
        core_feature='test-core-feature',
        pricing_model='test-pricing-model',
        target_audience='test-target-audience'
    )
    assert project.name == 'test-project'
    assert project.industry == 'test-industry'
    assert project.core_feature == 'test-core-feature'
    assert project.pricing_model == 'test-pricing-model'
    assert project.target_audience == 'test-target-audience'
