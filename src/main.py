from src.components import Component, ComponentLibrary, ApplicationBuilder
import json

def main():
    library = ComponentLibrary()
    builder = ApplicationBuilder()

    # Add components to library
    library.add_component(Component("Login", "Login functionality", {"username": "", "password": ""}))
    library.add_component(Component("Dashboard", "Dashboard view", {"title": "", "content": ""}))

    # Get components from library
    components = library.get_components()

    # Add components to application
    for component in components:
        builder.add_component_to_app(component)

    # Get application components
    app_components = builder.get_app_components()

    # Print application components
    print("Application Components:")
    for component in app_components:
        print(f"Name: {component.name}, Description: {component.description}, Config: {json.dumps(component.config)}")

if __name__ == "__main__":
    main()
