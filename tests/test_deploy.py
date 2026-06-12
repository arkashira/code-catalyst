import pytest
from unittest.mock import patch, MagicMock
from deploy import deploy, get_deployment_logs, Deployment

def test_deploy():
    deployment = Deployment("digitalocean", "test-cluster", "test-subdomain")
    with patch("subprocess.run") as mock_run:
        deploy(deployment)
        mock_run.assert_called_once()

def test_get_deployment_logs():
    deployment = Deployment("digitalocean", "test-cluster", "test-subdomain")
    with patch("subprocess.check_output") as mock_output:
        mock_output.return_value = b'{"logs": "test-logs"}'
        logs = get_deployment_logs(deployment)
        assert logs == {"logs": "test-logs"}

def test_main():
    with patch("argparse.ArgumentParser") as mock_parser:
        mock_parser.return_value.parse_args.return_value = MagicMock(provider="digitalocean", cluster_name="test-cluster", subdomain="test-subdomain")
        with patch("deploy.deploy") as mock_deploy:
            with patch("deploy.get_deployment_logs") as mock_get_logs:
                mock_get_logs.return_value = {"logs": "test-logs"}
                from deploy import main
                main()
                mock_deploy.assert_called_once()
                mock_get_logs.assert_called_once()
