# 1️⃣ Basic tuple

t = (1,2,3)
print(t)

# 2️⃣ Tuple without parentheses

t = 10, 20, 30
print(f"Tuple without paranthesis is : {t}")
print(f"without paranthesis data type check is : {type(t)}")

# 3️⃣ Type check

t = (5, 6)
print(type(t))

# 4️⃣ Single element tuple

t = (10,)
print(f"Single element tuple is : {t}")

# 5️⃣ Empty tuple

t = ()
print(f"empty tuple is : {t}")


# 6️⃣ Tuple with mixed data types

t = (1, "Rahul", 15.6, 2+3j)
print(f"tuple with mix data type is : {t}")

# 7️⃣ Tuple indexing

t = ("Rahul", 32, "Bagul")
print(f"tuple indexing is : {t[2]}")
print(f"tuple indexing data type is {type(t)}")

# 8️⃣ Negative indexing

t = ("x", "y", "z")
print(f"tuple negative indexing is : {t[-1]}")

# 9️⃣ Tuple slicing

t = (10, 20, 30, 40)
print(f" tuple slicing is : {t[1:3]}")

# 🔟 Reverse tuple

t = (1, 2, 3, 4)
print(f"reverse tuple is : {t[::-1]}")

# 1️⃣1️⃣ Tuple immutability test (comment & test)

# t = (1, 2, 3)
# t[0] = 100


# 1️⃣2️⃣ Tuple reassignment

t = (1, 2)
t = (3, 4)
print(f" tuple reassigment is : {t}")

# 1️⃣3️⃣ Tuple length

t = (5, 10, 15)
print(f"tuple lenght is {len(t)}")

# 1️⃣4️⃣ Tuple concatenation

a = (1, 2)
b = (3, 4)
print(f"tuple concatenation {a + b}")

# 1️⃣5️⃣ Tuple repetition
t = (1, 2)
print(f" tuple repetition {t *3}")

# 1️⃣6️⃣ Membership check

t = (10, 20, 30)
print(f"membership check {20 in t}")
print(f"mebership data type : {type(t)}")

# 1️⃣7️⃣ Tuple unpacking

t =  (1, 2, 3)
a, b, c = t
print(f"tuple uppacking {a, b, c}")

# 1️⃣8️⃣ Partial unpacking

t = (1, 2, 3 , 4)
a, b, *c = t
print(f"partitial unpacking {a,b,c}")

# 1️⃣9️⃣ Swap using tuple
a = 10
b = 20
a, b = b, a 
print(f"swap using using the tuple {a,b}")

# 2️⃣0️⃣ Nested tuple 

t = ((1,2), (3,4))
print(f"nested tuple is {t[1][0]}")

# 2️⃣1️⃣ Tuple inside list
data = [(1,2), (3,4)]
print(f"tuple inside list {(data[1])}")

# 2️⃣2️⃣ List inside tuple

t = ([1,2], [3,4])
print(f"list inside tuple {t}")

# 2️⃣3️⃣ Modify mutable element inside tuple

t = ([1, 2], 3)
t[0].append(5)
print(f"modify mutable element inside tuple {t}")

# 2️⃣4️⃣ Tuple count

t = (1, 2, 2, 3)
print(f"tuple count {t.count(2)}")

# 2️⃣5️⃣ Tuple index

t = (10, 20, 30)
print(f" tuple index {t.index(20)}")

# 2️⃣6️⃣ Tuple comparison

a = (1, 2)
b = (1, 3)
print(f" tuple comparison {a < b}")

# 2️⃣7️⃣ Tuple as dict ke

data = {(1,2): "point"}
print(f" tuple as dict key {data[(1,2)]}")

# 2️⃣8️⃣ Tuple from list

lst = [1,2,3,4]
t = tuple(lst)
print(f" tuple from list {t}")

# 2️⃣9️⃣ Tuple memory reference

a = (1,2)
b = a
print(f"tuple memory refrence {id(a), id(b)}")

# 3️⃣0️⃣ Tuple iteration

t = ("Python", "Java", "C")
for item in t:
    print(item)
