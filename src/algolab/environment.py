"""Execution environment and scope handling."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from .errors import RuntimeErrorAlgoLab, SemanticErrorAlgoLab
from .utils import build_suggestion_string, suggest_var


@dataclass(frozen=True)
class TypeSpec:
	"""Represents a scalar or array type."""

	base: str
	size: Optional[int] = None

	@property
	def is_array(self) -> bool:
		return self.size is not None


@dataclass
class Variable:
	"""Represents a typed variable in the environment."""

	type_spec: TypeSpec
	value: Any = None


class Environment:
	"""Environment with optional parent scope."""

	def __init__(self, parent: Optional["Environment"] = None) -> None:
		self._parent = parent
		self._values: dict[str, Variable] = {}

	def declare(self, name: str, type_spec: TypeSpec) -> None:
		if name in self._values:
			raise SemanticErrorAlgoLab(f"Variable deja declaree: {name}")
		initial_value: Any = None
		if type_spec.is_array:
			initial_value = [None] * int(type_spec.size or 0)
		self._values[name] = Variable(type_spec=type_spec, value=initial_value)

	def assign(self, name: str, value: Any) -> None:
		variable = self._resolve(name)
		if variable.type_spec.is_array:
			raise SemanticErrorAlgoLab("Affectation directe sur un tableau interdite")
		variable.value = self._coerce_value(variable.type_spec, value)

	def get(self, name: str) -> Any:
		variable = self._resolve(name)
		if variable.type_spec.is_array:
			raise RuntimeErrorAlgoLab("Un tableau doit etre indexe")
		if variable.value is None:
			raise RuntimeErrorAlgoLab(f"Variable non initialisee: {name}")
		return variable.value

	def get_type(self, name: str) -> str:
		variable = self._resolve(name)
		return variable.type_spec.base

	def get_type_spec(self, name: str) -> TypeSpec:
		variable = self._resolve(name)
		return variable.type_spec

	def set_index(self, name: str, index: int, value: Any) -> None:
		variable = self._resolve(name)
		if not variable.type_spec.is_array:
			raise SemanticErrorAlgoLab("Indexation sur une variable non tableau")
		position = self._to_zero_based(index, variable.type_spec.size)
		scalar_spec = TypeSpec(base=variable.type_spec.base)
		variable.value[position] = self._coerce_value(scalar_spec, value)

	def get_index(self, name: str, index: int) -> Any:
		variable = self._resolve(name)
		if not variable.type_spec.is_array:
			raise SemanticErrorAlgoLab("Indexation sur une variable non tableau")
		position = self._to_zero_based(index, variable.type_spec.size)
		value = variable.value[position]
		if value is None:
			raise RuntimeErrorAlgoLab(f"Variable non initialisee: {name}[{index}]")
		return value

	def _resolve(self, name: str) -> Variable:
		if name in self._values:
			return self._values[name]
		if self._parent is not None:
			return self._parent._resolve(name)
		suggestion = suggest_var(name, self._values.keys())
		suggestion_message = build_suggestion_string(suggestion)
		raise SemanticErrorAlgoLab(f"Variable non declaree: {name}.{suggestion_message}")

	def _coerce_value(self, type_spec: TypeSpec, value: Any) -> Any:
		if type_spec.is_array:
			raise SemanticErrorAlgoLab("Valeur scalaire attendue, pas un tableau")
		type_name = type_spec.base
		if type_name == "ENTIER":
			if isinstance(value, bool) or not isinstance(value, int):
				raise SemanticErrorAlgoLab("Type attendu ENTIER")
			return value
		if type_name == "REEL":
			if isinstance(value, bool):
				raise SemanticErrorAlgoLab("Type attendu REEL")
			if isinstance(value, int):
				return float(value)
			if isinstance(value, float):
				return value
			raise SemanticErrorAlgoLab("Type attendu REEL")
		if type_name == "CARACTERE":
			if not isinstance(value, str):
				raise SemanticErrorAlgoLab("Type attendu CARACTERE")
			return value
		if type_name == "BOOLEEN":
			if not isinstance(value, bool):
				raise SemanticErrorAlgoLab("Type attendu BOOLEEN")
			return value
		raise SemanticErrorAlgoLab(f"Type inconnu: {type_name}")

	def coerce_value(self, type_spec: TypeSpec, value: Any) -> Any:
		return self._coerce_value(type_spec, value)

	def _to_zero_based(self, index: int, size: Optional[int]) -> int:
		if not isinstance(index, int):
			raise SemanticErrorAlgoLab("Index de tableau doit etre un entier")
		if index < 1:
			raise SemanticErrorAlgoLab("Index de tableau commence a 1")
		if size is not None and index > size:
			raise SemanticErrorAlgoLab("Index de tableau hors limites")
		return index - 1
