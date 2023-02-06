import unittest
import os
import json

from plover_spanish_mqd import system
from plover_spanish_mqd import spanish_mqd_single
from . import detectDuplicateKeys

DICT = os.path.join(os.path.dirname(__file__), "..", "plover_spanish_mqd", "dictionaries", "user_es.json")


class TestUser(unittest.TestCase):

	def setUp(self):
		self.keys = "".join(system.KEYS)
		self.singleDict = spanish_mqd_single.dict
		with open(DICT, encoding="utf-8") as f:
			self.dict = json.load(f, object_pairs_hook=detectDuplicateKeys)

	def tearDown(self):
		self.keys = None
		self.singleDict = None
		self.dict = None

	def test_keyOrder(self):
		for k, v in self.dict.items():
			prevIndex = -1
			curIndex = -1
			for char in k:
				if char == "/":
					prevIndex = -1
					curIndex = -1
					continue
				curIndex = self.keys.find(char)
				self.assertTrue(curIndex > prevIndex, k)
				prevIndex = curIndex

	def test_valueType(self):
		for k, v in self.dict.items():
			self.assertTrue(isinstance(v, str), k)

	def test_ValueContent(self):
		for k, v in self.dict.items():
			self.assertFalse("//" in v, k)

	def test_duplicateKeysInSingle(self):
		dictKeys = self.dict.keys()
		singleDictKeys = self.singleDict.keys()
		duplicateKeys = []
		for k in dictKeys:
			if k in singleDictKeys:
				duplicateKeys.append(k)
		self.assertListEqual(duplicateKeys, [], "\rn".join(duplicateKeys))
