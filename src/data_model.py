from dataclasses import dataclass
from typing import Dict, List

@dataclass
class DataModel:
    name: str
    fields: List[str]

class DataModelManager:
    def __init__(self):
        self.data_models = {}

    def add_data_model(self, data_model: DataModel):
        self.data_models[data_model.name] = data_model

    def get_data_models(self) -> Dict[str, DataModel]:
        return self.data_models
