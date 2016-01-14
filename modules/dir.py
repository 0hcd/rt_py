#!/usr/bin/python

import os

def run(**args):

	print "[*] In directory listing module."
	files = os.listdir(".")

	return str(files)


