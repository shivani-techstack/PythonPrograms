# Check whether a number is a strong number
num=int(input("Enter a number:"))
while num>1:
    if num%2==0:
        print("not prime")
        break
    else:
        print("prime")
        break
