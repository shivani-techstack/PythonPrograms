# Check whether three sides can form a triangle
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
if a+b>c and a+c>b and b+c>a:
    print("The sides can form a triangle")
else:
     print("The sides cannot form a triangle")
