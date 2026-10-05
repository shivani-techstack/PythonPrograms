#Check whether a number is an Armstrong number.
num=int(input("Enter a number:"))
original=num
total=0
digits=len(str(num))
while num>0:
    digit=num%10
    total=total+digit ** digits
    num=num//10
if total==original:
    print("Armstrong")
else:
    print("Not Armstrong")
