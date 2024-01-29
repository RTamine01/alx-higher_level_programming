#!/usr/bin/python3
""" a function that writes to a text file
"""

def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    f.close()
    return len(text)
