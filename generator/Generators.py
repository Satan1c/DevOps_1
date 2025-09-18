from typing import List

from generator import GeneratorsBase


class Generators(GeneratorsBase):
	def uppercase(self, word: str = "smogtether") -> List[str]:
		super().uppercase(word)

		return [char for char in word.upper()]

	def fizzbuzz(self, amount: int = 100) -> List[str]:
		super().fizzbuzz(amount)

		return ["парне" if i % 2 == 0 else "непарне" for i in range(1, amount + 1)]