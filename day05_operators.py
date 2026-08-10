# =====================================================================================
# DAY 5 - OPERATORS IN PYTHON
# =====================================================================================
# ==========Program 1: Arithematic Operators==========
a = 10 
b = 3
 
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
print("Floor division:", a//b)
print("Exponentiation:", a**b)        #  it's a power
print("\n")
# OUTPUT:
# Addition: 13
# Subtraction: 7
# Multiplication: 30
# Division: 3.3333333333333335
# Modulus: 1
# Floor division: 3
# Exponentiation: 1000

# ==========Program 2: Comparision or Relational Operators==========
a = 10
b = 5

print("Equal to:", a==b)
print("is not equal to:", a!=b)
print("Greater than:", a>b)
print("Less than:", a<b)
print("Greater than equal to:", a>=b)
print("Less than equal to:", a<=b)
print("\n")

# OUTPUT:
# qual to: False
# is not equal to: True
# Greater than: True
# Less than: False
# Greater than equal to: True
# Less than equal to: False

# ==========Program 3: Logical Operators==========
age = 20

print(age >= 18 and age <= 25)
print(age < 18 or age > 18)
print(not(age < 18))
print("\n")

# OUTPUT:
# True
# True
# True

# ==========Program 4: Assignment Operators==========
number =10

number += 5
print("After += :", number)

number -= 3
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 2
print("After /= :", number)

number %= 4
print("After %= :", number)
print("\n")

# OUTPUT:
# After += : 15
# After -= : 12
# After *= : 24
# After /= : 12.0
# After %= : 0.0

# ==========Program 5: Identity Operators==========
a=[1,2]
b=a
c=[1,2]

print(a is b)
print(a is c)
print("\n")

# OUTPUT:
# True
# False  // Beacause b=a means a and b refer to the same object but c is a seperate list

# ==========Program 6: Membership Operators==========
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" not in fruits)
print("\n")

# OUTPUT:
# True
# True

# ==========Program 7: Bitwise Operators==========
a = 5
b = 3

print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)          # ~n = -(n+1)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# OUTPUT:
# Bitwise AND: 1
# Bitwise OR: 7
# Bitwise XOR: 6
# Bitwise NOT: -6
# Left Shift: 10
# Right Shift: 2

# =====================================================================================
# END OF DAY 5
# =====================================================================================