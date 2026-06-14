import pytest
from src.deployer import generate_deployment_config, deploy_to_staging, get_deployment_logs

def test_generate_deployment_config():
    environment = "staging"
    staging_url = "https://example.com"
    deployment_logs = "deployment_logs.txt"
    deployment_config = generate_deployment_config(environment, staging_url, deployment_logs)
    assert deployment_config.environment == environment
    assert deployment_config.staging_url == staging_url
    assert deployment_config.deployment_logs == deployment_logs

def test_deploy_to_staging():
    environment = "staging"
    staging_url = "https://example.com"
    deployment_logs = "deployment_logs.txt"
    deployment_config = generate_deployment_config(environment, staging_url, deployment_logs)
    deployed_staging_url = deploy_to_staging(deployment_config)
    assert deployed_staging_url == staging_url

def test_get_deployment_logs():
    environment = "staging"
    staging_url = "https://example.com"
    deployment_logs = "deployment_logs.txt"
    deployment_config = generate_deployment_config(environment, staging_url, deployment_logs)
    retrieved_deployment_logs = get_deployment_logs(deployment_config)
    assert retrieved_deployment_logs == deployment_logs

def test_main():
    # Test the main function with valid arguments
    import sys
    import io
    from contextlib import redirect_stdout
    from unittest.mock import patch

    with patch.object(sys, 'argv', ['deployer.py', '-e', 'staging', '-u', 'https://example.com', '-l', 'deployment_logs.txt']):
        with redirect_stdout(io.StringIO()) as f:
            from src.deployer import main
            main()
            output = f.getvalue()
            assert "Deployment successful!" in output
            assert "Staging URL: https://example.com" in output
            assert "Deployment logs: deployment_logs.txt" in output

    # Test the main function with invalid arguments
    with patch.object(sys, 'argv', ['deployer.py', '-e', 'staging']):
        with pytest.raises(SystemExit):
            from src.deployer import main
            main()
