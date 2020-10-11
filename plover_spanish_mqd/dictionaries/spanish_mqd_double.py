import os
import sys
sys.path.append(os.path.dirname(__file__))
import spanish_mqd_common
from spanish_mqd_common import *
from spanish_mqd_dictionary import dict
del sys.path[-1]

LONGEST_KEY = 2

def lookup(key):
	if dict.get(key[0]) is None:
		raise KeyError
	value = dict.get(key[0])[0]
	if not spanish_mqd_common.PAUSE_COMMAND in value:
		raise KeyError
	spanish_mqd_common.lastValue = value
	if len(key) == 1:
		return " "
	value = reverseSearch(dict, key[1])
	removeCommands(value)
	if value[0] in VOWELS:
		value = spanish_mqd_common.lastValue[:-1] + value
	else:
		value = spanish_mqd_common.lastValue + value
	spanish_mqd_common.lastValue = value
	if value.endswith(" "):
		return value
	return value + "{^}"
