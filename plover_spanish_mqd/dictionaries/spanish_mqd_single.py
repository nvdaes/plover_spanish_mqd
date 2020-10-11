import os
import sys
sys.path.append(os.path.dirname(__file__))
import spanish_mqd_common
from spanish_mqd_common import *
from spanish_mqd_dictionary import dict
del sys.path[-1]

LONGEST_KEY = 1

numbers = {
	"S": "1",
	"P": "2",
	"T": "3",
	"V": "4",
	"I": "5",
	"O": "0",
	"c": "6",
	"t": "7",
	"p": "8",
	"i": "9"
}


def lookup(key):
	value = ""
	# Numbers
	if "#" in key[0]:
		for k in key[0]:
			if k in ("A", "#"):
				continue
			numberValue = numbers.get(k)
			if numberValue is None:
				break
			value += numberValue
		if value != "" and "A" in key[0]:
			if len(value) > 1:
				value = value[::-1]
			else:
				value = "{firstDigit}{secondDigit}".format(firstDigit=value, secondDigit=value)
	if value == "" and dict.get(key[0]) is not None:
		if not dict.get(key[0])[2] or isInitial():
			value = dict.get(key[0])[0] 
	if value == "":
		value = reverseSearch(dict, key[0])
	spanish_mqd_common.lastValue = value
	removeCommands(value)
	if value.endswith(" "):
		return value
	return value + "{^}"
