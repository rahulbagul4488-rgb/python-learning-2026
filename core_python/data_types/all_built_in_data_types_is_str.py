# 1️⃣ Basic string

name = "Rahul"
print(f" Basic string is {name}")


# 2️⃣ Single quotes

name = 'Rahul'
print(f" Single quotes string is {name}")

# 3️⃣ Type check

text = "Python"
print(type(text))

# 4️⃣ Empty string

s = ""
print(f"Empty string is {s}")

# 5️⃣ String with numbers

name = "1234"
print(f"String with number {name}")


# 6️⃣ String concatenation

a = "Hello"
b = "Rahul"
c = (a + " " + b )
print(f"String concatenation is {c}")


# 7️⃣ String repetition

name = "Rahul"
print(f"String repetion is {name * 5}")


# 8️⃣ Length of string

msg = "Python"
print(f"Lenght of string is {len(msg)}")

# 9️⃣ Indexing

text = "Python"
print(f"Indexing is {text[1]}")

# 🔟 Negative indexing

text = "Rahul"
print(f"Negative indexing is {text[-1]}")

# 1️⃣1️⃣ Slicing

text = "RahulMadhavraoBagul"
print(f"slicing is {text[0:6]}")


# 1️⃣2️⃣ Slice with step
text = "RahulMadhavraoBagul"
print(f"Slicing with steps {text[0:10:2]}")

# 1️⃣3️⃣ Reverse string
text = "Rahul"
print(f"Reverse string is {text[:-1]}")

# 1️⃣4️⃣ String immutability test (comment & test)

# text = "Python"
# text[0] = "J"

# 1️⃣5️⃣ Reassignment

text = "Python"
text = "Java"
print(f"Reassingment is {text}")

# 1️⃣6️⃣ Uppercase

name = "rahul"
print(f"Uppercase {name.upper()}")

# 1️⃣7️⃣ Lowercase

name = "RAHUL"
print(f"Lower case is {name.lower()}")

# 1️⃣8️⃣ Capitalize

name = "python"
print(f"captilize {name.capitalize()}")

# 1️⃣9️⃣ Title case

line = "python programming language"
print(f"Title case {line.title()}")

# 2️⃣0️⃣ Strip spaces

text = "  hello  "
print(f"Strip spaces {text.strip()}")


# 2️⃣1️⃣ Replace

text = "I like Java"
print(f" Replace {text.replace('Java', 'Python')}")

# 2️⃣2️⃣ Find substring

text = "Python programming"
print(f" Find the substring {text.find('program')}")

# 2️⃣3️⃣ Check startswith

text = "Python"
print(f" Check startswith  {text.startswith('Py')}")


# 2️⃣4️⃣ Check endswith

text = "Python.py"
print(f"Check endswith is :  {text.endswith('.py')}")

# 2️⃣5️⃣ Split string

line = "apple,banana,grapes"
print(line.split(","))

# 2️⃣6️⃣ Join strings

words = ["Python", "is", "awesome"]
print(f" Join string is : {' '.join(words)}")

# 2️⃣7️⃣ String formatting (f-string)

name = "Rahul"
age = 32
print(f"My name is {name} and I am {age} year old")

# 2️⃣8️⃣ String comparison

a = "Rahul"
b = "Rahul"
c = (a == b)
print(f"String comparition  {c}")

# 2️⃣9️⃣ Membership check

text = "python programming"
print("python" in text)

# 2️⃣9️⃣ Membership check

names = ["Rahul", "Amit", "Neha"]
print(f" Membership check  {names[0]}")

