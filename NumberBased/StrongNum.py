# Check whether a number is a strong number
num=int(input("Enter a number:"))
original=num
total=0
while num >0:
    digit=num%10
    factorial=1
    for i in range(1,digit+1):
        factorial=factorial*i
    total+=factorial
    num=num//10
if total==original:
    print("strong")
else:
    print("not strong")