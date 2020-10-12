import os
import sys
sys.path.append(os.path.dirname(__file__))
import spanish_mqd_common
import spanish_mqd_single
del sys.path[-1]

LONGEST_KEY = 2

dict = {
	"Ccn": "camina"
	}


def lookup(key):
	value = dict.get(key[0])
	if value is None:
		raise KeyError
	spanish_mqd_common.lastValue = value
	if len(key) == 1:
		return " "
	value = spanish_mqd_common.reverseSearch(spanish_mqd_single.dict , key[1])
	if spanish_mqd_common.lastValue.endswith("a") and value[0] in ("a", "á", "e", "é", "i", "o", "ó"):
		value = spanish_mqd_common.lastValue[:-1] + value
	elif spanish_mqd_common.lastValue[-1] in ("e", "o") and value[0] in ("a", "á"):
		value = spanish_mqd_common.lastValue + "zc" + value
	else:
		value = spanish_mqd_common.lastValue + value
	spanish_mqd_common.lastValue = value
	value.replace("{i}", "")
	if value.endswith(" "):
		return value
	else:
		return value + "{^}"
