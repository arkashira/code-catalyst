from urllib.parse import urlparse
from deployer import Deployer

def test_deploy():
    deployer = Deployer()
    app_name = "my_app"
    url = deployer.deploy(app_name)
    assert urlparse(url).netloc == f"{app_name}-{list(deployer.deployments.keys())[0]}.example.com"

def test_get_deployment_url():
    deployer = Deployer()
    app_name = "my_app"
    url = deployer.deploy(app_name)
    deployment_id = list(deployer.deployments.keys())[0]
    assert deployer.get_deployment_url(deployment_id) == url

def test_copy_url_to_clipboard():
    deployer = Deployer()
    app_name = "my_app"
    url = deployer.deploy(app_name)
    deployer.copy_url_to_clipboard(url)

def test_get_stable_url():
    deployer = Deployer()
    app_name = "my_app"
    url = deployer.deploy(app_name)
    deployment_id = list(deployer.deployments.keys())[0]
    assert deployer.get_stable_url(deployment_id) == url
