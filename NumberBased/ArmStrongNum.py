#Print all Armstrong numbers between 1 and 1000.
for num in range(1,1001):
    original=num
    total=0
    digits=len(str(num))
    while num>0:
        digit=num%10
        total=total+digit ** digits
        num=num//10
    if total==original:
        print(original)