import pytest
from src.main import DataModel, load_models, generate_api, write_swagger

def test_parse_args() -> None:
    args = ["-m", "model1.json", "-m", "model2.json"]
    assert args[0] == "-m"
    assert args[1] == "model1.json"
    assert args[2] == "-m"
    assert args[3] == "model2.json"

def test_load_models() -> None:
    models = [
        {"name": "Model1", "fields": ["field1", "field2"]},
        {"name": "Model2", "fields": ["field3", "field4"]}
    ]
    data_models = [
        DataModel("Model1", ["field1", "field2"]),
        DataModel("Model2", ["field3", "field4"])
    ]
    assert load_models(["model1.json", "model2.json"]) == {model.name: model for model in data_models}

def test_generate_api() -> None:
    models = {
        "Model1": DataModel("Model1", ["field1", "field2"]),
        "Model2": DataModel("Model2", ["field3", "field4"])
    }
    api = generate_api(models)
    assert api["Model1"]["get"] == "/Model1"
    assert api["Model1"]["post"] == "/Model1"
    assert api["Model1"]["put"] == "/Model1/field1"
    assert api["Model1"]["delete"] == "/Model1/field1"
    assert api["Model2"]["get"] == "/Model2"
    assert api["Model2"]["post"] == "/Model2"
    assert api["Model2"]["put"] == "/Model2/field3"
    assert api["Model2"]["delete"] == "/Model2/field3"

def test_write_swagger() -> None:
    api = {
        "Model1": {
            "get": "/Model1",
            "post": "/Model1",
            "put": "/Model1/field1",
            "delete": "/Model1/field1"
        },
        "Model2": {
            "get": "/Model2",
            "post": "/Model2",
            "put": "/Model2/field3",
            "delete": "/Model2/field3"
        }
    }
    with pytest.raises(FileNotFoundError):
        write_swagger(api)
