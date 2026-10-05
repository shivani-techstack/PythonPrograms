# Check whether a character is uppercase, lowercase, digit, or special character
c=input("Enter a Character:")
if c.islower():
    print(c," is a lower case")
elif c.isupper():
    print(c," is a upper case")
elif c.isdigit():
    print(c," is a digit case")
else:
    print(c," is a special case")
