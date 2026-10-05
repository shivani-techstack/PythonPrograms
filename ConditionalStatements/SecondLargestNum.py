# Find the second largest number among three numbers.
a=2
b=7
c=1
if b<a<c or c<a<b:
    print(a,"is second largest")
elif a<b<c or c<b<a:
    print(b,"is second largest")
else:
    print(c,"is second largest")