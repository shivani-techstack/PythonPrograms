#Count the numbers from 1 to n.
n=int(input("Enter a num:"))
count=0
for i in range(1,n+1):
    i=i//10
    count+=1
print(count)