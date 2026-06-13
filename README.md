# code-catalyst

A minimal, pure‑Python implementation of an “idea capture wizard” used by the
founder onboarding flow.

## Features

- Collects product name, target audience, core features and revenue model.
- Validates that all required fields are present and non‑empty.
- Stores the validated idea in an in‑memory database (a stand‑in for a real
  persistence layer).

## Usage

The library is deliberately tiny – it can be used directly from Python code:
