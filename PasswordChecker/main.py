import string
import re


print("Enter a password for evaluation: ")
password = input()


if (len(password) >= 10
    and re.search("[a-z]", password)
    and re.search("[A-Z]", password)
    and re.search("[0-9]", password)
    and re.search("[_@$£!,&*]", password)
    and not re.search("[\s]", password)):
    print("This password is strong.")
else:
    print("This password is weak.")