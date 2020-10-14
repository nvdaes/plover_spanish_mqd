import os
import sys
sys.path.append(os.path.dirname(__file__))
import spanish_mqd_single
del sys.path[-1]

LONGEST_KEY = 2

VOWELS = ("a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú")

doubleStrokes = {
	"Ccn": "camina"
}

def lookup(key):
	if doubleStrokes.get(key[0]) is None:
		raise KeyError
	spanish_mqd_single.lastValue = doubleStrokes.get(key[0])
	if len(key) == 1:
		return " "
	value = ""
	if spanish_mqd_single.dict.get(key[1]) is not None:
		value = spanish_mqd_single.dict.get(key[1])[1]
	if value == "":
		value = spanish_mqd_single.searchKey(spanish_mqd_single.dict, key[1])
	if spanish_mqd_single.lastValue.endswith("a") and value[0] in VOWELS:
		value = spanish_mqd_single.lastValue[:-1] + value
	elif spanish_mqd_single.lastValue[-1] in ("e", "o") and value[0] == "a":
		value = spanish_mqd_single.lastValue + "zc" + value
	else:
		value = spanish_mqd_single.lastValue + value
	if not value.endswith (" "):
		value = value+ "{^}"
	spanish_mqd_single.lastValue = value
	return value
