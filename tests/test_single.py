import unittest
from plover_spanish_mqd import spanish_mqd_single
from plover_spanish_mqd import system


class TestSingle(unittest.TestCase):

	def setUp(self):
		self.keys = "".join(system.KEYS)
		self.dict = spanish_mqd_single.dict

	def tearDown(self):
		self.keys = None
		self.dict = None

	def test_keyOrder(self):
		for k, v in self.dict.items():
			prevIndex = -1
			curIndex = -1
			for char in k:
				curIndex = self.keys.find(char)
				self.assertTrue(curIndex > prevIndex, k)
				prevIndex = curIndex

	def test_value(self):
		keys = []
		for k, v in self.dict.items():
			for value in v:
				if "\t" in value:
					keys.append(k)
		self.assertEqual(keys, [], "\r\n".join(keys))
