"""code_catalyst – a tiny idea‑capture wizard.

The module provides:

* `Idea` – a dataclass representing a validated product idea.
* `InMemoryDB` – a very small in‑memory storage that mimics a DB table.
* `IdeaWizard` – the core class that validates input and stores it.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass(frozen=True)
class Idea:
    """A validated product idea."""

    product_name: str
    target_audience: str
    core_features: List[str]
    revenue_model: str

    def to_json(self) -> str:
        """Return a JSON representation of the idea."""
        return json.dumps(asdict(self), ensure_ascii=False)


class InMemoryDB:
    """A minimal in‑memory store for `Idea` objects."""

    def __init__(self) -> None:
        self._ideas: List[Idea] = []

    def add(self, idea: Idea) -> None:
        """Persist an `Idea` instance."""
        self._ideas.append(idea)

    def all(self) -> List[Idea]:
        """Return a copy of all stored ideas."""
        return list(self._ideas)


class IdeaWizard:
    """Collects, validates and stores product ideas."""

    REQUIRED_FIELDS = {"product_name", "target_audience", "core_features", "revenue_model"}

    @staticmethod
    def _validate_non_empty_string(value: Any, field_name: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"'{field_name}' must be a non‑empty string.")

    @staticmethod
    def _validate_core_features(value: Any) -> None:
        if not isinstance(value, list) or not value:
            raise ValueError("'core_features' must be a non‑empty list.")
        for i, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                raise ValueError(f"core_features[{i}] must be a non‑empty string.")

    def validate(self, data: Dict[str, Any]) -> Idea:
        """Validate raw input and return an `Idea` instance.

        Raises:
            ValueError: If any required field is missing or invalid.
        """
        missing = self.REQUIRED_FIELDS - data.keys()
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(sorted(missing))}")

        # Validate each field
        self._validate_non_empty_string(data["product_name"], "product_name")
        self._validate_non_empty_string(data["target_audience"], "target_audience")
        self._validate_core_features(data["core_features"])
        self._validate_non_empty_string(data["revenue_model"], "revenue_model")

        # All checks passed – build the Idea
        return Idea(
            product_name=data["product_name"].strip(),
            target_audience=data["target_audience"].strip(),
            core_features=[feat.strip() for feat in data["core_features"]],
            revenue_model=data["revenue_model"].strip(),
        )

    def process_submission(self, data: Dict[str, Any], db: InMemoryDB) -> Idea:
        """Validate the payload and store the resulting `Idea` in `db`.

        Returns:
            The stored `Idea` instance.

        Raises:
            ValueError: Propagated from `validate` if data is invalid.
        """
        idea = self.validate(data)
        db.add(idea)
        return idea
