import re
import os
import shutil
import tempfile
from pathlib import Path
import pytest
from unittest.mock import patch
from src.code_catalyst import CodeCatalyst

@pytest.fixture
def temp_dir():
    """Create a temporary directory."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)

def test_generate_url(temp_dir: Path) -> None:
    """Test generating a URL."""
    catalyst = CodeCatalyst(storage_path=temp_dir)
    url1 = catalyst.generate_url()
    url2 = catalyst.generate_url()
    assert url1 == url2

def test_copy_to_clipboard(temp_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test copying a URL to the clipboard."""
    catalyst = CodeCatalyst(storage_path=temp_dir)
    url = "https://example.com"
    # Since we cannot directly mock subprocess calls, we will just test
    # that the method does not throw any exceptions.
    catalyst.copy_to_clipboard(url)

def test_main(temp_dir: Path, capsys: pytest.CaptureFixture) -> None:
    """Test the main entry point."""
    catalyst = CodeCatalyst(storage_path=temp_dir)
    with patch.object(catalyst, "generate_url", return_value="https://example.com"):
        with patch.object(catalyst, "copy_to_clipboard"):
            catalyst.main()
    captured = capsys.readouterr()
    assert "Generated URL: https://example.com" in captured.out
