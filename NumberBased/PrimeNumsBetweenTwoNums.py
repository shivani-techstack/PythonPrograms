#Count prime numbers between two given numbers.
num1=int(input("Enter first number:"))
num2=int(input('enter a second number:'))
count=0
for i in range(num1,num2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count+=1
print(count)