#!/usr/bin/env python
""" Provides AVKLabel Widget Class
"""

from tkinter import Label
from Styles import AVKLabelStyles

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

class AVKLabel(Label):
	def __init__(self,
	             pmaster,
	             ptext=None,
	             pstyle="DEFAULT"):
		Label.__init__(self, pmaster)
		self.config(text=ptext)

		try:
			self.avklConfigure(AVKLabelStyles[pstyle])
		except KeyError:
			raise AVKLabel.InvalidAVKLabelTypeError(pstyle)

	def avklConfigure(self, pconfig):
		self.config(font=pconfig['font'])
		self.config(fg=pconfig['fontColor'])
		self.config(bg=pconfig['backgroundColor'])

	class InvalidAVKLabelTypeError(Exception):
		def __init__(self, key):
			Exception.__init__(self, "\nInvalid AVKButton type: {0}".format(key))
