#!/usr/bin/python3
def write_string(string=""):
    for c in string:
        for i in range(ord(c)):
            print("+", end="")
        if c != "\n":
            print(".>")
        else:
            print(".")

write_string
