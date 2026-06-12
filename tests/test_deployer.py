from deployer import deploy_mvp, get_deployment_status

def test_deploy_mvp():
    project = "test-project"
    deployment = deploy_mvp(project)
    assert deployment.project == project
    assert deployment.subdomain == f"{project}.codecatalyst.io"
    assert deployment.status == "deployed"

def test_get_deployment_status():
    project = "test-project"
    status = get_deployment_status(project)
    assert status == f"{project} is deployed"

def test_main():
    # Simulate running the main function
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    import argparse
    argparse._sys.argv = ["deployer.py", "test-project"]
    from deployer import main
    main()
    sys.stdout = sys.__stdout__
    output = capturedOutput.getvalue()
    assert "Deployment status: deployed" in output
    assert "MVP reachable at: test-project.codecatalyst.io" in output
    assert "test-project is deployed" in output
