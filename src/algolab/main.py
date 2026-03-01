"""Main entry point for AlgoLab."""

from __future__ import annotations

import argparse
from pathlib import Path

from algolab.errors import AlgoLabError
from algolab.interpreter import Interpreter


def _read_source(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable: {path}")
    return path.read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AlgoLab interpreter")
    parser.add_argument("source", nargs="?", help="Fichier .algo a executer")
    parser.add_argument("-c", "--code", help="Executer du code fourni en argument")
    args = parser.parse_args(argv)

    try:
        if args.code:
            source = args.code
        elif args.source:
            source = _read_source(Path(args.source))
        else:
            parser.error("Veuillez fournir un fichier .algo ou --code")
        Interpreter().run(source)
    except (AlgoLabError, FileNotFoundError) as exc:
        print(exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
