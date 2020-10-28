'''
Functionality to repeat output in Plover.
'''

from typing import List

from plover.translation import Translation
from plover.formatting import _Context, _Action



def initial(context: _Context, args: str) -> _Action:
	'''
	Meta to repeat the last translation(s) in Plover.

	:param context: The context of actions in Plover.
	:param args: Optional arguments provided to the meta as a comma-delimited string.
				 Piece 1: The number of previous translations to repeat. Default is 1.

	:return: The next action for Plover to perform.
	'''

	# Process input
	output = ''
	translations: List[Translation] = context.previous_translations[-1:]
	for translation in translations:
		actions: List[_Action] = reversed(translation.formatting)
		for action in actions:
			output = output + action.text

	# Create the new action
	action: _Action = context.new_action()
	action.text = output[-1]

	return action
