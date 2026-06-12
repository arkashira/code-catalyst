from integration_hub import IntegrationHub, Integration

def test_add_integration():
    hub = IntegrationHub()
    hub.add_integration("Stripe", "stripe_api_key")
    assert len(hub.integrations) == 1

def test_remove_integration():
    hub = IntegrationHub()
    hub.add_integration("Stripe", "stripe_api_key")
    hub.remove_integration("Stripe")
    assert len(hub.integrations) == 0

def test_get_integration():
    hub = IntegrationHub()
    hub.add_integration("Stripe", "stripe_api_key")
    integration = hub.get_integration("Stripe")
    assert integration.name == "Stripe"

def test_monitor_health():
    hub = IntegrationHub()
    hub.add_integration("Stripe", "stripe_api_key")
    hub.monitor_health()
    integration = hub.get_integration("Stripe")
    assert integration.health

def test_get_compatible_services():
    hub = IntegrationHub()
    hub.add_integration("Stripe", "stripe_api_key")
    services = hub.get_compatible_services()
    assert len(services) == 1

def test_one_click_setup():
    hub = IntegrationHub()
    hub.one_click_setup("Stripe", "stripe_api_key")
    integration = hub.get_integration("Stripe")
    assert integration.name == "Stripe"
    assert integration.health
