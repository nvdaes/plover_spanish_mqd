LONGEST_KEY = 1

dict = {
	"SC": ("casa ", "ca", True),
	"N": ("nana", "n", False),
	"Ccn": ("camina{p}", "camin", False)
}

lastValue = ""
shouldWait = False

def isInitial(value):
	if value == "" or value.endswith("{i}") or value[0] == " ":
		return True
	return False

def isWaiting():
	if lastValue != "" and lastValue.endswith("{p}"):
		return True
	return False

def searchKey(dictionary, stroke):
	searchKey = stroke[:]
	searchKeyValue = ""
	lenSearched = 0
	value = ""
	while len(searchKey) > 0:
		if dictionary.get(searchKey) is not None:
			searchKeyValue = dictionary.get(searchKey)[1]
		if searchKeyValue == "":
			searchKey = searchKey[:len(searchKey)-1]
		else:
			value += searchKeyValue
			searchKeyValue = ""
			lenSearched += len(searchKey)
			searchKey = stroke[lenSearched:]
	return value

def lookup(key):
	global lastValue, shouldWait
	value = ""
	if dict.get(key[0]) is not None:
		if lastValue == "" or lastValue.endswith("{i}") or lastValue[-1] == " " or not dict.get(key[0])[2]:
			value = dict.get(key[0])[0] 
			if value.endswith("{p}"):
				lastValue = value[:-3]
				shouldWait = True
				return " "
		if value == "":
			value = dict.get(key[0])[1] 
	if value == "":
		value = searchKey(dict, key[0])
	if shouldWait:
		lastValue = lastValue + value
	value.replace("{i}", "")
	lastValue = value
	if value.endswith(" "):
		return value
	return value + "{^}"
