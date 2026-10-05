#Find the first digit of a number.
num=int(input("enter a num:"))
digit=0
while num>0:
    digit=num%10
    num=num//10
print("First digit=",digit)