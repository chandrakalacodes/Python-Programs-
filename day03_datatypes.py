# =====================================================================================
# DAY 3 - DATA TYPES IN PYTHON
# =====================================================================================
# ========== Program 1: Integer Data Type==========
num = 100

print("Value:", num)
print("Data Type:", type(num))
print("\n")

# OUTPUT:
# Value: 100
# Data Type: <class 'int'>

# ==========Program 2: Float Data Type==========
percentage = 89.75

print("Percentage:", percentage)
print("Data Type:", type(percentage))
print("\n")

# OUTPUT:
# Percentage: 89.75
# Data Type: <class 'float'>

# ==========Program 3: Complex Data Type==========
number = 4 + 7j

print("Complex Number:", number)
print("Data Type:", type(number))
print("\n")

# OUTPUT:
# Complex Number: (4+7j)
# Data Type: <class 'complex'>

# ==========Program 4: String Data Type==========
name = "Chandrakala"
college = "ASKW College"

print("Name:", name)
print("College:", college)
print("Data Type:", type(name))
print("\n")

# OUTPUT:
# Name: Chandrakala
# College: ASKW College
# Data Type: <class 'str'>

# ==========Program 5: Boolean Data Type==========
is_student = True
is_placed = False

print("Is Student:", is_student)
print("Is Placed:", is_placed)
print("Data Type:", type(is_student))
print("\n")

# OUTPUT:
# Is Student: True
# Is Placed: False
# Data Type: <class 'bool'>

# ==========Program 6: List Data Type==========
languages = ["Python", "Java", "C", "HTML"]

print("Programming Languages:", languages)
print("First Language:", languages[0])
print("Data Type:", type(languages))
print("\n")

# OUTPUT:
# Programming Languages: ['Python', 'Java', 'C', 'HTML']
# First Language: Python
# Data Type: <class 'list'>

# ==========Program 7: Tuple Data Type==========
colors = ("Red", "Green", "Blue")

print("Colors:", colors)
print("Second Color:", colors[1])
print("Data Type:", type(colors))
print("\n")

# OUTPUT:
# Colors: ('Red', 'Green', 'Blue')
# Second Color: Green
# Data Type: <class 'tuple'>

# ==========Program 8: Set Data Type==========
companies = {"Amazon", "Google", "Microsoft", "Amazon"}

print("Companies:", companies)
print("Data Type:", type(companies))
print("\n")

# OUTPUT:
# Companies: {'Amazon', 'Google', 'Microsoft'}
# (Duplicate values are removed automatically)  ***
# Data Type: <class 'set'>

# ==========Program 9: Dictionary Data Type==========
student = {
    "Name": "Chandrakala",
    "Age": 20,
    "Branch": "CSE",
    "CGPA": 8.5
}

print(student)
print("Name:", student["Name"])
print("Branch:", student["Branch"])
print("Data Type:", type(student))
print("\n")

# OUTPUT:
# {'Name': 'Chandrakala', 'Age': 20, 'Branch': 'CSE', 'CGPA': 8.5}
# Name: Chandrakala
# Branch: CSE
# Data Type: <class 'dict'>

# ==========Program 10: Checking All Data Types==========
integer_value = 10
float_value = 15.5
complex_value = 2 + 3j
string_value = "Python"
boolean_value = True
list_value = [10, 20, 30]
tuple_value = (1, 2, 3)
set_value = {5, 6, 7}
dict_value = {"Name": "Chandu", "Age": 20}

print("Integer:", type(integer_value))
print("Float:", type(float_value))
print("Complex:", type(complex_value))
print("String:", type(string_value))
print("Boolean:", type(boolean_value))
print("List:", type(list_value))
print("Tuple:", type(tuple_value))
print("Set:", type(set_value))
print("Dictionary:", type(dict_value))

# OUTPUT:
# Integer: <class 'int'>
# Float: <class 'float'>
# Complex: <class 'complex'>
# String: <class 'str'>
# Boolean: <class 'bool'>
# List: <class 'list'>
# Tuple: <class 'tuple'>
# Set: <class 'set'>
# Dictionary: <class 'dict'>

# ==========Program 11: Type Checking using type()==========
name = "Chandrakala"
age = 20
percentage = 87.5
is_student = True

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of percentage:", type(percentage))
print("Type of is_student:", type(is_student))
print("\n")

# OUTPUT:
# Type of name: <class 'str'>
# Type of age: <class 'int'>
# Type of percentage: <class 'float'>
# Type of is_student: <class 'bool'>


# ==========Program 12: Checking Data Type using isinstance()==========
number = 100
text = "Python"
marks = [90, 95, 98]

print(isinstance(number, int))
print(isinstance(text, str))
print(isinstance(marks, list))
print(isinstance(number, float))
print("\n")

# OUTPUT:
# True
# True
# True
# False


# ==========Program 13: Type Conversion==========
age = "20"
percentage = "87.5"
number = 100

print("Original Data Types")
print(type(age))
print(type(percentage))
print(type(number))

age = int(age)
percentage = float(percentage)
number = str(number)

print("\nAfter Type Conversion")
print(type(age))
print(type(percentage))
print(type(number))
print("\n")

# OUTPUT:
# Original Data Types
# <class 'str'>
# <class 'str'>
# <class 'int'>
#
# After Type Conversion
# <class 'int'>
# <class 'float'>
# <class 'str'>

# ==========Program 14: Truthy and Falsy Values==========
print("Truthy Values")
print(bool(10))
print(bool("Python"))
print(bool([1, 2, 3]))

print("\nFalsy Values")
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))
print("\n")

# OUTPUT:
# Truthy Values
# True
# True
# True
#
# Falsy Values
# False
# False
# False
# False

# ==========Program 15: Mutable vs Immutable Data Types==========
my_list = [10, 20, 30]
print("Original List:", my_list)

my_list[1] = 99
print("Modified List:", my_list)

my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)

print("\nList is Mutable")
print("Tuple is Immutable")
print("\n")

# OUTPUT:
# Original List: [10, 20, 30]
# Modified List: [10, 99, 30]
# Tuple: (10, 20, 30)
#
# List is Mutable
# Tuple is Immutable


# ==========Program 16: Difference Between List, Tuple, Set and Dictionary==========
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
my_dict = {"Name": "Chandrakala", "Age": 20}

print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)

print("\nCharacteristics")
print("List       : Ordered, Mutable")
print("Tuple      : Ordered, Immutable")
print("Set        : Unordered, No Duplicate Values")
print("Dictionary : Key-Value Pairs")
print("\n")

# OUTPUT:
# List: [10, 20, 30]
# Tuple: (10, 20, 30)
# Set: {10, 20, 30}
# Dictionary: {'Name': 'Chandrakala', 'Age': 20}
#
# Characteristics
# List       : Ordered, Mutable
# Tuple      : Ordered, Immutable
# Set        : Unordered, No Duplicate Values
# Dictionary : Key-Value Pairs

# =====================================================================================
# END OF DAY 3
# DAY 3 COVERS ALL BUILT-IN PYTHON DATA TYPES WITH SIMPLE PROGRAMS
# =====================================================================================