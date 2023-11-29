'''#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)))'''
#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c != ord('e') and c != ord('q'):
        print("{:c}".format(c), end="")
