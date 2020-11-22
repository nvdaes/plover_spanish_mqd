import unittest
from plover_spanish_mqd.dictionaries import spanish_mqd_single
from plover_spanish_mqd import system


class TestSingle(unittest.TestCase):

	def setUp(self):
		self.keys = "".join(system.KEYS)
		self.dict = spanish_mqd_single.dict

	def tearDown(self):
		self.keys = None
		self.dict = None

	def test_keyType(self):
		for k, v in self.dict.items():
			self.assertTrue(isinstance(k, str), k)

	def test_keyOrder(self):
		for k, v in self.dict.items():
			prevIndex = -1
			curIndex = -1
			for char in k:
				curIndex = self.keys.find(char)
				self.assertTrue(curIndex > prevIndex, k)
				prevIndex = curIndex

	def test_valueType(self):
		for k, v in self.dict.items():
			self.assertTrue(isinstance(v, tuple), k)

	def test_valueLenght(self):
		for k, v in self.dict.items():
			self.assertTrue(len(v) == 2, k)

