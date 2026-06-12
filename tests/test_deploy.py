from deploy import deploy

def test_deploy():
    image_name = "test-image"
    cluster_name = "test-cluster"
    deployment = deploy(image_name, cluster_name)
    assert deployment.image_name == image_name
    assert deployment.cluster_name == cluster_name
    assert deployment.public_url == f"https://{cluster_name}.example.com"

def test_push_to_docker_hub():
    image_name = "test-image"
    deploy.push_to_docker_hub(image_name)

def test_create_kubernetes_deployment():
    cluster_name = "test-cluster"
    image_name = "test-image"
    deploy.create_kubernetes_deployment(cluster_name, image_name)

def test_get_public_url():
    cluster_name = "test-cluster"
    public_url = deploy.get_public_url(cluster_name)
    assert public_url == f"https://{cluster_name}.example.com"
