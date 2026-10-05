# Find the product of digits of a number.
n=input("enter a num:")
product=1
for i in n:
    product=product*int(i)
print(product)