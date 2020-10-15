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
	"N": ("nana", "n", False),
	"*": ("{#control(BackSpace)} ", "{empty}", False)
}

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
			searchKey = searchKey[:len(searchKey)-1]
		else:
			value += searchKeyValue
			searchKeyValue = ""
			lenSearched += len(searchKey)
			searchKey = stroke[lenSearched:]
	if value == "":
		value = "{empty}"
	return value

def lookup(key):
	global lastValue
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
	if dict.get(key[0]) is not None:
		if lastValue == "" or lastValue.endswith("{i}") or lastValue[-1] == " " or not dict.get(key[0])[2]:
			value = dict.get(key[0])[0] 
		if value == "":
			value = dict.get(key[0])[1] 
	if value == "":
		value = searchKey(dict, key[0])
	lastValue = value
	value = value.replace("{i}", "")
	if value.endswith(" "):
		return value
	return value + "{^}"
