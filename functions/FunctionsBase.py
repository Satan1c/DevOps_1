import enum


class CaseState(enum.Enum):
	LOWER = 1
	UPPER = 2
	MIXED = 3


class FunctionsBase:
	def __init__(self) -> None:
		pass

	def print(self, message: str) -> None:
		if not message:
			raise ValueError("Input message must not be empty")

		if not isinstance(message, str):
			raise TypeError("Input message must be a string")

	def case_check(self, text: str) -> CaseState:
		if not text:
			raise ValueError("Input text must not be empty")

		if not isinstance(text, str):
			raise TypeError("Input text must be a string")
