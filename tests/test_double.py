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

	def test_repeatedKey(self):
		values = list(self.dict.values())
		assertEqual(len(set(values)), len(values), f""Repeated values are {values - list(set(values))}")

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

	def test_camina(self):
		key = ("Ccn", "Eneo")
		value = spanish_mqd_double.lookup(key)
		self.assertEqual(value, "caminen ", "Value should be caminen ")

	def test_llega(self):
		key = ("PCVRcs", "Eneo")
		value = spanish_mqd_double.lookup(key)
		self.assertEqual(value, "lleguen ", "Value should be lleguen ")

	def test_garantiza(self):
		key = ("PCTNsn", "Eneo")
		value = spanish_mqd_double.lookup(key)
		self.assertEqual(value, "garanticen ", "Value should be garanticen ")

	def test_proba(self):
		key = ("PRct", "Eneo")
		value = spanish_mqd_double.lookup(key)
		self.assertEqual(value, "prueben ", "Value should be prueben ")

	def test_estable(self):
		key = ("PTNVRc", "Aneo")
		value = spanish_mqd_double.lookup(key)
		self.assertEqual(value, "establezcan ", "Value should be establezcan ")

	def test_cono(self):
		key = ("CNc", "Aneo")
		value = spanish_mqd_double.lookup(key)
		self.assertEqual(value, "conozcan ", "Value should be conozcan ")

	def test_respetuo(self):
		key = ("SPt", "sa")
		value = spanish_mqd_double.lookup(key)
		self.assertEqual(value, "respetuosa ", "Value should be respetuosa ")

