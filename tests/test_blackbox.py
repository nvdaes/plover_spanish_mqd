import functools

from plover.dictionary.base import load_dictionary
from plover.registry import registry
from plover import system
from plover import log

from plover_spanish_mqd.system import DICTIONARIES_ROOT

from plover_build_utils import testing as plover_testing


def with_pydicts(fn):

	@functools.wraps(fn)
	def wrapper(bb, *args, **kwargs):
		py_dict = load_dictionary(DICTIONARIES_ROOT + '/spanish_mqd.py')
		bb.dictionary.set_dicts(bb.dictionary.dicts + [py_dict])
		fn(bb, *args, **kwargs)

	return wrapper


def blackbox_test(cls):

	class wrapper(cls):
		pass

	for name in dir(wrapper):
		if name.startswith('test_'):
			fn = getattr(wrapper, name)
			new_fn = with_pydicts(fn)
			setattr(wrapper, name, new_fn)

	return plover_testing.blackbox_test(wrapper)


@blackbox_test
class TestsBlackbox:

	@classmethod
	def setup_class(cls):
		log.set_level(log.WARNING)
		registry.update()
		system.setup('Spanish MQD')

	def test_regular_1(self):
		r'''
		"*": "=undo",

		Ccn	' camin'
		PTVa	' caminaba'
		*	' camin'
		A*	' caminá'
		'''

	def test_regular_2(self):
		r'''
		"*": "=undo",

		PCVRcs	' lleg'
		PTVAneo	' llegaban'
		*	' lleg'
		Eneo	' lleguen'
		'''

	def test_regular_3(self):
		r'''
		"*": "=undo",

		PCNct	' averig'
		PTVAneo	' averiguaban'
		*	' averig'
		Eneo	' averigüen'
		'''

	def test_regular_4(self):
		r'''
		"*": "=undo",

		Cctn	' indi'
		PTVAneo	' indicaban'
		*	' indi'
		Eneo	' indiquen'
		'''

	def test_irregular_1(self):
		r'''
		"*": "=undo",

		PCTcs	' ju'
		TNo	' jugado'
		*	' ju'
		Eneo	' jueguen'
		'''

	def test_irregular_2(self):
		r'''
		"*": "=undo",

		CNVRctn	' rec'
		TNo	' recordado'
		*	' rec'
		Esnreo	' recordemos'
		*	' rec'
		Eneo	' recuerden'
		'''

	def test_irregular_3(self):
		r'''
		"*": "=undo",

		CNc	' cono'
		A*	' conozcá'
		*	' cono'
		CItna	' conocida'
		'''

	def test_irregular_4(self):
		r'''
		"*": "=undo",

		PRc	' produ'
		A*	' produzcá'
		*	' produ'
		Tcta	' productiva'
		'''

	def test_adj(self):
		r'''
		"*": "=undo",
		
		PCRn	' gener'
		SI	' generosi'
		*	 ' gener'
		PTVa	' generaba'
		'''
