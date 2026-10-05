#Check whether a number belongs to the Fibonacci series.
num=int(input("Enter a number:"))
a=0
b=1
while a<num:
    c=a+b
    a=b
    b=c
if a==num:
    print("Yes")
else:
    print("No")
