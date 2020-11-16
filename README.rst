Spanish support for Plover
##########################

*	Authors: Sonsoles García Martín, Noelia Ruiz Martínez

Plover support for Melani system in Spanish, used at MQD.

Based on this `template <https://github.com/benoit-pierre/plover_template_system>`_

API
***

API can be manipulated via `Python dictionaries <https://github.com/benoit-pierre/plover_python_dictionary>`_

For example:

# single.py
from plover_spanish_mqd.dictionaries import spanish_mqd_single

LONGEST_KEY = spanish_mqd_single.LONGEST_KEY


dict = {
	"STROKe": ("translationIfPresedAlone", "translationMayBeSubsetOfWiderStroke"),
	"N": ("en ", "n"),
	"A": ("", "a"),
	"a": ("", "a ")
}

spanish_mqd_single.dict = dict


def lookup(key):
	return spanish_mqd_single.lookup(key)

Dependencies
************

* `Plover Python dictionary <https://github.com/benoit-pierre/plover_python_dictionary>`_
* `Plover Start words <https://github.com/nvdaes/plover_start_words>`_

Versioning
**********

We use `SemVer <https://semver.org/>`_
