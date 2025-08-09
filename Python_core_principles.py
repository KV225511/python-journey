# print("chai aur python")

# def chai(n):
#     print(n)
    
    
# chai(5)

# takeInput=input("Write a number:")
# print(takeInput)
# internal working for python
# >>> import sys
# >>> sys.getrefcount(24601)
# 3
# >>> sys.getrefcount('hitesh')
# 3
# >>> sys.getrefcount(1)
# 4294967295
# >>> sys.getrefcount('h')
# 4294967295
# >>> sys.getrefcount('krissh')
# 3
# >>> 




# Intro to Numbers

# Operators in Python
# Arithmetic Operators
# +(plus), -(minus), *(multiply), /(divide), //(floor divide gives quotient), %(modulus gives remainder), **(exponent)
x=2
y=3
z=4
# print(x+y)
# print(x+y*z)

# print(int(23.2))
# print(float(23))
# print(x,y,z)
# print(3/2)
# print(3//2)
# print(3%2)

# print(repr('chai\n')) OUtput:"'chai\n"
# print(str('chai\n')) Output: chai

# print('chai\n') Output:chai


# import math
# print(math.floor(3.5))
# print(math.ceil(3.5))
# print(math.ceil(-3.5))
# print(math.floor(-3.4))
# print(math.trunc(-2.8)) trunc goes towards 0 basically removes the decimal part aand gives integeer closer to 0 i.e. for 2.8 it gives 2 and for -2.8 it gives -2
# print(math.trunc(2.8))
#2+1j  Complex number in python

# 0o20  octal number
# 0x20  hexadecimal number
# 0b111  binary number
# oct(64)   returns '0o100'
# hex(64)   returns '0x40'
# bin(64)   returns '0b1000000'
# int ('64',8)    # returns 52 this also does the same as octal number
# int ('64',16)   # returns 100 this also does the same as hexadecimal number
# int ('10001',2)    # returns 17 this also does the same as binary number
# x<<1 # left shift operator gives x*2
# x>>2 # right shift operator gives x/2^2=x//4


# import random
# random.random() gives a random number between 0 and 1 including 0 and 1

# random.randint(1,10)  # gives a random integer between 1 and 10 including both 1 and 10


# random.choice([1,2,3,4,5,6,7,8,9,10])  # gives a random choice from the list

# l1=[1,2,3,4,5,6,7,8,9,10]
# random.shuffle(l1)  # shuffles the list in place
# print(l1)  # prints the shuffled list

# import decimal

# print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1')-decimal.Decimal('0.3'))


# from fractions import Fraction
# myfra=Fraction(2,7)
# print(myfra)


# Sets introduction
# A set is an unordered collection of unique elements.

# setone={1,2,3,4}
# setone.add(5)
# print(setone)  # {1, 2, 3, 4, 5}


# Boolean introduction
# Boolean values are either True or False.

# print(True==1)
# print(False==0)
# print(True is 1)
# print(False is 0)


# String introduction

chai="Masala Chai"
first_char=chai[0]
# print(first_char)  # M
# print(chai[0:6])  # Masala
# print(chai[0:6:2])  # Msl
# print(chai[-1::-1])  # iahC alasaM
# print(chai[::-1])  # iahC alasaM
# print(chai[0:6:1])  # Masala
# print(chai.lower()) # masala chai
# print(chai.upper()) # MASALA CHAI
# print(chai.title()) # Masala Chai
# print(chai.replace("Masala", "Garam"))  # Garam Chai
# print(chai.split(" "))  # ['Masala', 'Chai']
# print(chai.strip()) # Masala Chai (removes leading and trailing whitespace)
# print(chai.find("Chai"))  # 7 (returns the index of the first occurrence of the substring)
# print(chai.index("Chai"))  # 7 (returns the index of the first occurrence of the substring, raises ValueError if not found)
# print(chai.count("a"))  # 3 (returns the number of occurrences of the substring)
# print(chai.startswith("Masala"))  # True (checks if the string starts with the substring)

# order="I ordered {} cups of {} chai"
# print(order.format(2, "Masala"))  # I ordered 2 cups of Masala chai
# print(order.format(3, "Garam"))  # I ordered 3 cups of Garam chai

# chai_variety=["Lemon","Masala","Ginger"]
# print(chai_variety) # ['Lemon', 'Masala', 'Ginger']
# print("".join(chai_variety))  # LemonMasalaGinger (joins the list elements into a string without any separator)
# print("-".join(chai_variety))  # Lemon-Masala-Ginger (joins the list elements into a string with '-' as separator)
# path=r"C:\Users\hitesh\Desktop\chai"  # raw string, backslashes are treated as literal characters
# print(path)  # C:\Users\hitesh\Desktop\chai
# path2="C:\\Users\\hitesh\\Desktop\\chai"  # escaped backslashes
# print(path2)  # C:\Users\hitesh\Desktop\chai


# List Introduction
# A list is an ordered collection of items that can be of different types.
# Eg
# chai_list=["Masala","Ginger","Lemon"]

# tea_varieties=["Black","Green","Oolong","White"]
# # print(tea_varieties)   # ['Black', 'Green', 'Oolong', 'White']
# # print(tea_varieties[:2]) # ['Black', 'Green'] (slicing the list to get first two elements)
# # tea_varieties[1:3]="Lemon"
# # print(tea_varieties)
# # tea_varieties[1:3]=["Ginger"]
# # print(tea_varieties)
# # tea_varieties[1:1]=["test","test2"]
# # print(tea_varieties)
# # tea_varieties[1:2]=[]
# # print(tea_varieties)

# for tea in tea_varieties:
#     print(tea,end=" ")  # Output: Black Green Oolong White (prints each element in the list with a space in between)
    
# tea_varieties.append("Chamomile")  # adds "Chamomile" to the end of the list
# print(tea_varieties)  # ['Black', 'Green', 'Oolong', 'White', 'Chamomile']
# tea_varieties.insert(2, "Jasmine")  # inserts "Jasmine" at index 2
# print(tea_varieties)  # ['Black', 'Green', 'Jasmine', 'Oolong', 'White', 'Chamomile']
# tea_varieties.remove("Green")  # removes "Green" from the list 
# tea_varieties.extend(["Mint", "Hibiscus"])  # extends the list with "Mint" and "Hibiscus"
# print(tea_varieties)  # ['Black', 'Jasmine', 'Oolong', 'White', 'Chamomile', 'Mint', 'Hibiscus']
# print(tea_varieties.pop())  # removes and returns the last element of the list
# print(tea_varieties.pop(2))  # removes and returns the element at index 2
# tea_varietiescopy=tea_varieties.copy()  # creates a shallow copy of the list
# print(tea_varietiescopy)  # ['Black', 'Jasmine', 'White', 'Chamomile', 'Mint']
# tea_varieties.sort()  # sorts the list in ascending order     
# print(tea_varieties)  # ['Black', 'Chamomile', 'Jasmine', 'Mint', 'White']
# squared_num=[x**2 for x in range(10)]  # list comprehension to create a list of squares of numbers from 0 to 9
# print(squared_num)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# even_squares=[x**2 for x in range(10) if x%2==0]  # list comprehension to create a list of squares of even numbers from 0 to 9
# print(even_squares)  # [0, 4, 16, 36, 64]



# Dictioanries introduction 
# A dictionary is an unordered collection of key-value pairs.
# chai_dict={"Masala":10,"Ginger":15,"Lemon":20}

# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# print(chai_types)

# print(chai_types["Masala"])  # Spicy (accessing the value associated with the key "Masala")

# print(chai_types.get("Ginger"))  # Zesty (using get method to access the value associated with the key "Ginger")
# print(chai_types.get("Black", "Not Found"))  # Not Found (using get method with a default value if the key is not found)


# for key in chai_types:
#     print(key, chai_types[key])  # prints each key and its associated value 

# for key,value in chai_types.items():
#     print(key, value)  # prints each key and its associated value using items() method  
    
# print("I have masala chai") if "Masala" in chai_types else print("Nothing")

# chai_types.pop("Masala")  # removes the key-value pair with key "Masala"
# print(chai_types)  # {'Ginger': 'Zesty', 'Green': 'Mild'}
# chai_types["Black"]="Strong"  # adds a new key-value pair to the dictionary
# print(chai_types)  # {'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Strong'}
# chai_types.popitem()    # removes the last inserted key-value pair from the dictionary
# print(chai_types)  # {'Ginger': 'Zesty', 'Green': 'Mild'}
# chai_types.clear()  # clears the dictionary 
# del chai_types  # deletes the dictionary
# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# chai_types_copy=chai_types.copy()  # creates a shallow copy of the dictionary
# print(chai_types_copy)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
# chai_types_copy["Black"]="Strong"  # adds a new key-value pair to the copied dictionary
# print(chai_types_copy)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Strong'}
# print(chai_types)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'} (original dictionary remains unchanged after copying)

# chai_types.update({"Chamomile":"Herbal"})  # updates the dictionary with a new key-value pair
# print(chai_types)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Chamomile': 'Herbal'}
# squared_num={x:x**2 for x in range(10)}
# print(squared_num)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# squared_num.clear()
# print(squared_num)  # {} (clears the dictionary)
# print(list(chai_types.keys()))
# print(list(chai_types.values()))  # prints the values of the dictionary
# print(list(chai_types.items()))  # prints the key-value pairs of the dictionary



# Tuples Introduction 

# A tuple is an ordered collection of items that can be of different types, similar to a list but immutable.

# tea_types=("Black","Green","Oolong","White")
# print(tea_types)    # ('Black', 'Green', 'Oolong', 'White')


# Problem Solving with Python

# 1 Age group categorization

# age= int(input("Enter your age:"))
# if (age<13):
#     print("You are classified as Child")
# elif(age<=19):
#     print("You are classified as Teenager")

# elif(age<=59):
#     print("You are classified as Adult")

# elif(age>=60):
#     print("You are classified as Senior")

# else:
#     print("Please enter the correct age")



# 2 Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


# age=int(input("Enter your age :"))
# day=input("Enter the day of the week :")
# new_day=day.lower()
# if(new_day=="wednesday"):
#     if(age<18):
#         print("Your price of the ticket is $6")
#     else:
#         print("Your price of the ticket is $10")
# else:
#     if(age<18):
#         print("Your price of the ticket is $8")
#     else:
#         print("Your price of the ticket is $12")


# 3 Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).


# score=int (input("Enter your grade:"))
# if(score<60):
#     print("Your grade is F")
# elif(score<70):
#     print("Your grade is D")
# elif(score<80):
#     print("Your grade is C")
# elif(score<90):
#     print("Your grade is B")
# else:
#     print("Your grade is A")


#4  Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)


# fruit_color=input("Enter the color of the fruit:")
# new_fruit_color=fruit_color.lower()
# match new_fruit_color:
#     case "green":
#         print("Unripe")
#     case "yellow":
#         print("Ripe")
#     case "brown":
#         print("Overripe")
#     case _:
#         print("Please enter a valid state of the fruit")


# 5 Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# weather=input("Enter the weather condition:")
# new_weather=weather.lower()
# match new_weather:
#     case "sunny":
#         print("Go for a walk")
#     case "rainy":
#         print("Read a book")
#     case "snowy":
#         print("Build a snowman")
#     case _ :
#         print("Please enter a valid weather condition")


# 6 Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

# distance=float(input("Enter the distance in km:"))
# if(distance<3 and distance>0 ):
#         print("Walk")
# elif(distance<+15 and distance ):
#         print("Bike")
# elif(distance>15 and distance ):
#         print("Car")


# 7 Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

# size_of_drink=input("Enter the size of the drink (Small, Medium, Large):")
# shot=input("Do you want an extra shot of espresso? (yes/no):")
# new_shot=shot.lower()
# new_size_of_drink=size_of_drink.lower()
# if new_shot == "yes":
#     match new_size_of_drink:
#         case "small":
#             print("You have ordered a Small drink with an extra shot of espresso")
#         case "medium":
#             print("You have ordered a Medium drink with an extra shot of espresso")
#         case "large":
#             print("You have ordered a Large drink with an extra shot of espresso")
#         case _:
#             print("Please enter a valid size of the drink")
# else:
#     match new_size_of_drink:
#         case "small":
#             print("You have ordered a Small drink")
#         case "medium":
#             print("You have ordered a Medium drink")
#         case "large":
#             print("You have ordered a Large drink")
#         case _:
#             print("Please enter a valid size of the drink")



# 8 Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

# password=input("Enter your password:")
# if len(password)<6:
#     print("Your password is Weak")
# elif len(password)<=10:
#     print("Your password is Medium")
# else:
#     print("Your password is Strong")


#9  Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).


# year=int(input("Enter the year:"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("The year is a leap year")
# else:
#     print("The year is not a leap year")

# 10 Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# species = input("Enter the pet's species (Dog/Cat): ")
# age = int(input("Enter the pet's age in years: "))

# if species.lower() == "dog":
#     if age < 2:
#         print("Recommended food: Puppy food")
#     else:
#         print("Recommended food: Adult dog food")
# elif species.lower() == "cat":
#     if age > 5:
#         print("Recommended food: Senior cat food")
#     else:
#         print("Recommended food: Adult cat food")
# else:
#     print("Unknown species")

# Loops Exercise

#  1 Given a list of numbers, count how many are positive.


# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# count=0
# for i in numbers:
#     if(i>0):
#         count+=1
# print("The count of positive numbers is:", count)  # Output: The count of positive numbers is: 6



# 2 Calculate the sum of even numbers up to a given number n.

# n=int(input("Enter the number till where you want to calculate the sum of even numbers: "))

# sum_of_even=0
# for i in range(0,n+1,2):
#     sum_of_even+=i
# print("The sum of even numbers up to", n, "is:", sum_of_even)  # Output: The sum of even numbers up to n is: sum_of_even


# 3  Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# number=int(input("Enter the number fopr which table has to be printed:"))


# for i in range(1,11):
#     if(i==5):
#         continue
#     else:
#         print(f"{number} * {i} = {number*i}")


# 4  Reverse a string using a loop

# string=input("Enter the string:")
# new_string=""
# for i in range(-1,-len(string)-1,-1):
#     new_string+=string[i]

# print(new_string)


# 5 Given a string, find the first non-repeated character.


# string=input("Enter the string: ")
# non_repeated_list=[]
# for i in range(len(string)):
#     count=0
#     for j in range(len(string)):
#         if(i==j):
#             continue
#         elif(string[i]==string[j]):
#             count+=1
#     if(count==0):
#         non_repeated_list.append(string[i])

# print(non_repeated_list[0])
# print(non_repeated_list)


# 6 Compute the factorial of a number using a while loop.


# number= int(input("Enter the number for which factorial is to be made:"))
# fac=1
# i=1
# while(i<=number):
#     fac*=i
#     i+=1
    
# print(fac)

# 7 Keep asking the user for input until they enter a number between 1 and 10.


# number=int(input("Enter a number: "))

# while (number not in range(1,11)):
#     number=int(input("Enter the number"))
# print(number)



# 8 Check if a number is prime.



# num=int(input("Enter the number:"))
# count=0
# if num<=1:
    # print(f"{num}is not a prime number")
# for i in range(2,int(num/2)+1):
#     if(num==2):
#         print(f"{num} is a prime number")
#     if(num%i==0): 
#         count=1
#         break

# if(count==0):
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not a prime number")


# 9 .Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.


# items=["apple","banana","orange","apple","mango"]
# duplicate_items=[]
# for i in range(len(items)):
#     count=0
#     for j in range(len(items)):
#         if(j==i):
#             continue
#         elif(items[i]==items[j]):
#            count+=1
#     if(count>0 and items[i] not in duplicate_items ):
#         duplicate_items.append(items[i]) 

# print(duplicate_items)


# 10 Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

# import time
# print("Attempt 1: ")
# count=1
# i=1
# while (count<5):
#     count+=1
#     time.sleep(i)
#     print(f"Attempt {count}: ")
#     i*=2

# Functions introduction

# 1 Write a function to calculate and return the square of a number


# def square(num):
#     return num*num

# print(square(5))



# 2  Create a function that takes two numbers as parameters and returns their sum.



# def sum(num1,num2):
#     return num1+num2

# print(sum(5,10))



# 3 Write a function multiply that multiplies two numbers, but can also accept and multiply strings.


# def polymophic_function(val1,val2):
#     type1=type(val1)
#     type2=type(val2)
#     if(type1==str and type2==str):
#         return "Invalid operation cannot multiply 2 strings"
#     else:
#         return val1*val2
    
# print(polymophic_function("sting","rdj"))


# 4 Create a function that returns both the area and circumference of a circle given its radius.


# def circle():
#     return 240,300

# print(circle())


# 5 Write a function that greets a user. If no name is provided, it should greet with a default name.


# def greeting(user="Krissh"):
#     return f"Nice to see you {user}"

# print(greeting("vansh"))
# print(greeting())


# 6  Create a lambda function to compute the cube of a number.

# cube=lambda x:x**3

# print(cube(3))


# 7 Write a function that takes variable number of arguments and returns their sum.

# def sum_all(*args):
#     print(args) #gives a tuple as args=(1,2,3,4,5,6)
#     sum=0
#     for i in args:
#         sum+=i
#     return sum

# print(sum_all(1,2,3,4,5,6))


# 8 Create a function that accepts any number of keyword arguments and prints them in the format key: value.


# def dictionary(**kwargs):
#     for key in kwargs.keys():
#         print(key," : ",kwargs[key])
    
    
# dictionary(name_1="hi",bye=2)



# 9 Write a generator function that yields even numbers up to a specified limit.


# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i


# for num in even_generator(10):
#     print(num)
        


# 10 Create a recursive function to calculate the factorial of a number.
# fac=1
# def factorial(num):
#     global fac
#     if(num==1):
#         return fac
#     else:
#         fac*=num
#         num-=1
#         return factorial(num)
# print(factorial(5))
        
        
# def factorial(num):
#     if(num==1):
#         return 1
#     else:
#         return num*factorial(num-1)
    
# print(factorial(5))
    
    
# Closure and Scopes

# there is a rule called as  LEGB RULE (Local Enclosing Global Built-in .In python the elements can be accessed from global scope but we cannot change the value inside the local scope of the global variable we have to use a specific keyword named 'global' that is used like 'global x' to tell python that i am trying to access the global 'x' and not creating another local variable)

# for Eg

# global scope

# x=99

# def function():
#     local scope
#     x=88
#     def func2():
#         enclosing scope
#         print(x)
#     return func2()

# function()

# here in the above example as you can see the whole file is considerred as global scope and the function is considerred as local scope while the function made inside the local scope is considerred as the enclosing scope 

# so we can access the variables from the variables in the locasl scope form the enclosing scope and use and change there value but in the case of global scope we need to specify with the global keyword


# eg 

# x=99
# def func1():
#     x=88
#     def func2():
#         x=x+2  this gives error as we cannot change the value of outer scope we  can only use it
#         print(z)
#     func2()
#     print(x)

# func1()   


# Eg for closure
 
# x=99
# def func1():
#     x=88
#     def func2():
#         z=x+2
#         print(z)
#     return func2

# print(func1())    



# def chaicoder(num):
#     def actual(x):
#         return x ** num
#     return actual



# f = chaicoder(2)
# g = chaicoder(3)

# print(f(3))
# print(g(3))


# Object oriented programming

# class Car:
#     total_car=0
#     def __init__(self,userbrand,usermodel):
#         self.__brand=userbrand
#         self.__model=usermodel
#         Car.total_car+=1
#     def get_brand(self):
#         return self.__brand
#     def full_name(self):
#         return (f"The car is: {self.__brand} {self.__model}")
#     def fuel_type(self):
#         return "Petrol or diesel"
#     @staticmethod
#     def general_description():
#         return "Cars are means of transport"
#     @property
#     def model(self):
#         return self.__model

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size
#     def fuel_type(self):
#         return "Electricity"
    
# class Battery(ElectricCar):
#     def battery_info(self):
#         return "This is battery"
# class Engine(ElectricCar):
#     def engine_info(self):
#         return "This is engine"
    

# class ElectricCar2(Battery,Engine,Car):
#     pass

# corolla=Car("Toyota","Corolla")
# # print(corolla.full_name())
# # print(corolla.fuel_type())
# nexon=Car("Tata","nexon")
# # print(nexon.full_name())
# # print(nexon.fuel_type())

# my_tesla=ElectricCar("Tesla","Model S","85Kwh")
# # print(my_tesla.full_name())
# # print(my_tesla.fuel_type())
# # print(Car.total_car)
# # # print(my_tesla.general_description())
# # print(Car.general_description())

# # print(isinstance(my_tesla,Car))
# # print(isinstance(my_tesla,ElectricCar))

# my_new_tesla=ElectricCar2("Tesla","Model s","85Kwh")
# print(my_new_tesla.battery_info())
# print(my_new_tesla.engine_info())



# Into to Decorator
# 1
# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result=func(*args,**kwargs)
#         end=time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)



# 2

# def function_print(func):
#     def wrapper(*args,**kwargs):
#         args_value=", ".join(str(arg) for arg in args)
#         kwargs_value=", ".join(f"{k}={v}" for k,v in kwargs.items())
        
#         result=func(*args,**kwargs)
#         print(f"{func.__name__} returned {result} with arguments {args_value} {kwargs_value}")
#     return wrapper
    
    
    
# @function_print    
# def greet(name,greeting="Hello"):
#     return(f"{greeting}, {name}")
    
# greet("chai",greeting="hanji ")



# 3
# import time

# def cache(func):
#     cache_value={}
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result=func(*args)
#         cache_value[args]=result
#         print(cache_value)
#         return result
#     return wrapper


# @cache
# def long_running_function(a,b):
#     time.sleep(4)
#     return a+b

# print(long_running_function(2,3))
# print(long_running_function(2,3))
# print(long_running_function(4,6))


# File handling

# x=('Masala','Lemon','Ginger')
# y=enumerate(x)
# print(list(y))


# file=open('text.py','w')
# try:
#     file.write("chai aur code")
    
# finally:
#     file.close()
    
# with open('youtube.txt','w') as f:
#     f.write("Chai aur python")