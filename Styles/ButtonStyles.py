#!/usr/bin/env python
""" Provides Styling for AVKButtons

"""

from Styles import defaults

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

AVKButtonStyles = {
	'DEFAULT': defaults,
}

def newAVKButtonStyle(pname,
                      pfont=defaults['font'],
                      pfontColor=defaults['fontColor'],
                      pbackgroundColor=defaults['backgroundColor'],
                      pactiveFontColor=defaults['activeFontColor'],
                      pactiveBackgroundColor=defaults['activeBackgroundColor'],
                      prelief=defaults['relief']):
	AVKButtonStyles[pname] = {
		'font': pfont,
		'fontColor': pfontColor,
		'backgroundColor': pbackgroundColor,
		'activeFontColor': pactiveFontColor,
		'activeBackgroundColor': pactiveBackgroundColor,
		'relief': prelief
	}
