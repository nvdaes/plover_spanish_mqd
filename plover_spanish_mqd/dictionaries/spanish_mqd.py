from plover_spanish_mqd import (
	spanish_mqd_double as double,
	spanish_mqd_single as single,
)


single.lastValue = ''

DICTIONARIES = [double, single]

LONGEST_KEY = max(d.LONGEST_KEY for d in DICTIONARIES)

def lookup(key):
	for d in DICTIONARIES:
		if len(key) > d.LONGEST_KEY:
			continue
		try:
			return d.lookup(key)
		except KeyError:
			pass
	raise KeyError
