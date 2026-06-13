from src.api_generator import ApiGenerator, DataModel, Table, Column
import pytest

def test_api_generator():
    data_model = DataModel()
    table = Table("users", [Column("id", "int"), Column("name", "string")])
    data_model.add_table(table)
    api_generator = ApiGenerator(data_model)
    endpoints = api_generator.generate_endpoints()
    assert len(endpoints) == 5
    assert endpoints[0].method == "GET"
    assert endpoints[0].path == "/users"
    assert endpoints[0].description == "Get all users"
    swagger = api_generator.generate_swagger()
    assert "swagger" in swagger
    assert "info" in swagger
    assert "paths" in swagger
    assert "/users" in swagger
