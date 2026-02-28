"""AlgoLab error types and messages."""

class AlgoLabError(Exception):
    """Base class for AlgoLab errors."""

    def __init__(
        self,
        message: str,
        line: int | None = None,
        column: int | None = None,
        prefix: str | None = None,
    ) -> None:
        self.raw_message = message
        self.line = line
        self.column = column
        location = ""
        if line is not None and column is not None:
            location = f" (Ligne {line}, Colonne {column})"
        final = f"{prefix}{location} : {message}" if prefix else message
        super().__init__(final)


class SyntaxErrorAlgoLab(AlgoLabError):
    """Syntax error with location details."""

    def __init__(self, message: str, line: int | None = None, column: int | None = None) -> None:
        super().__init__(message, line=line, column=column, prefix="Erreur Syntaxique")


class SemanticErrorAlgoLab(AlgoLabError):
    """Semantic error raised during analysis or execution."""

    def __init__(self, message: str, line: int | None = None, column: int | None = None) -> None:
        super().__init__(message, line=line, column=column, prefix="Erreur Semantique")


class RuntimeErrorAlgoLab(AlgoLabError):
    """Runtime error raised during execution."""

    def __init__(self, message: str, line: int | None = None, column: int | None = None) -> None:
        super().__init__(message, line=line, column=column, prefix="Erreur d execution")