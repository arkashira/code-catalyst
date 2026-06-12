# Code Catalyst

A minimal implementation of Backend-as-a-Service (BaaS) with built-in authentication.

## Features

* Authentication via Google and GitHub
* Session tokens stored securely in the database
* Auth can be enabled via a toggle in the project settings

## Usage

1. Create an instance of the `Auth` class
2. Enable authentication using the `enable_auth` method
3. Authenticate with a provider using the `authenticate` method
4. Validate a session token using the `validate_session` method
