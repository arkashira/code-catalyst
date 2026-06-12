from src.data_model import DataModel, DataModelManager

def test_data_model():
    data_model = DataModel('User', ['name', 'email'])
    assert data_model.name == 'User'
    assert data_model.fields == ['name', 'email']

def test_data_model_manager():
    data_model_manager = DataModelManager()
    data_model = DataModel('User', ['name', 'email'])
    data_model_manager.add_data_model(data_model)
    assert data_model_manager.get_data_models() == {'User': data_model}
