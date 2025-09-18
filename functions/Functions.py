from functions import FunctionsBase, CaseState


class Functions(FunctionsBase):
	def print(self, message: str) -> None:
		super().print(message)

		print(message)

		return None

	def case_check(self, text: str) -> CaseState:
		super().case_check(text)

		if text.islower():
			return CaseState.LOWER
		elif text.isupper():
			return CaseState.UPPER
		else:
			return CaseState.MIXED