from documentation import SupportResources, Resource

def test_add_documentation_resource():
    support_resources = SupportResources()
    support_resources.add_documentation_resource("Getting Started", "This is a getting started guide.")
    assert len(support_resources.get_documentation_resources()) == 1

def test_get_documentation_resources():
    support_resources = SupportResources()
    support_resources.add_documentation_resource("Getting Started", "This is a getting started guide.")
    resources = support_resources.get_documentation_resources()
    assert len(resources) == 1
    assert resources[0].title == "Getting Started"
    assert resources[0].content == "This is a getting started guide."

def test_save_documentation_to_json():
    support_resources = SupportResources()
    support_resources.add_documentation_resource("Getting Started", "This is a getting started guide.")
    support_resources.save_documentation_to_json("documentation.json")
    with open("documentation.json", "r") as f:
        data = f.read()
    assert data == '[{"title": "Getting Started", "content": "This is a getting started guide."}]'

def test_load_documentation_from_json():
    support_resources = SupportResources()
    support_resources.load_documentation_from_json("documentation.json")
    resources = support_resources.get_documentation_resources()
    assert len(resources) == 1
    assert resources[0].title == "Getting Started"
    assert resources[0].content == "This is a getting started guide."
