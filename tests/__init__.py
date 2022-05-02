import os
import sys

UNIT_DIR = os.path.dirname(os.path.abspath(__file__))
TOP_DIR = os.path.dirname(os.path.dirname(UNIT_DIR))
SOURCE_DIR = os.path.join(TOP_DIR, "plover_spanish_mqd")
DICT_DIR = os.path.join(SOURCE_DIR, "dictionaries")
sys.path.append(DICT_DIR)


def detectDuplicateKeys(orderedPairs):
	d = {}
	duplicateKeys = []
	for k, v in orderedPairs:
		if k in d:
			duplicateKeys.append(k)
		else:
			d[k] = v
	if len(duplicateKeys):
		raise ValueError("\n".join(duplicateKeys))
	return d
