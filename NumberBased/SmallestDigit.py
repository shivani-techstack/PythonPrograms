# Find the smallest digit in a number.
n=input("enter a num:")
smallest=9
for i in n:
    if smallest>int(i):
        smallest=int(i)
print(smallest)