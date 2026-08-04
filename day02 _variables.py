# =====================================================================================
# DAY 2 - VARIABLES IN PYTHON
# EVERY EXPERT WAS ONCE A BEGINNER . 👍
# =====================================================================================
# ==========Program 1: Creating Variables==========
name = "Chandrakala"
age = 20
percentage = 87.7
print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)
print("\n")

# OUTPUT:
# Name: Chandrakala
# Age: 20
# Percentage: 87.7

# ==========Program 2: Rules For Naming Variables==========
student_name = "Chandu"
_marks = 87
city11 = "Tadipatri"
print(student_name)
print(_marks)
print(city11)  

print("\n Variable names:")
print(" Can contain letters, numbers, underscore (_)")
print(" Cannot start with a number")
print(" Cannot contain spaces")
print(" Are case-sensitive")
print(" Cannot use python keywords(if,else,class, def.....)")
print("\n")

# OUTPUT:
# Chandu
# 87
# Tadipatri

#  Variable names:
#  Can contain letters, numbers, underscore (_)
#  Cannot start with a number
#  Cannot contain spaces
#  Are case-sensitive
#  Cannot use python keywords(if,else,class, def.....)

# ==========Program 3: Multiple Variable Assignment==========
x, y, z = 10, 20, 30 
print("X =", x)
print("Y =", y)
print("Z =", z)
print("\n")

# OUTPUT:
# X = 10
# Y = 20
# Z = 30

# ==========Program 4: Assign Same Value==========
a = b = c = 100
print(a)
print(b)
print(c)
print("\n")

# OUTPUT:
# 100
# 100
# 100

# ==========Program 5: Swapping Two Variables==========
num1 = 50
num2 = 100
print("Before Swapping")
print("num1 =", num1)
print("num2 =", num2)
num1, num2 = num2, num1
print("After Swapping")
print("num1 =", num1)
print("num2 =", num2)
print("\n")

# OUTPUT:
# Before Swapping
# num1 = 50
# num2 = 100
# After Swapping
# num1 = 100
# num2 = 50

# ==========Program 6: Case Sensitivity==========
name = "Chandrakala"
Name = "Python"
print(name)
print(Name)
print("\n")

# OUTPUT:
# Chandrakala
# Python

# ==========Program 7: Updating Variables==========
marks = 80
print("Old Marks:", marks)
marks = 95
print("Updated Marks:", marks)
print("\n")

# OUTPUT:
# Old Marks: 80
# Updated Marks: 95

# ==========Program 8: Deleting Variables==========
value = 500
print("Value =", value)
del value
print("Variable 'value' deleted successfully.")
print("\n")

# OUTPUT:
# Value = 500
# Variable 'value' deleted successfully.

# ==========Program 9: Checking Variable Type==========
name = "chandu"
marks = 877
percentage = 87.7
is_student = True
num = 3+2j
skills = ["Python", "HTML", "JAVA"]
skills2 = ("good communicator", "problem-solving")
companies = {"Amazon", "Google", "Microsoft"}
print(type(name))
print(type(marks))
print(type(percentage))
print(type(is_student))
print(type(num))
print(type(skills))
print(type(skills2))
print(type(companies))
print("\n")

# OUTPUT:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'complex'>
# <class 'list'>
# <class 'tuple'>
# <class 'set'>

# ==========Program 10: Student Details==========
name = "Chandrakala"
college = "ASKW"
CGPA = 85.7
Roll_number = "242ta05159"
company1 = "Amazon"
company2 = "Google"
print("Name: ", name)
print("College: ", college)
print("CGPA: ",CGPA)
print("ROLL NUMBER: ", Roll_number)
print("Company1: ", company1)
print("Company2: ", company2)

# OUTPUT:
# Name:  Chandrakala
# College:  ASKW
# CGPA:  85.7
# ROLL NUMBER:  242ta05159
# Company1:  Amazon
# Company2:  Google
# =====================================================================================
# END OF DAY 2
# KEEP LEARNING. KEEP GROWING. 🚀
# =====================================================================================