#Check whether a number is a perfect number.
num=int(input("Enter a number:"))
original=num
total=0
for i in range(1,num):
    if num % i==0:
        total+=i
if total==original:
    print("perfect")
else:
    print("Not perfect")