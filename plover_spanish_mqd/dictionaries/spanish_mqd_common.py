LONGEST_KEY = 1

PAUSE_COMMAND = "{p}"
SPACE_COMMAND = "{i}"
VOWELS = ("a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú")

lastValue = ""

def reverseSearch(dictionary, indexedKey):
	value = ""
	if dictionary.get(indexedKey) is not None:
		value = dictionary.get(indexedKey)[1]
	if value == "":
		searchKey = indexedKey[:-1]
		searchKeyValue = ""
		while len(searchKey) > 0:
			if dictionary.get(searchKey) is not None:
				searchKeyValue = dictionary.get(searchKey)[1]
			if searchKeyValue == "":
				searchKey = searchKey[:len(searchKey)-1]
			else:
				value += searchKeyValue
				searchKeyValue = ""
				searchKey = key[len(searchKey):]
	return value

def isInitial(text=lastValue):
	if lastValue == "" or SPACE_COMMAND in lastValue or lastValue.endswith(" "):
		return True
	return False

def removeCommands(text):
	return text.replace(PAUSE_COMMAND, "").replace(SPACE_COMMAND, "")

def lookup(key):
	return " "
