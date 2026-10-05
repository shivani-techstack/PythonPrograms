#Find the nth  Fibonacci series.
num=int(input("Enter a number:"))
a=0
b=1
for i in range(num-1):
   
    c=a+b
    a=b
    b=c
print(a)