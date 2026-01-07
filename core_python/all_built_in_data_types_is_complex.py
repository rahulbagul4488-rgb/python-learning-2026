# 1️⃣ Basic complex number

a = 3 + 4j
print(f" Basic complex number is {a}")
print(f"Basic of complex number Data type  is {type(a)}")

# 2️⃣ Complex with negative imaginary part

a = 5 - 2j
print(f" Complex with negative imaginary part is {a}")


# 3️⃣ Type check

a = 7 + 1j
print(f" Type of complex data type is {type(a)}")

# 4️⃣ Real part

a = 10 + 20j
print(f" The real number is {a.real}")

# 5️⃣ Imaginary part

a = 10 + 20j
print(f"Imaginary part is {a.imag}")

# 6️⃣ Complex addition

a = 3 + 2j
b = 1 + 4j
c = (a+b)
print(f"Complex addtion is {c}")

 # 7️⃣ Complex subtraction

a = 5 + 6j
b = 2 + 3j
c = (a-b)
print(f"Complex subtraction is {c}")


# 8️⃣ Complex multiplication

a =  1 + 2j
b =  3 + 4j
c = (a*b)
print(f"Complex multiplication is  {c}")
print(f"Complex multiplication is Data type is {type(c)}")

# 9️⃣ Complex division

a = 4 + 2j
b = 1 + 1j
c = (a/b)
print(f"Complex division is  {c}")

# 🔟 Complex power

a = 2 + 3j
print(f"Complex power is {a**2}")

# 1️⃣1️⃣ Complex conjugate

a = 5 + 7j
print(f"Complex conjugate is {a.conjugate()}")

# 1️⃣2️⃣ Absolute value (magnitude)
a = 3 + 4j
print(f"Absolute value magnitute is {abs(a)}")
print(f"Absolute value magnitute  Data Type is {abs(a)}")

# 1️⃣3️⃣ Create complex using constructor
a = 3 + 4j
print(f"Create complex using constructor is {a}")


# 1️⃣4️⃣ Complex from float + imaginary

a = complex(3.5, -2.7)
print(f"Complex from float + Imaginary is  {a}")

# 1️⃣5️⃣ Reassignment

a = 1 + 1j
b = 2 + 2j
print(f"Reassignment complex number is {a}")


# 1️⃣6️⃣ Complex comparison (equality only)

a = 2 + 3j
b = 2 + 3j
c =  (a == b)
print(f"Complex comparison is {c}")

# 1️⃣7️⃣ Invalid comparison (comment & test)

# a = 2 + 3j
# b = 1 + 2j
# print(a > b)

# 1️⃣8️⃣ Complex inside list

nums = [1+2j, 3+4j, 5+6j]
print(f"Complex inside list is {nums[1]}")

# 1️⃣9️⃣ Complex inside tuple
data = (2+3j, 4+5j)
print(f" Complex inside tuple is {data}")


# 2️⃣0️⃣ Complex inside dict

z = 1 + 2j
d = {"value": z}
print(f" Complex inside dict is {d["value"]}")

# 2️⃣1️⃣ Convert int to complex

a = complex(10)
print(f"Convert int to complex is {a}")


# 2️⃣2️⃣ Convert float to complex

a = complex(3.14)
print(f"Convert float to complex {a}")


# 2️⃣3️⃣ Complex from string

a = complex("2+3j")
print(f"Complex from dtring is {a}")

# 2️⃣4️⃣ Invalid complex string (comment & test)

# a = complex("2 + 3j")
# print(a)


# 2️⃣5️⃣ Boolean value of complex

a = 0 + 0j
print(bool(a))

# 2️⃣6️⃣ Non-zero complex to bool

a = 1 + 0j
print(bool(a))

# 2️⃣7️⃣ Memory reference check

a = 3 +4j
b = a
print(f"Memory refrence check is {id(a), id(b)}")

# 2️⃣8️⃣ Complex in arithmetic mix

a = 5 + 2j
b = 10
c = (a+b)
print(f"Complex in arithmetic mix is {c}")

# 2️⃣9️⃣ Complex in float mix

a = 1.5
b = 2 + 3j
c = (a + b)
print(f"Complex in float mix  {c}")

# 3️⃣0️⃣ Magnitude comparison

a = 3 + 4j
b = 1 +1j
print(f"Magnitute comparison : {abs(a) > abs(b)}")
