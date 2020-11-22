import unittest
from plover_spanish_mqd.dictionaries import spanish_mqd_double
from plover_spanish_mqd import system


class TestSingle(unittest.TestCase):

	def setUp(self):
		self.dict = spanish_mqd_double.doubleStrokes
		self.adjs = spanish_mqd_double.adjs
		self.keys = "".join(system.KEYS)

	def tearDown(self):
		self.dict = None
		self.adjs = None
		self.keys = None

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
			self.assertTrue(isinstance(v, str), k)

	def test_keyTypeAdjs(self):
		for k, v in self.adjs.items():
			self.assertTrue(isinstance(k, str), k)

	def test_keyOrderAdjs(self):
		for k, v in self.adjs.items():
			prevIndex = -1
			curIndex = -1
			for char in k:
				curIndex = self.keys.find(char)
				self.assertTrue(curIndex > prevIndex, k)
				prevIndex = curIndex

	def test_valueTypeAdjs(self):
		for k, v in self.adjs.items():
			self.assertTrue(isinstance(v, str), k)
