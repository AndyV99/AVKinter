#!/usr/bin/env python
""" Provides Syling for AVKLabels

"""

from Styles import defaults

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

AVKLabelStyles = {
	'DEFAULT': defaults['LABEL']
}

def newAVKLabelStyle(pname,
                     pfont=defaults['font'],
                     pfontColor=defaults['fontColor'],
                     pbackgroundColor=defaults['backgroundColor']):
	AVKLabelStyles[pname] = {
		'font': pfont,
		'fontColor': pfontColor,
		'backgroundColor': pbackgroundColor
	}
