import os
import sys
sys.path.append(os.path.dirname(__file__))
import spanish_mqd_common
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

dict = {
	"SC": ("casa ", "ca", True),
	"N": ("nana ", "n", False)
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
		if spanish_mqd_common.lastValue == "" or spanish_mqd_common.lastValue.endswith(" ") or spanish_mqd_common.markedAsInitial() or not dict.get(key[0])[2]:
			value = dict.get(key[0])[0] 
		if value == "":
			value = spanish_mqd_common.reverseSearch(dict, key[0])
	spanish_mqd_common.lastValue = value
	value.replace("{i}", "")
	if value.endswith(" "):
		return value
	return value + "{^}"
