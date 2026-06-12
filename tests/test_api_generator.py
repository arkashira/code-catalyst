from src.api_generator import APIGenerator
from src.data_model import DataModel, DataModelManager

def test_api_generator():
    data_model_manager = DataModelManager()
    api_generator = APIGenerator(data_model_manager)
    data_model = DataModel('User', ['name', 'email'])
    data_model_manager.add_data_model(data_model)
    api_endpoints = api_generator.generate_api()
    assert api_endpoints == {'User': {'GET': '/api/User', 'POST': '/api/User', 'PUT': '/api/User/{id}', 'DELETE': '/api/User/{id}'}}

def test_generate_swagger():
    data_model_manager = DataModelManager()
    api_generator = APIGenerator(data_model_manager)
    data_model = DataModel('User', ['name', 'email'])
    data_model_manager.add_data_model(data_model)
    api_endpoints = api_generator.generate_api()
    swagger = api_generator.generate_swagger(api_endpoints)
    assert 'swagger' in swagger
    assert 'info' in swagger
    assert 'paths' in swagger

def test_generate_sdk():
    data_model_manager = DataModelManager()
    api_generator = APIGenerator(data_model_manager)
    data_model = DataModel('User', ['name', 'email'])
    data_model_manager.add_data_model(data_model)
    api_endpoints = api_generator.generate_api()
    sdk = api_generator.generate_sdk(api_endpoints)
    assert 'class User:' in sdk
