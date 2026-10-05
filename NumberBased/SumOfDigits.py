# Find the sum of digits of a number.
numbers=int(input("Enter a numbers:"))
sum=0
while numbers>0:
    sum+=numbers%10
    numbers=numbers//10
print(sum)