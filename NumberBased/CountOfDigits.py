#. Count the number of digits in a number.
numbers=int(input("Enter a numbers:"))
count=0
while numbers>0:
    count+=1
    numbers=numbers//10
print(count)