#Program:1
#def add(a,b):
    #print (a+b)
#a=int(input("Enter first number:"))
#b=int(input("Enter second number:"))
#add (10,20)

#Program:2
#a =int(input("Enter a number:"))
#if (a%2==0):
#    print("Even number")
#else:
#    print("Odd number")

#Program: 3
#def greet(name):
#    print("hello",name)
#name = input("Enter name:")
#greet(name)

#Program: 4
#def largest(a,b):
#    if (a>b):
#    return a
 #   else:
 #    return b
#a=int(input("Enter first number:"))
#b=int(input("Enter second number:"))
#result=largest(a,b)
#print("Largest number:",result)

#Program: 5
#def average(a,b,c):
#    return(a+b+c)/3
#a=int(input("Enter first number:"))
#b=int(input("Enter second number:"))
#c=int(input("Enter third number:"))
#result = average(a,b,c)
#print("Average:",result)

#Program: 6
#Employees = ["Ashwin","Silambarasan","STR","Atman"]
#for name in Employees:
#    print(name)

#Program: 7
#Employees = ["Ashwin","Silambarasan","STR","Atman"]
#Employees.append("Simbu")
#print(Employees)

#Program: 8
#Employees = ["Ashwin","Silambarasan","STR","Atman"]
#Employees.remove("Ashwin")
#print(Employees)

#Program: 9
#numbers = [20,30,40,50,60,70,80]
#largest =max(numbers)
#print ("Largest number is:", largest)

#Program: 10
#list = [10,15,20,25]
#count=0
#for list in list:
#    if list%2==0:
#        count=count+1
#print("The even number is:",count)

#Program: 11
#student={
#    "name":"Uday",
#    "age":25,
 #   "mark":85
#}
#print("name:",student["name"])
#print("Age:",student["age"])
#print("mark:",student["mark"])

#Program: 12
#student={
#    "name":"Uday",
#    "age":25,
#    "mark":85
#}
#student["city"]="Coimbatore"
#print(student)

#Program: 13
#student={
#    "name":"Uday",
#    "age":25,
 #   "mark":85
#}
#student["mark"]=100
#print(student)

#Program: 14
#class Car:
  #def __init__(self, brand, model, year):
    #self.brand=brand
    #self.model=model
    #self.year=year
#car1=Car("Toyota","innova",2023)
#car2=Car("Hyundai","i20",2024)
#print(car1.brand,car1.model,car1.year)
#print(car2.brand,car2.model,car2.year)

#Program: 15
class Employee:
    def __init__(self,name,salary):
self.name=name
        self.salary=salary
    def display(self):
       print("Name:",self.name)
        print("salary:",self.salary)
employee1=Employee("Ashwin",40000)
employee1.display()


    
