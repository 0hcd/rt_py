#!/usr/bin/python

import os


def run(**args):

	with open('/etc/passwd', 'r') as f:
		rd = f.read()
		f.close()

	return str(rd)
