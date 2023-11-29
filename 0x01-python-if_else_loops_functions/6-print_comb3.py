#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 10):
        print("{:02d}, {:02d}".format(tens, ones), end="")
        if ones < 9:
            print(", ", end="")
        else:
            print()
