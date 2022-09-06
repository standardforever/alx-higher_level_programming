#!/usr/bin/python3
def read_file(filename=""):
	"""It print the content of a file"""
	with open(filename, encoding="UTF8") as f:
		content = f.read()
		print("{}".format(content))
	