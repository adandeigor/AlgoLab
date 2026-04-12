"""Tests for the main CLI entry point."""

from __future__ import annotations

import pytest

from algolab.main import main, __version__


def test_version_flag_exits_zero(capsys: pytest.CaptureFixture[str]) -> None:
    """--version should print the version string and exit with code 0."""
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])
    assert exc_info.value.code == 0


def test_version_flag_prints_version(capsys: pytest.CaptureFixture[str]) -> None:
    """--version output should contain 'AlgoLab' and the package version."""
    with pytest.raises(SystemExit):
        main(["--version"])
    captured = capsys.readouterr()
    output = captured.out + captured.err  # argparse writes to stdout or stderr depending on Python version
    assert "AlgoLab" in output
    assert __version__ in output


def test_version_string_is_not_unknown() -> None:
    """Package version should resolve correctly when installed."""
    assert __version__ != "unknown"
