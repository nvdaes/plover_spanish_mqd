import unittest
import os
import json
from plover_spanish_mqd import system

DICT = os.path.join(os.path.dirname(__file__), "..", "plover_spanish_mqd", "dictionaries", "initial.json")


class TestInitial(unittest.TestCase):

	def setUp(self):
		self.keys = "".join(system.KEYS)
		with open(DICT) as f:
			self.dict = json.load(f)

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
				if char == "/":
					curIndex = -1
					prevIndex = -1
					continue
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

	def test_ValueContent(self):
		for k, v in self.dict.items():
			self.assertFalse("//" in v, k)
			self.assertFalse(r"^}" in v, k)
