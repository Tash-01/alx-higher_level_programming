#!/usr/bin/python3
for character in range(97, 123):
    if (character != 'q' and character != 'e'):
        print("{:chr}".format(character), end="")
