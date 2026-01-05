"""
Python built-in data types reference and practice module.

This module demonstrates usage, behavior, and common operations
of all core Python built-in data types, organized in a clean
and logical hierarchy for learning and revision purposes.

Covered categories:
- Numeric types: int, float, complex
- Sequence types (immutable and mutable)
- Set types
- Mapping type (dict)
- Boolean type
- Binary and buffer type (memoryview)
- None type

The examples in this module are intended for:
- Building strong Python fundamentals
- Interview preparation
- Code readability and best practices
- Understanding mutability and data behavior

This module is designed as a learning-focused reference,
not as a production utility.
"""









# # ## There are two main types of data types in Python:

# # **1) Built-in Data Types**

# # **2) User-Defined Data Types**


# # ## Python Built-in Data Types (Clean Hierarchy)

# # **I. NUMERIC Data  TYPES:**

# 1) int Data Type

# Code 1: Integer Creation & Types

# 1️⃣ Basic int assignment

DATA=11
print(DATA)
print(type(DATA))

DATA1=55
print(DATA1)
print(type(DATA1))

# 2️⃣ Negative integer

NEGATIVE_NUMBER=-85
print(NEGATIVE_NUMBER)
print(type(NEGATIVE_NUMBER))


# 3️⃣ Zero  integer

ZERO_NUMBER = 0
print(ZERO_NUMBER)
print(type(ZERO_NUMBER))

# 4️⃣ Large integer

LONG_NUMBER = 14586975625896546562255
print(LONG_NUMBER)
print(type(LONG_NUMBER))

# 5️⃣ Addition

A=10
B=20
print(A+B)

# 6️⃣ Subtraction

A = 100
B = 25
print(A-B)
print(type(A-B))

# 7️⃣ Multiplication

A = 25
B = 5
print(A*B)
print(type(A*B))

# 8️⃣ Division (observe result)

A = 10
B = 2
print(A-B)
print(type(A-B))

# 9️⃣ Floor division

a = 10
b = 20
print(a//b)
print(type(a//b))

# 🔟 Modulus

a = 10
b = 20
result= a%b
print("Modulus is:", {(result)})
print(f"Type of result: {type(result)}")


a = 10
b = 20

modulus = a % b
print(f"Modulus is: {modulus}")
print(f"Result type: {type(modulus)}")

#  1️⃣1️⃣ Power

a = 2
b = 5
power = a**b
print(f"Power is : {power}")
print(f"power type: {type(power)}")

# 1️⃣2️⃣ int + int + int

a = 10
b = 20
c = 30
int_all = (a+b+c)
print(f"int_all is : {int_all}")
print(f"all_int type is: {type(int_all)}")

# 1️⃣3️⃣ int reassignment

a = 10
a = 20
print(f"int reassigment is : {a} ")


# 1️⃣4️⃣ Same value, different variables

a = 10
b = 10
print(f"same value , diffrent varaiables : {a,b}")


# 1️⃣5️⃣ Chained assignment

a = b = c = 100
print(f" Chained assignment : {a, b, a}")


# 1️⃣6️⃣ Comparison

a = 10
b = 20
print(f"Comparison : {a <  b}")


# 1️⃣7️⃣ Equality check

a = 15
b = 15
print(f"1Equality check : {a == b}")

# 1️⃣8️⃣ Boolean result from int

a = 0
print(f"Boolean result from int : {bool(a)}")


#  1️⃣9️⃣ Positive int to bool

a = 5
print(f"Positive int to bool : {(bool(a))}")

# 2️⃣0️⃣ int with logical operator

a = 10
b = 0
print(f"int with logical operator : {(a,b)}")

# 2️⃣1️⃣ Absolute value

a = -50
print(f" Absolute value : {(abs(a))}")

# 2️⃣2️⃣ int from string

a = int("123")
print(f"int from string : {a}")
print(f"int string type : {type(a)}")

# 2️⃣4️⃣ int from float

a = int(12.5)
print(f"int from float : {a}")
print(f"int from float is : {type(a)}")

# 2️⃣5️⃣ User input (assume number)

a =  int(input("Enter tha input : "))
print(f"user input assume number is : {a}")
print(f"user input number is type  is : {type(a)}")

# 2️⃣6️⃣ Sum of two user integers

a = int(input("Enter tha number  a: "))
b = int(input("Enter the second number b : "))
print(f"sum of the two number is : {a+b}")

# 2️⃣7️⃣ Check even or odd

a = int(input("Enter the number : "))
print(f"The number is : {a % 2 ==0}")


a = int(input("Enter the number : "))
if a % 2 ==0:
    print(f"The number is even ")
else:
    print(f"The number is odd ")

# 2️⃣8️⃣ Swap two integers

a = 20
b = 30
a, b = b ,  a
print(f"swap the two numbers : a = {a}")
print(f"swap the two numbers : b = {b}")


# 2️⃣9️⃣ Memory reference check

a = 10
b = a
print(f"Memory refrence check is : {id(a), id(b)}")

# 3️⃣0️⃣ int inside list

nums = [1,2,3,4,5]
print(f"int inside the numbers is : {nums[2]}")
