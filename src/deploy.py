import argparse
import json
import subprocess
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class Deployment:
    provider: str
    cluster_name: str
    subdomain: str

def deploy(deployment: Deployment):
    terraform_cmd = f"terraform apply -auto-approve -var provider={deployment.provider} -var cluster_name={deployment.cluster_name} -var subdomain={deployment.subdomain}"
    subprocess.run(terraform_cmd, shell=True)

def get_deployment_logs(deployment: Deployment):
    terraform_cmd = f"terraform output -json"
    output = subprocess.check_output(terraform_cmd, shell=True)
    return json.loads(output)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", help="Cloud provider")
    parser.add_argument("--cluster-name", help="Kubernetes cluster name")
    parser.add_argument("--subdomain", help="Unique subdomain")
    args = parser.parse_args()
    deployment = Deployment(args.provider, args.cluster_name, args.subdomain)
    deploy(deployment)
    logs = get_deployment_logs(deployment)
    print(logs)

if __name__ == "__main__":
    main()
