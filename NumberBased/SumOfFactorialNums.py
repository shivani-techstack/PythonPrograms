#Find the sum of factorials from 1 to n.
num=int(input("Enter a number:"))
fact=1
sum=0
for i in range(1,num+1):
    fact=fact*i
    sum+=fact
print(sum)