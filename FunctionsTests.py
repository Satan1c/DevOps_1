import unittest

import functions
from functions import CaseState


class FunctionsPrintTests(unittest.TestCase):
	def setUp(self) -> None:
		self.instance = functions.instance

	def test_print_empty_string(self):
		with self.assertRaises(ValueError) as e:
			self.instance.print("")
			self.assertEqual(str(e), "Input message must not be empty")

	def test_print_non_string(self):
		with self.assertRaises(TypeError) as e:
			self.instance.print(123)
			self.assertEqual(str(e), "Input message must be a string")

	def test_print_message(self):
		result = "my message"
		result = self.instance.print(result)
		self.assertIsNone(result)


class FunctionsCaseCheckTests(unittest.TestCase):
	def setUp(self) -> None:
		self.instance = functions.instance

	def test_case_check_empty_string(self):
		with self.assertRaises(ValueError) as e:
			self.instance.case_check("")
			self.assertEqual(str(e), "Input text must not be empty")

	def test_case_check_non_string(self):
		with self.assertRaises(TypeError) as e:
			self.instance.case_check(123)
			self.assertEqual(str(e), "Input text must be a string")

	def test_case_check_lowercase(self):
		result = self.instance.case_check("lowercase")
		self.assertEqual(result, CaseState.LOWER)

	def test_case_check_uppercase(self):
		result = self.instance.case_check("UPPERCASE")
		self.assertEqual(result, CaseState.UPPER)

	def test_case_check_mixedcase(self):
		result = self.instance.case_check("MixedCase")
		self.assertEqual(result, CaseState.MIXED)


if __name__ == '__main__':
	unittest.main()
