from .auth import Role

class Builder:
    def __init__(self) -> None:
        self.role_definitions: dict[str, Role] = {}

    def enable_auth(self) -> bool:
        return True

    def generate_auth_middleware(self) -> str:
        return "auth_middleware"

    def set_role_definition(self, page: str, role: Role) -> None:
        self.role_definitions[page] = role

    def get_role_definition(self, page: str) -> Role | None:
        return self.role_definitions.get(page)
