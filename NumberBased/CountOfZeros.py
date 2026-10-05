#Count zeros in a number.
n=int(input("enter a number:"))
count=0
if n==0:
    count=1
while n>0:
    if n%10==0:
        count+=1
    n=n//10
print(count)