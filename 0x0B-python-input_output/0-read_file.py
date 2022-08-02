#!/usr/bin/python3
def read_file(filename="UTF8"):
	"""It print the content of a file"""
	with open(filename, 'r', encoding="") as f:
		content = f.read()
		print("{}".format(content))
	