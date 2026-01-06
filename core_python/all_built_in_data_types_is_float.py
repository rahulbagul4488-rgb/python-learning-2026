"""
Python float data type reference and practice module.

This module focuses specifically on the Python built-in `float` data type
and demonstrates its usage, behavior, and common operations in detail.

The float data type represents real numbers (decimal values) and is
commonly used for mathematical calculations, scientific computing,
data analysis, and AI/ML workloads.

Key concepts covered in this module:
- Creation and assignment of float values
- Arithmetic operations involving floats
- Interaction between int and float
- Float precision and rounding behavior
- Boolean evaluation of float values
- Type conversion (int ↔ float, str → float)
- Comparison pitfalls due to floating-point precision
- Immutability and memory behavior of float objects

The examples in this module are intended for:
- Building a strong understanding of numerical data handling in Python
- Developing clean and Pythonic coding practices
- Avoiding common floating-point precision mistakes
- Preparing for technical interviews and real-world applications
- Strengthening foundations for data science and AI/ML programming

This module is designed purely for learning and practice purposes
and serves as a reference for mastering the float data type in Python.
"""


#  1️⃣ Basic float assignment

a = 10.5 
print(f"Basic of float is {a}")
print(f"basic of float data type is {type(a)}")

# 2️⃣ Integer + float
a  = 10
b = 2.5
c = (a+b)
print(f"int and float output is : {c}")
print(f"int and float data type is : {type(c)}")

# 3️⃣ Type check

a = 3.14
print(f"Check the type is : {type(a)}")


# 4️⃣ Negative float

a = -7.25
print(f"Negative float is : {a}")
print(f"Negative  float is : {type(a)}")

# 5️⃣ Large float

a = 1.23456789e10
print(f"Large float is : {a}")
print(f"Large float data type is : {type(a)}")

# 6️⃣ Float addition

a = 2.54
b = 2.57
c = (a+b)
print(f"Float addition is : {c}")
print(f"Float addition type is : {type(c)}")


# 7️⃣ Float subtraction
a = 14
b = 26
c = (a-b)
print(f"Float subtraction is : {c}")
print(f"Float subtraction  type is {type(a)}")

# 8️⃣ Float multiplication

a = 15
b = 2.8
c = (a*b)
print(f"Float multilplication is {c}")
print(f"Float multiplication type is : {type(c)}")

# 9️⃣ Float division

a = 10
b = 4
c = (a / b)
print(f"Float divition is {c}")
print(f"Float divition type is {type(c)}")

# 🔟 Floor division with float

a = 10.5
b = 2
c = (a // b)
print(f"Float divition with float is : {c}")
print(f"Float divition type is  {type(c)}")

# 1️⃣1️⃣ Modulus with float

a = 10.5
b = 5
c = (a%b)
print(f"Modulus with float is : {c}")
print(f"Moulus with float type is {type(c)}")

# 1️⃣2️⃣ Power with float
a = 2.5
b = (a ** 2)
print(f"Power with float is {b}")

# 1️⃣3️⃣ Float reassignment

a = 1.5
a = 3.5
print(f"Float reassigment : {a}")

# 1️⃣4️⃣ Same float value, different variables

a = 2.2
b = 2.2
print(f" Same float value diffrent variable is : {a, b}")

# 1️⃣5️⃣ Chained assignment

a = b = c = 1.5
print(f" Chain assigment is : {a, b, c}")


# 1️⃣6️⃣ Comparison of floats

a = 0.1 + 0.2
b = 0.3
print(f" Comparation of floats is : {a == b}")


# 1️⃣7️⃣ Float comparison (tolerance idea)

a = 0.1 + 0.2
print(f"Float comparion (tolerance idea : {round(a, 2) == 0.3}")

      
# 1️⃣8️⃣ Float to bool

a = 0.0
print(f" Float to bool : {bool(a)}")

# 1️⃣9️⃣ Positive float to bool

a = 0.0001
print(f" Positive float to bool  : {a}")


# 2️⃣0️⃣ Float with logical operator

a = 2.5
b = 0.0
print(f"Float with logical operator is {a and b}")

# 2️⃣1️⃣ Absolute value

a = -12.75
print(f"Float with absolute value is {abs(a)}")


# 2️⃣2️⃣ Float from string

a = float("12.34")
print(f" Float with string : {a}")

# 2️⃣3️⃣ Invalid float conversion (comment & test)

# a = float("abc")
# print(a)

# 2️⃣4️⃣ Int to float

a = float(10)
print(f"int to float  is {a}")

# 2️⃣5️⃣ User input as float

a = float(input("Enter a float value: "))
print(f" Usert input as float is {a}")

# 2️⃣6️⃣ Sum of two float inputs

a = float(input("Enter a: "))
b = float(input("Enter b: "))
print(f"Sum of the two float input is {a + b}")


# 2️⃣7️⃣ Check decimal part

a = 10.75
print(f" Check the decimal part is {a - int(a)}")

# 2️⃣8️⃣ Rounding float

a = 3.14159
print(f" ROunding float is {round(a, 2)}")

# 2️⃣9️⃣ Memory reference check

a = 2.5
b = a
print(f" Memory refrence check is  {id(a), id(b)}")


# 3️⃣0️⃣ Float inside list

values = [1.1, 2.2, 3.3]
print(f" Float inside list is {values[1]}")







