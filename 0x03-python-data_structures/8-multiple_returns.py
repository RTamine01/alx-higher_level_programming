#!/usr/bin/python
def multiple_returns(sentence):
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
