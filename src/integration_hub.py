import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Integration:
    name: str
    api_key: str
    health: bool

class IntegrationHub:
    def __init__(self):
        self.integrations = {}

    def add_integration(self, name: str, api_key: str):
        self.integrations[name] = Integration(name, api_key, True)

    def remove_integration(self, name: str):
        if name in self.integrations:
            del self.integrations[name]

    def get_integration(self, name: str) -> Integration:
        return self.integrations.get(name)

    def monitor_health(self):
        for integration in self.integrations.values():
            # Simulate health monitoring
            integration.health = True

    def get_compatible_services(self) -> Dict[str, str]:
        # Simulate version compatibility check
        return {name: "compatible" for name in self.integrations.keys()}

    def one_click_setup(self, name: str, api_key: str):
        self.add_integration(name, api_key)
        self.monitor_health()

def main():
    hub = IntegrationHub()
    hub.one_click_setup("Stripe", "stripe_api_key")
    hub.one_click_setup("Auth0", "auth0_api_key")
    hub.one_click_setup("Zapier", "zapier_api_key")
    print(json.dumps(hub.get_compatible_services()))

if __name__ == "__main__":
    main()
