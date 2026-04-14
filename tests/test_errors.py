from __future__ import annotations

import pytest
from algolab.errors import SemanticErrorAlgoLab, SyntaxErrorAlgoLab
from algolab.interpreter import Interpreter
from algolab.parser import parse_source


def test_error_format_includes_location() -> None:
    error = SyntaxErrorAlgoLab("Mot-cle manquant", line=4, column=7)
    text = str(error)
    assert "Erreur Syntaxique" in text
    assert "Ligne 4, Colonne 7" in text


def test_syntax_error_exposes_guidance() -> None:
    source = """
    Debut
      TantQue Vrai
        Ecrire "ok"
      FinTantQue
    Fin
    """.strip()
    with pytest.raises(SyntaxErrorAlgoLab) as exc_info:
        parse_source(source)
    assert "FAIRE" in str(exc_info.value)


def test_semantic_error_on_undeclared_variable() -> None:
    source = """
    Debut
      x <- 1
    Fin
    """.strip()
    with pytest.raises(SemanticErrorAlgoLab) as exc_info:
        Interpreter().run(source)
    assert "non declaree" in str(exc_info.value)


def test_semantic_error_on_typo_variable() -> None:
    source = """
    Variable x : Entier
    Debut
      y <- 1
    Fin
    """.strip()
    with pytest.raises(SemanticErrorAlgoLab) as exc_info:
        Interpreter().run(source)
    assert "Vouliez-vous dire 'x' ?" in str(exc_info.value)
