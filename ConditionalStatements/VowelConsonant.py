#Check whether a character is a vowel or consonant.
char=input("Enter a character=")
v="aeiouAeiou"
if char in v:
    print(char,"is vowel")
else:
    print(char,"is consonant")