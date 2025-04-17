# OOPS IN PYTHON

# 1. Basic of OOP
# 2. Types of variables and methods.
# 3. Inheritance 
# 4. Polymorphism
# 5. Encapsulation
# 6. Abstraction
# 7. Interface
# 8. Mini Project OOPS
# 9. Interview Preparation

# Programming Paradigms  

# Ways of organizing programs.  
# Python supports multiple paradigms. These are as follows:-  
  
# 1) Procedural oriented paradigm    -- Line by Line Exceultion of Code
  
# 2) Functional oriented paradigm  -- Calling 
  
# 3) Object-oriented paradigm  -- real life examples we solved

# object

# An object in OOP represents real-life objects.
# ex. Email, man, student, employee etc

# Every object has two properties.

# 1) attributes
# 2) Behaviours

# Attributes:- heading, subject, name, recipients list -- data
# Behaviours:- sending, Adding attachments

# employee attributes are email id, Name
# behaviours means employee getting bonus

# What is Object-Oriented Programming (OOP) ?

# Object-oriented programming is an approach of writing programs by creating classes and objects.
# More focus is on data rather than logic.


# Why OOP

# To solve real-world problems/effectively.

# OOP provides some features :-

# 1) Inheritance :- reusability
# 2) encapsulation :- data security
# 3) abstraction :- Data hiding


# What is class?

# Class is a template/blueprint/prototype for creating objects

# Object is real life entity

# Every object belong to same class
    
# Email class
#     email1 + email2 + email3    -- object

# What is class?

# Class is a collection of attribute and methods.

# class is a collection of objects.

# Technically class is a user defined data type.

# attributes:-
# heading
# participants
# attachments

# methods:-

# send()
# save_as_draft()

# Email1:-

# heading:- taking leave
# participant:- xyz
# attachments:- form.pdf

# Email2:-
# heading:- require help
# participant:- abc
# attachments:- pic.jpg

# All 14 data types are built in data types

# x = 100

# print(type(x)) -- class -- int


# def demo():
#     print("hello")

# print(type(demo))  -- class -- function -- bulit in function

# employee, student this we will create own its called user defined function.

# Creating Class and Objects ?

# class Class_name:
#     #attributes
#     #methods

# obj1 = Class_name([args])
# obj2 = Class_name([args])

# class Email:  # Class -- User defined data type
#     pass

# e1 = Email() # Object1
# e2 = Email() # Object2

# print(type(e1))
# print(type(e2))

# # Constructor and types of Constructor

# class Employee:
#     def __init__(self):  #Special method or magic method
#         self.salary=2000
#         self.age=21

# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)

# What is constructor?

# Special method used for initializing objects with attributes
# It is __init__ method
# First arguments is self.

# Types of constructor?

# Parameterized constructor
# Non-Parameterized constructor
# Default Constructor


# class Employee:
#     def __init__(self,sal,ag):  # Special method or magic method
#         self.salary=sal         # Parameterized constructor
#         self.age=ag 

# e1 = Employee(24000,21)
# e2 = Employee(26000,26)
# print(e1.__dict__)



# class Employee:
#    pass

# e1 = Employee()   # Default Constructor
# e2 = Employee()
# print(e1.__dict__)

# # without constructor: object cannot be created

# ----------------------------------------------------

# class Employee:
#     def __init__(self,sal,ag):  # Special method or magic method
#         self.salary=sal         # Parameterized constructor
#         self.age=ag 

# e1 = Employee(24000,21)
# e2 = Employee(26000,26)

# 1. Memory allocation for object
# 2. memory reference returned to the object
# 3. memory reference automatically passed inside constructor
# 4. constructor creates/initialize variables at that memory reference.

# What is self?
# self is a variable in that memory address of current object


# Accessing Class Members Outside the Class

# class Employee:
#     def __init__(self,sal,ag):  # Special method or magic method
#         self.salary=sal         # Parameterized constructor
#         self.age=ag 

#     def display(self):
#         print(f"salary is {self.salary} and age is {self.age}")

# e1 = Employee(24000,21)
# e2 = Employee(26000,26)

# # accessing attribute outside the class

# print(e1.salary) # 24000
# e1.salary = 34000 # updating attribute
# print(e1.salary) # 

# e2.display() 
