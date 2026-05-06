# 1️⃣ Basic bytes literal

b = b"Hello"
print(f"Basic byte literal is : {b}")
print(f"basic byte data type is   {type(b)}")

# 2️⃣ Type check

b = b"Rahul"
print(f"the data typ-es is {type(b)}")

# 3️⃣ Bytes with numbers (ASCII)

b = b"123"
print(f"the bytes with number is {b}")

# 4️⃣ Bytes from list

b = bytes([10,20,30,40,50])
print(f"The bytes from list is {b}")

# 5️⃣ Bytes from range

b = bytes(range(50))
print(f"Byte form range is {b}")
print(f"Show the byte range in decimal numbe4rs {list(b)}")

# 6️⃣ Bytes length

b = b"Hello"
print(f"The byte from lenght is {len(b)}")

# 7️⃣ Bytes indexing

b = "abc"
print(f"The bytes index is {b[1]}")

# 8️⃣ Bytes slicing

b = b"Python"
print(f"The bytes slicing is {b[1:4]}")

# 9️⃣ Bytes immutability test (comment & test)

# b = b"Hi"
# b[0] = 72

# 🔟 Bytes reassignment

a = b"rahul"
print(a)
b = b"bagul"
print(b)
b = a
print(f"The bytes reassigments is {b}")

# 1️⃣1️⃣ Bytes iteration

b = b"ABC"
for x in b:
    print(f"The byte numer is : {x}")

# 1️⃣2️⃣ Membership check

b = b"python"
print(f"The membership check is {80 in b}")

# 1️⃣3️⃣ Bytes concatenation

a = "Rahul"
b = "Bagul"
c = (a+b)
print(f"The two string concatnation is {c}")

# 1️⃣4️⃣ Bytes repetition

b = b"A"
print(f"The byte concatenation is {b*2}")

# 1️⃣5️⃣ Bytes comparison

a = (b"A" < b"B")
print(f"The byte comparation is  : {a}")

# 1️⃣6️⃣ Convert string to bytes (encoding)

a = "Rahul"
print(f"The data type is {type(a)}")
b = a.encode("utf-8")
print(f"The convert string to bytes is {b}")
print(f"The data type is {type(b)}")


# 1️⃣7️⃣ Convert bytes to string (decoding)

a = b"Rahul"
print(f"The data type is {type(a)}")
b = a.decode("utf-8")
print(f"The convert bytes to string (decoding) is {b}")
print(f"The data type is {type(b)}")

# 1️⃣8️⃣ Bytes from string using constructor

b = bytes("Hell0", "utf-8")
print(f"the bytes from constructor is {b}")

# 1️⃣9️⃣ Invalid bytes (comment & test)

# b = b"हॅलो"

# 2️⃣0️⃣ Valid Unicode via encoding

s = "हॅलो"
b = s.encode("utf-8")
print(b)

# 2️⃣1️⃣ Bytes inside list

data = [b"A", b"B", b"C"]
print(data)

# 2️⃣2️⃣ Bytes inside tuple

t = (b"Hi" , b"Bye")
print(f"Byte inside the tupel is {t}")

# 2️⃣3️⃣ Bytes inside dict

d = {b"id": 101}
print(d[b"id"])

# 2️⃣4️⃣ Bytes memory reference

b = b"Test"
c = b
print(id(b), id(c))

# 2️⃣5️⃣ Bytes comparison equality

print(b"Hi" == b"Hi")

# 2️⃣6️⃣ Bytes to list

b =b"ABC"
print(list(b))

# 2️⃣7️⃣ Bytes to tuple

b = b"ABCD"
print(tuple(b))

# 2️⃣8️⃣ Bytes with range logic

for x in bytes(range(48, 53)):
    print(x)

# 2️⃣9️⃣ Bytes boolean value

print(bool(b""))
print(bool(b"A"))

# 3️⃣0️⃣ Bytes size efficiency demo

b = bytes(range(256))
print(len(b))

