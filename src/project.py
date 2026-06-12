import os
import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class Project:
    name: str
    industry: str
    core_feature: str
    pricing_model: str
    target_audience: str

def create_project(project: Project):
    try:
        os.mkdir(project.name)
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(project.name, 'src'))
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(project.name, 'tests'))
    except FileExistsError:
        pass
    with open(os.path.join(project.name, 'README.md'), 'w') as f:
        f.write(f'# {project.name}\n')
        f.write(f'Industry: {project.industry}\n')
        f.write(f'Core Feature: {project.core_feature}\n')
        f.write(f'Pricing Model: {project.pricing_model}\n')
        f.write(f'Target Audience: {project.target_audience}\n')
    with open(os.path.join(project.name, 'github.json'), 'w') as f:
        json.dump({
            'name': project.name,
            'description': f'{project.name} SaaS MVP project',
            'keywords': [project.industry, project.core_feature],
            'license': 'MIT'
        }, f)

def main():
    parser = ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--industry', required=True)
    parser.add_argument('--core-feature', required=True)
    parser.add_argument('--pricing-model', required=True)
    parser.add_argument('--target-audience', required=True)
    args = parser.parse_args()
    project = Project(
        name=args.name,
        industry=args.industry,
        core_feature=args.core_feature,
        pricing_model=args.pricing_model,
        target_audience=args.target_audience
    )
    create_project(project)

if __name__ == '__main__':
    main()
