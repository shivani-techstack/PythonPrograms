#Find the largest digit in a number.
n=input("enter a num:")
largest=0
for i in n:
    if int(i)>largest:
        largest=int(i)
print(largest)