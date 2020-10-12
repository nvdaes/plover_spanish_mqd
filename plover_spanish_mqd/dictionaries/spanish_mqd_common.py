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

def markedAsInitial():
	if lastValue.endswith("{i}"):
		return True
	return False
