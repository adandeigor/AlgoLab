""" Utility functions for AlgoLab."""

from difflib import SequenceMatcher, get_close_matches


def suggest_var(typo: str, names: list[str]) -> str:
    if not names:
        return ""

    matches = get_close_matches(typo, names, n=1)
    if matches:
        return matches[0]

    ranked = sorted(names, key=lambda n: SequenceMatcher(None, typo, n).ratio(), reverse=True)
    return ranked[0]


def build_suggestion_string(suggestion: str):
    if not suggestion:
        return ""
    return f" Vouliez-vous dire '{suggestion}' ?"
