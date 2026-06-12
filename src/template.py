import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Template:
    text: str
    logo: str
    brand_assets: Dict[str, str]

    def to_json(self):
        return {
            "text": self.text,
            "logo": self.logo,
            "brand_assets": self.brand_assets
        }

    @classmethod
    def from_json(cls, data: Dict):
        return cls(
            text=data["text"],
            logo=data["logo"],
            brand_assets=data["brand_assets"]
        )

class TemplateEditor:
    def __init__(self, template: Template):
        self.template = template

    def edit_text(self, new_text: str):
        self.template.text = new_text

    def upload_logo(self, new_logo: str):
        self.template.logo = new_logo

    def upload_brand_assets(self, new_brand_assets: Dict[str, str]):
        self.template.brand_assets = new_brand_assets

    def save(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.template.to_json(), f)

    @classmethod
    def load(cls, filename: str):
        with open(filename, "r") as f:
            data = json.load(f)
            template = Template.from_json(data)
            return cls(template)

    def preview(self):
        print("Text:", self.template.text)
        print("Logo:", self.template.logo)
        print("Brand Assets:", self.template.brand_assets)
