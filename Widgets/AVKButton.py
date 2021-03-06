#!/usr/bin/env python
""" Provides AVKButton Widget Class

"""

from tkinter import Button
from ..Styles import AVKButtonStyles

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

class AVKButton(Button):
	def __init__(self,
	             pmaster,
	             ptext=None,
	             pcommand=None,
	             pstyle="DEFAULT"):
		"""
		Initialization Function
		:param pmaster: Master Frame
		:param ptext: Text to display on button
		:param pcommand: Command button will execute
		:param pstyle: User-defined style or default as string
		"""
		Button.__init__(self, pmaster)
		self.config(text=ptext)
		self.config(command=pcommand)

		try:
			self.avkbConfigure(AVKButtonStyles[pstyle])
		except KeyError:
			raise AVKButton.InvalidAVKButtonTypeError(pstyle)

	def avkbConfigure(self, pconfig):
		"""
		Configures style of AVKButton Based on configuration dictionary
		:param pconfig: Configuration dictionary from AVKButtonStyles
		:return: None
		"""
		self.configure(font=pconfig['font'])
		self.configure(fg=pconfig['fontColor'])
		self.configure(bg=pconfig['backgroundColor'])
		self.configure(activeforeground=pconfig['activeFontColor'])
		self.configure(activebackground=pconfig['activeBackgroundColor'])
		self.configure(relief=pconfig['relief'])

	class InvalidAVKButtonTypeError(Exception):
		def __init__(self, key):
			"""
			Initialization Function
			:param key: Key that caused error meaning this AVKButton Style doesn't exist
			"""
			Exception.__init__(self, "\nInvalid AVButton type: {0}".format(key))
