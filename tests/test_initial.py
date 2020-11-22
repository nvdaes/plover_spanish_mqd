import unittest
import os
import json
from plover_spanish_mqd import system

DICT = os.path.join(DICT_DIR, "initial.json")


class TestInitial(unittest.TestCase):

	def setUp(self):
		self.keys = "".join(system.KEYS)
		with open(DICT) as f:
			dict = json.load(F)

	def tearDown(self):
		self.dict = None
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

	def test_command(self):
		for k, v in self.dict.items():
			if v.startswith(":initial:"):
				self.assertEqual(len(v.split(" | ")), 2, k)


