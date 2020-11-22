import unittest
import os
import sys
UNIT_DIR = os.path.dirname(os.path.abspath(__file__))
TOP_DIR = os.path.dirname(os.path.dirname(UNIT_DIR))
SOURCE_DIR = os.path.join(TOP_DIR, "plover_spanish_mqd")
DICT_DIR = os.path.join(TOP_DIR, "dictionaries")
sys.path.append(DICT_DIR)

import spanish_mqd_single

def isDictWellFormed():
	dict = spanish_mqd_single.dict
	for k, v in dict.items():
		if len(v) != 3:
			return False
	return True

class TestSingle(unittest.TestCase):

	def test_single(self):
		self.assertTrue(isDictWellFormed)

