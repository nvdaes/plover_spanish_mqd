import unittest
from plover_spanish_mqd.dictionaries import spanish_mqd_single

def isDictWellFormed():
	dict = spanish_mqd_single.dict
	for k, v in dict.items():
		if len(v) != 3:
			return False
	return True

class TestSingle(unittest.TestCase):

	def test_single(self):
		self.assertTrue(isDictWellFormed)

