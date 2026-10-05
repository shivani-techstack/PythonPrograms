#1.Print "Hello World".
a="Hello World"
print(a)

#2. Take your name as input and print it.
n=input("enter your name:")
print(n)
#3. Take two numbers and print their sum.
a=10
b=20
print(a+b)
#4. Perform addition, subtraction, multiplication, and division of two numbers.
a=6
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#5. Swap two numbers.
a=10
b=20
a,b=b,a
print("A:",a)
print("B:",b)
#6. Swap two numbers without using a third variable.
a=10
b=20
a=a+b #10+20=30
b=a-b #30-20=10
a=a-b #30-10=20
print("A:",a)
print("B:",b)
#7. Calculate the area of a circle.
r=2
area=22/7*(r**2)
print(area )
#8. Calculate the area of a rectangle.
l=5
b=6
area=l*b
print(area)
#9. Convert Celsius to Fahrenheit.
Celsius=int(input("Enter a celsius:"))
Fahrenheit=(Celsius*9/5)+32          #formula->fahrenheit=(celsius*9/5)+32
print("Fahrenheit:",Fahrenheit)
#10. Convert minutes into hours and minutes.
minutes=125
hours=minutes//60
remaining_min=minutes%60
print("Hours:",hours)
print("Minutes:",remaining_min)
#11. Find the data type of a variable.
a="shivani"
print(type(a))
#12. Demonstrate implicit type conversion.
a=10
b=10.2
c=a+b
print(c)
#13. Demonstrate explicit type conversion.

a=10
b=float(a)
print(b)
