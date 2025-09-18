from typing import List


class GeneratorsBase:
	def __init__(self):
		pass

	def uppercase(self, word: str = "smogtether") -> List[str]:
		if not word:
			raise ValueError("Input word must not be empty")

		if not isinstance(word, str):
			raise TypeError("Input word must be a string")

		raise NotImplementedError("Subclasses should implement this method")

	def fizzbuzz(self, amount: int = 100) -> List[str]:
		if not isinstance(amount, int):
			raise TypeError("Amount must be an integer")

		if amount == 0:
			raise ValueError("Amount must not be zero")

		raise NotImplementedError("Subclasses should implement this method")
