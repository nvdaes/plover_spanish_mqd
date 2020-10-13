LONGEST_KEY = 1

dict = {
	"SC": ("casa", "ca", False),
	"N": ("nana", "n", False),
	"Ccn": ("camina{p}", "camin", False)
}

lastValue = ""

def lookup(key):
	global lastValue
	value = ""
	if "{p}" in lastValue:
        value = lastValue.replace(""{p", "")
	if dict.get(key[0]) is not None:

			value = dict.get(key[0])[0] 
		if value == "":
			value = dict.get(key[0])[1]
	if value == "":
		searchKey = key[0][:]
		searchKeyValue = ""
		lenSearched = 0
		while len(searchKey) > 0:
			if dict.get(searchKey) is not None:
				searchKeyValue = dict.get(searchKey)[1]
			if searchKeyValue == "":
				searchKey = searchKey[:len(searchKey)-1]
			else:
				value += searchKeyValue
				searchKeyValue = ""
				lenSearched += len(searchKey)
				searchKey = key[0][lenSearched:]
	if "{p}" in value:
		value.replace("{p}", "")
		lastValue = value
		return " "
	lastValue = value
	return value
