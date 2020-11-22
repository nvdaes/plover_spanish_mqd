import os
import sys
UNIT_DIR = os.path.dirname(os.path.abspath(__file__))
TOP_DIR = os.path.dirname(os.path.dirname(UNIT_DIR))
SOURCE_DIR = os.path.join(TOP_DIR, "plover_spanish_mqd")
DICT_DIR = os.path.join(SOURCE_DIR, "dictionaries")
sys.path.append(DICT_DIR)
