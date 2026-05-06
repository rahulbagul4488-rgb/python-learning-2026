"""
Python range data type reference and practice module.

This module focuses on the Python built-in `range` data type and demonstrates
its usage, behavior, and common patterns in a structured and learning-oriented way.

The `range` data type represents an immutable sequence of integers and is
primarily used for iteration, looping, indexing, and generating numeric sequences
in a memory-efficient manner.

Key concepts covered in this module:
- Creation of range objects using start, stop, and step values
- Iteration using range in loops
- Indexing and slicing on range objects
- Membership testing with the `in` operator
- Length calculation and comparisons
- Conversion of range to list or tuple when needed
- Memory efficiency and lazy evaluation behavior
- Immutability of range objects

The examples in this module are intended for:
- Building strong fundamentals of Python iteration mechanisms
- Understanding how Python handles numeric sequences efficiently
- Writing clean and performant loops
- Preparing for technical interviews
- Developing a solid foundation for data structures and algorithms

This module is designed purely for learning and practice purposes
and serves as a reference for mastering the range data type in Python.
"""



# 1️⃣ Basic range

r = range(5)
print(f"the range is {r}")


# 2️⃣ Convert range to list

r = range(5)
b = (list(r))
print(f"convert range to list data type {b}")
print(f"converted range to list data type is {type(b)}")

# 3️⃣ Type check

r = range(10)
print(f"the range is {type(r)}")


# 4️⃣ Range with start & stop
r = range(2, 10)
print(f"The range starting and stop is : {r}")

# 5️⃣ Range with step
r = range(0,10,2)
print(f"the list of range steps is {list(r)}")


# 6️⃣ Negative step

r = range(10,0,-1)
print(f"the negative steps is {r}")

# 7️⃣ Range indexing

r = range(10)
print(f"the range indexing is {r[5]}")

# 8️⃣ Negative indexing
r= range(10)
print(f"the negative indexing is {r[-2]}")

# 9️⃣ Range slicing
r = range(10)
print(f"range slicing is {list(r[2:7])}")

# 🔟 Reverse range using slicing

r = range(10)
print(f"the reverse range slicing is the {r[::-1]}")

# 1️⃣1️⃣ Range length

r = range(1, 20, 2)
print(f" range lenght is {len(r)}")


# 1️⃣2️⃣ Membership check

r = range(1, 10)
print(f" membership check is  {5 in r}")

# 1️⃣3️⃣ Membership check (false)

r = range(1, 10, 2)
print(f" membership check  {4 in r}")


# 1️⃣4️⃣ Range equality

print(range(0,5) == range(5))

# 1️⃣5️⃣ Range inequality

print(range(0, 5) != range(1, 6))

# 1️⃣6️⃣ Range in for loop

for i in range(5):
    print(i)

# 1️⃣7️⃣ Range with start in loop

for i in range(2, 6):
    print(i)

# 1️⃣8️⃣ Range with step in loop

for i in range(1,10,3):
    print(i)


# 1️⃣9️⃣ Range backward loop

for i in range(5, 0 -1):
    print(i)

# 2️⃣0️⃣ Nested loop with range

for i in range(3):
    for j in range(2):
        print(i, j)

# 2️⃣1️⃣ Range to tuple

r = range(4)
print(f"range to tuple is {tuple(r)}")


# 2️⃣2️⃣ Range inside list

lst = list(range(3))
print(f"range inside list is {lst}")

# 2️⃣3️⃣ Range inside tuple

t = tuple(range(3))
print(f"range inside tuple is {t}")

# 2️⃣4️⃣ Range memory reference

r = range(10)
print(f"range inside tuple is {id(r)}")


# 2️⃣5️⃣ Range object reuse

r = range(5)
a = r
print(a is r)


# 2️⃣6️⃣ Large range (memory efficient)

r = range(1000000)
print(f" large range {len(r)}")


# 2️⃣7️⃣ Range sum
r = range(1,6)
print(f" range sum {sum(r)}")

# 2️⃣8️⃣ Range max

r = range(1, 10)
print(f"range max {max(r)}")

# 2️⃣9️⃣ Range min

r = range(1,10)
print(f"range min {min(r)}")

# 3️⃣0️⃣ Range with enumerate

for index, value in enumerate(range(3)):
    print(index, value)
