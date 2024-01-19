#!/usr/bin/python3
"""task 12"""


class MyInt(int):
    """class MyInt"""

    def __ne__(self, next):
        """negation to equal"""
        return super().__eq__(next)

    def __eq__(self, next):
        """equal to negation"""
        return super().__ne__(next)
