# Count even digits in a number.
num=int(input("Enter a number:"))
count=0
while num>0:
    if num%2==0:
        count+=1
    num=num//10
print(count)


