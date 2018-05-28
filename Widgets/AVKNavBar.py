#!/usr/bin/env python
""" Provides AVKNavBar Class

"""

from tkinter import Frame
from ..Styles import AVKNavBarStyles
from .AVKButton import AVKButton
from .AVKLabel import AVKLabel

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

class AVKNavBar(Frame):
	def __init__(self,
	             pmaster,
	             pname,
	             pbackButtonInfo=None,
	             pnextButtonInfo=None,
	             pstyle="DEFAULT"):
		"""
		Initialization Function
		:param pmaster: Master frame
		:param pname: Text to display on navbar
		:param pbackButtonInfo: Dict with TEXT and COMMAND
		:param pnextButtonInfo: Dict with TEXT and COMMAND
		:param pstyle: User-defined style or default as string
		"""
		Frame.__init__(self, pmaster)
		self.B_BackButton = None
		self.B_NextButton = None
		self.L_TitleLabel = AVKLabel(self,
		                             ptext=pname,
		                             pstyle=AVKNavBarStyles[pstyle]['titleLabelStyle'])

		if pbackButtonInfo is not None:
			self.B_BackButton = AVKButton(self,
			                              ptext=pbackButtonInfo['TEXT'],
			                              pcommand=pbackButtonInfo['COMMAND'],
			                              pstyle=AVKNavBarStyles[pstyle]['backButtonStlye'])

		if pnextButtonInfo is not None:
			self.B_NextButton = AVKButton(self,
			                              ptext=pnextButtonInfo['TEXT'],
			                              pcommand=pbackButtonInfo['COMMAND'],
			                              pstyle=AVKNavBarStyles[pstyle]['nextButtonStlye'])

