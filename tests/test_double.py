import unittest
from plover_spanish_mqd import spanish_mqd_single
from plover_spanish_mqd import spanish_mqd_double
from plover_spanish_mqd import system


class TestDouble(unittest.TestCase):

	def setUp(self):
		self.keys = "".join(system.KEYS)
		self.dict = spanish_mqd_double.doubleStrokes
		self.adjs = spanish_mqd_double.adjs
		self.irregular = spanish_mqd_double.irregular

	def tearDown(self):
		self.keys = None
		self.dict = None
		self.adjs = None
		self.irregular = None
		spanish_mqd_single.lastValue = ""

	def test_keyOrder(self):
		for k, v in self.dict.items():
			prevIndex = -1
			curIndex = -1
			for char in k:
				curIndex = self.keys.find(char)
				self.assertTrue(curIndex > prevIndex, k)
				prevIndex = curIndex
