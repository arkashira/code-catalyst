import pytest
from deployer import Deployer, Deployment

def test_successful_deployment():
    deployer = Deployer()
    code_path = "./my_mvp_code"
    
    result = deployer.deploy_mvp(code_path)
    
    assert result.status == "success"
    assert result.staging_url.startswith("https://staging.example.com/")
    assert len(result.id) == 8
    assert any("Deployment completed" in log for log in result.logs)
    assert any(code_path in log for log in result.logs)

def test_empty_code_path():
    deployer = Deployer()
    
    with pytest.raises(ValueError, match="Code path cannot be empty"):
        deployer.deploy_mvp("")

def test_deployment_log_retrieval():
    deployer = Deployer()
    first_deployment = deployer.deploy_mvp("./first")
    
    logs = deployer.get_deployment_logs(first_deployment.id)
    
    assert len(logs) == 4
    assert logs[-1].startswith("SUCCESS: Deployment completed")
    assert any("first" in log for log in logs)

def test_invalid_deployment_id():
    deployer = Deployer()
    
    with pytest.raises(ValueError, match="Deployment 999 not found"):
        deployer.get_deployment_logs("999")
