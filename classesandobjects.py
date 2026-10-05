# 1->Create a Student class with:
#name
#age
#marks
#Create one object and print all the details

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Marks=",self.marks)
s=Student("Shivani",23,55)
s.display()

# 2->Create a Mobile class with:
#brand
#model
#price
#Create two objects and display their details.

class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("Brand=",self.brand)
        print("Model=",self.model)
        print("Price=",self.price)
m1=Mobile("samsung","A14",20000)
m2=Mobile("Vivo","Y22",30000)
m1.display()
m2.display()

# 3->Create a Car class with:
#brand
#color
#price
#Create three car objects and print their details.
class Car:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
    def display(self):
        print("Brand=",self.brand)
        print("Color=",self.color)
        print("Price=",self.price)
car1=Car("Swift","white",500000)
car2=Car("Honda","Black",650000)
car3=Car("Tata","Red",550000)
car1.display()
car2.display()
car3.display()

# 4->Create an Employee class with:
#name
#salary
#Create two employees and display their information.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name=",self.name)
        print("Salary=",self.salary)
emp1=Employee("Shivani",100000)
emp2=Employee("Santhosh",100000)
emp1.display()
emp2.display()
