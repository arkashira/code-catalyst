import argparse
from dataclasses import dataclass

@dataclass
class Deployment:
    image_name: str
    cluster_name: str
    public_url: str

def push_to_docker_hub(image_name: str) -> None:
    """Simulate pushing an image to Docker Hub."""
    print(f"Pushing {image_name} to Docker Hub")

def create_kubernetes_deployment(cluster_name: str, image_name: str) -> None:
    """Simulate creating a Kubernetes deployment."""
    print(f"Creating deployment on {cluster_name} with {image_name}")

def get_public_url(cluster_name: str) -> str:
    """Simulate retrieving a public HTTPS URL for a cluster."""
    return f"https://{cluster_name}.example.com"

def deploy(image_name: str, cluster_name: str) -> Deployment:
    """Perform the full deployment workflow:
    1. Push the image to Docker Hub.
    2. Create a Kubernetes deployment.
    3. Retrieve the public URL.
    Returns a Deployment dataclass instance.
    """
    push_to_docker_hub(image_name)
    create_kubernetes_deployment(cluster_name, image_name)
    public_url = get_public_url(cluster_name)
    return Deployment(image_name, cluster_name, public_url)

deploy.push_to_docker_hub = push_to_docker_hub
deploy.create_kubernetes_deployment = create_kubernetes_deployment
deploy.get_public_url = get_public_url
