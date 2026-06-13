import json
import uuid
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class Deployment:
    id: str
    url: str

class Deployer:
    def __init__(self):
        self.deployments = {}

    def deploy(self, app_name):
        deployment_id = str(uuid.uuid4())
        url = f"https://{app_name}-{deployment_id}.example.com"
        self.deployments[deployment_id] = Deployment(deployment_id, url)
        return url

    def get_deployment_url(self, deployment_id):
        deployment = self.deployments.get(deployment_id)
        if deployment:
            return deployment.url
        return None

    def copy_url_to_clipboard(self, url):
        # Simulate copying to clipboard
        print(f"URL copied to clipboard: {url}")

    def get_stable_url(self, deployment_id):
        deployment = self.deployments.get(deployment_id)
        if deployment:
            return deployment.url
        return None
