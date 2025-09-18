import unittest
import generator

class GeneratorsUppercaseTests(unittest.TestCase):
	def setUp(self) -> None:
		self.instance = generator.instance

	def test_uppercase_empty_string(self):
		with self.assertRaises(ValueError) as e:
			list(self.instance.uppercase(""))
			self.assertEqual(str(e), "Input text must not be empty")

	def test_uppercase_non_string(self):
		with self.assertRaises(TypeError) as e:
			list(self.instance.uppercase(123))
			self.assertEqual(str(e), "Input text must be a string")

	def test_uppercase_conversion(self):
		result = list(self.instance.uppercase("Hello"))
		self.assertEqual(result, ['H', 'E', 'L', 'L', 'O'])

class GeneratorsFizzBuzzTests(unittest.TestCase):
	def setUp(self) -> None:
		self.instance = generator.instance

	def test_fizzbuzz_non_integer(self):
		with self.assertRaises(TypeError) as e:
			list(self.instance.fizzbuzz("100"))
			self.assertEqual(str(e), "Amount must be an integer")

	def test_fizzbuzz_zero(self):
		with self.assertRaises(ValueError) as e:
			list(self.instance.fizzbuzz(0))
			self.assertEqual(str(e), "Amount must not be zero")

	def test_fizzbuzz_standard(self):
		result = list(self.instance.fizzbuzz(5))
		expected = [
			"непарне", "парне", "непарне", "парне", "непарне"
		]
		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()
