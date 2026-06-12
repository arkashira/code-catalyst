# Code Catalyst
A no-code feature builder with authentication and role-based access controls.

## Features

* Toggle to enable authentication
* Automatic generation of JWT-based auth middleware
* Role definitions (admin, user) can be set per page

## Usage

1. Create an instance of `AuthConfig` with the desired settings.
2. Use the `generate_jwt_middleware` function to generate the JWT middleware.
3. Use the `set_role_definitions` function to set role definitions for each page.
4. Use the `toggle_authentication` function to toggle authentication on or off.
