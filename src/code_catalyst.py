import json
import os
import re
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Final

@dataclass
class CodeCatalyst:
    """A simple MVP URL generator and copier."""
    storage_path: Path = Path.home() / ".code_catalyst"

    def __post_init__(self):
        """Initialize the storage directory if it doesn't exist."""
        self.storage_path.mkdir(exist_ok=True)

    def generate_url(self) -> str:
        """Generate a stable, human-readable URL."""
        url_file = self.storage_path / "url.json"
        if url_file.exists():
            with url_file.open("r") as f:
                return json.load(f)["url"]
        else:
            url = f"https://example.com/{uuid.uuid4()}"
            with url_file.open("w") as f:
                json.dump({"url": url}, f)
            return url

    def copy_to_clipboard(self, url: str) -> None:
        """Copy the URL to the system clipboard (best-effort)."""
        try:
            # Use a simple workaround since pyperclip is not in the stdlib
            # and we cannot add external dependencies.
            import subprocess
            if os.name == 'posix':  # Unix/Linux/MacOS/BSDOS
                subprocess.run(['xclip', '-selection', 'c'], input=url.encode())
            elif os.name == 'nt':  # Windows
                subprocess.run(['clip'], input=url.encode())
        except Exception as e:
            print(f"Failed to copy URL to clipboard: {e}")

    def main(self) -> None:
        """Main entry point."""
        url = self.generate_url()
        print(f"Generated URL: {url}")
        self.copy_to_clipboard(url)

if __name__ == "__main__":
    CodeCatalyst().main()
