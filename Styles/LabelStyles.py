#!/usr/bin/env python
""" Provides Syling for AVKLabels

"""

from .Styles import defaults

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

AVKLabelStyles = {
	'DEFAULT': defaults['LABEL']
}

def newAVKLabelStyle(pname,
                     pfont=defaults['LABEL']['font'],
                     pfontColor=defaults['LABEL']['fontColor'],
                     pbackgroundColor=defaults['LABEL']['backgroundColor']):
	"""
	Defines a new AVKLabel style
	:param pname: Name of new style
	:param pfont: Font definition as tuple
	:param pfontColor: Color of font as hex string
	:param pbackgroundColor: Color of background as hex string
	:return: Nune
	"""
	AVKLabelStyles[pname] = {
		'font': pfont,
		'fontColor': pfontColor,
		'backgroundColor': pbackgroundColor
	}
