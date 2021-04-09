LONGEST_KEY = 2

import os
import sys
sys.path.append(os.path.dirname(__file__))
import spanish_mqd_single
import spanish_mqd_double
del sys.path[-1]



lastValue = ""

def searchKey(dictionary, stroke):
	searchKey = stroke[:]
	searchKeyValue = ""
	lenSearched = 0
	value = ""
	while len(searchKey) > 0:
		if dictionary.get(searchKey) is not None:
			searchKeyValue = dictionary.get(searchKey)[1]
		if searchKeyValue == "":
			searchKey = searchKey[:len(searchKey) - 1]
		else:
			value += searchKeyValue
			searchKeyValue = ""
			lenSearched += len(searchKey)
			searchKey = stroke[lenSearched:]
	if value == "":
		value = "{empty}"
	return value


def lookup(key):
	lastValue = ""
	value = ""

	# Double
	if spanish_mqd_double.doubleStrokes.get(key[0]) is not None:
		lastValue = doubleStrokes.get(key[0])
		if len(key) == 1:
			return
		if key[1] == "*":
			lastValue = ""
			return " "
		value = searchKey(spanish_mqd_single.dict, key[1])
		if lastValue.endswith("a") and value[0] in spanish_mqd_double.VOWELS:
			if spanish_mqd_double.irregular.get(lastValue) and value in ("an ", "as ", "en ", "es "):
				if irregular[lastValue].endswith("g") and value.startswith("e"):
					value = irregular[lastValue] + "u" + value
				else:
					value = irregular[lastValue] + value
			elif lastValue.endswith("ca") and (value[0] == "e" or value[0] == "é"):
				value = lastValue[:-2] + "qu" + value
			elif lastValue.endswith("ga") and (value[0] == "e" or value[0] == "é"):
				value = lastValue[:-1] + "u" + value
			else:
				value = lastValue[:-1] + value
		elif spanish_mqd_double.adjs.get(lastValue) is not None and value[:2] in ("sa", "si", "sí", "so"):
			value = adjs.get(lastValue) + value
		elif lastValue[-1] in ("e", "o", "u") and value[0] == "a":
			value = lastValue + "zc" + value
		elif lastValue.endswith("u") and value.startswith("t"):
			value = lastValue + "c" + value
		else:
			value = lastValue + value
		value = value.replace("ze", "ce")
		value = value.replace("zé", "cé")
		if not value.endswith(" "):
			value = value + "{^}"
		return value


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
	if spanish_mqd_single.dict.get(key[0]) is not None:
		value = spanish_mqd_single.dict.get(key[0])[0]
	if value == "":
		value = searchKey(spanish_mqd_single.dict, key[0])
	if value.endswith(" "):
		return value
	if value.isdigit() or value.endswith(".000"):
		return "{&" + value + "}"
	return value + "{^}"

