from http import HTTPStatus
from json import JSONEncoder
from dataclasses import asdict
from src.data_model import DataModel, DataModelManager
from typing import Dict

class APIGenerator:
    def __init__(self, data_model_manager: DataModelManager):
        self.data_model_manager = data_model_manager

    def generate_api(self) -> Dict[str, Dict[str, str]]:
        api_endpoints = {}
        for data_model_name, data_model in self.data_model_manager.get_data_models().items():
            api_endpoints[data_model_name] = {
                'GET': f'/api/{data_model_name}',
                'POST': f'/api/{data_model_name}',
                'PUT': f'/api/{data_model_name}/{{id}}',
                'DELETE': f'/api/{data_model_name}/{{id}}'
            }
        return api_endpoints

    def generate_swagger(self, api_endpoints: Dict[str, Dict[str, str]]) -> str:
        swagger = {
            'swagger': '2.0',
            'info': {
                'title': 'API Documentation',
                'version': '1.0.0'
            },
            'paths': {}
        }
        for data_model_name, endpoints in api_endpoints.items():
            swagger['paths'][endpoints['GET']] = {
                'get': {
                    'summary': f'Get {data_model_name}',
                    'responses': {
                        '200': {
                            'description': f'{data_model_name} retrieved successfully'
                        }
                    }
                }
            }
            swagger['paths'][endpoints['POST']] = {
                'post': {
                    'summary': f'Create {data_model_name}',
                    'responses': {
                        '201': {
                            'description': f'{data_model_name} created successfully'
                        }
                    }
                }
            }
            swagger['paths'][endpoints['PUT']] = {
                'put': {
                    'summary': f'Update {data_model_name}',
                    'responses': {
                        '200': {
                            'description': f'{data_model_name} updated successfully'
                        }
                    }
                }
            }
            swagger['paths'][endpoints['DELETE']] = {
                'delete': {
                    'summary': f'Delete {data_model_name}',
                    'responses': {
                        '204': {
                            'description': f'{data_model_name} deleted successfully'
                        }
                    }
                }
            }
        return JSONEncoder().encode(swagger)

    def generate_sdk(self, api_endpoints: Dict[str, Dict[str, str]]) -> str:
        sdk = ''
        for data_model_name, endpoints in api_endpoints.items():
            sdk += f'class {data_model_name.capitalize()}:\n'
            sdk += f'    def get(self, id: int):\n'
            sdk += f'        return requests.get({endpoints["GET"]})\n'
            sdk += f'    def create(self, data: Dict[str, str]):\n'
            sdk += f'        return requests.post({endpoints["POST"]}, json=data)\n'
            sdk += f'    def update(self, id: int, data: Dict[str, str]):\n'
            sdk += f'        return requests.put({endpoints["PUT"]}, json=data)\n'
            sdk += f'    def delete(self, id: int):\n'
            sdk += f'        return requests.delete({endpoints["DELETE"]})\n'
        return sdk
