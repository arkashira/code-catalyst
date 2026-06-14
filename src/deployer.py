import uuid
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict

@dataclass
class Deployment:
    id: str
    status: str
    staging_url: str
    logs: List[str]

class Deployer:
    def __init__(self):
        self.deployments: List[Deployment] = []
    
    def deploy_mvp(self, code_path: str) -> Deployment:
        if not code_path or not code_path.strip():
            raise ValueError("Code path cannot be empty")
            
        deployment_id = str(uuid.uuid4())[:8]
        staging_url = f"https://staging.example.com/{deployment_id}"
        
        logs = [
            f"INFO: Starting deployment for {code_path}",
            f"INFO: Building container image {deployment_id}",
            f"INFO: Provisioning staging environment",
            f"SUCCESS: Deployment completed at {staging_url}"
        ]
        
        deployment = Deployment(
            id=deployment_id,
            status="success",
            staging_url=staging_url,
            logs=logs
        )
        
        self.deployments.append(deployment)
        return deployment
    
    def get_deployment_logs(self, deployment_id: str) -> List[str]:
        for deployment in self.deployments:
            if deployment.id == deployment_id:
                return deployment.logs
        raise ValueError(f"Deployment {deployment_id} not found")
