#!/usr/bin/env python
""" Provides AVKNavBar Class

"""

from tkinter import Frame

__author__ = "Andrew Vorndran"
__copyright__ = "Copyright 2018, Andrew Vorndran"
__version__ = "0.1.0"
__maintainer__ = "Andrew Vorndran"
__email__ = "andvornd@iu.edu"

class AVKNavBar(Frame):
	def __init__(self,
	             pmaster,
	             pname,
	             pbackButtonText=None,
	             pbackButtonCommand=None,
	             pnextButtonText=None,
	             pnextButtonCommand=None,
	             pstyle="DEFAULT"):
		Frame.__init__(self, pmaster)

