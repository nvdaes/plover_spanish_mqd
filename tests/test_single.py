import unittest
from plover_spanish_mqd.dictionaries import spanish_mqd_single

class TestSingle(unittest.TestCase):

	def setUp(self):
		self.dict = spanish_mqd_single.dict

	def test_keyType(self):
		for k, v in self.dict.items():
			self.assertTrue(isinstance(k, str))

	def test_valueType(self):
		for k, v in self.dict.items():
			self.assertTrue(isinstance(v, tuple))

	def test_valueLenght(self):
		for k, v in self.dict.items():
			self.assertTrue(len(v) == 3)

