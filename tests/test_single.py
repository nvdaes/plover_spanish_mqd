import unittest
from plover_spanish_mqd.dictionaries import spanish_mqd_single

def isDictWellFormed():
	dict = spanish_mqd_single.dict
	for k, v in dict.items():
		if not isinstance(k, str):
			raise TypeError("Invalid key")
		if len(v) != 3:
			raise ValueError("Tuple with invalid length")
		for fragment in v:
			if not isinstance(fragment, str):
				raise TypeError("Invalid value")
	return True

class TestSingle(unittest.TestCase):

	def test_single(self):
		self.assertTrue(isDictWellFormed)

