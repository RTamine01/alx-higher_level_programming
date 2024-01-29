#!/usr/bin/python3
""" a function that writes to a text file
"""

def write_file(filename="", text=""):
with open(filename, "w", encoding='utf-_') as f:
return f.write(text)
