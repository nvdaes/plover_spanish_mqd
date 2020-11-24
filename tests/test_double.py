import unittest
from plover_spanish_mqd.dictionaries import spanish_mqd_single
from plover_spanish_mqd.dictionaries import spanish_mqd_double
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

	def test_valueTypeAdjs(self):
		for k, v in self.adjs.items():
			self.assertTrue(isinstance(v, str), k)

	def test_keyTypeIrregular(self):
		for k, v in self.irregular.items():
			self.assertTrue(isinstance(k, str), k)

	def test_valueTypeIrregular(self):
		for k, v in self.irregular.items():
			self.assertTrue(isinstance(v, str), k)

	def test_aValues(self):
		key = ("Ccn", "Eneo")
		values = {
			"camina": "caminen ",
			"llega": "lleguen ",
			"proba": "prueben ",
			"garantiza": "garanticen"
		}
		for k, v in values.items():
			spanish_mqd_single.lastValue = k
			value = spanish_mqd_double.lookup(key)
			self.assertEqual(value, v, "Value should be {0}".format(v))

	def test_zValues(self):
		key = ("PTNVRc", "Aneo")
		values = {
			"estable": "establezcan ",
			"cono": "conozcan "
		}
		for k, v in values.items():
			spanish_mqd_single.lastValue = k
			value = spanish_mqd_double.lookup(key)
			self.assertEqual(value, v, "Value should be {0}".format(v))
