# 1️⃣ Create a list

L = [1,2,3,4,5]
print(f"The basis list is {L}")
print(f"The basci list Data type is {type(L)}")

# 2️⃣ Check type

L = [1, 2, 3]
print(f"The basci list Data type is {type(L)}")

# 3️⃣ Empty list

L  = []
print(f"The empty list is : {L}")
print(f"The basci list Data type is {type(L)}")


# 4️⃣ List with mixed data types

L = ["Rahul", 1.5, 15, 2+3j]
print(f"The mixed data type is : {L}")
print(f"The basci list Data type is {type(L)}")

# 5️⃣ Nested list

L = [[1,2], [2,3], [3,4],[4,5]]
print(f"The nested list is {L}")
print(f"The basci list Data type is {type(L)}")

# 6️⃣ List length

L =[10,20,30,40,50]
print(f"The length is {len(L)}")

# 7️⃣ List from range

L = [list(range(11))]
print(f"The list from range is : {L}")


# 8️⃣ List memory behavior

L = [10]
M = ["A"]
print(f"The list data type object refrence id is : {id(L)}")
print(f"The list data type object refrence id is : {id(M)}")


L = [10]
print(f"The list data type object refrence id is : {id(L)}")
M = L
print(f"The list data type object refrence id is : {id(L)}")
print(f"The list data type object refrence id is : {id(M)}")


# 9️⃣ List repetition

L = [10]
print(f"The list repetition is {L*5}")

# 🔟 List concatenation

L = [10,50]
M = [20,80]
A = L+M
print(f"The list concatenation is : {A}")

# I just print first single list and the after that concat all list 
L = [1]
print(L)
M = [2]
N = [3]
O = [4]
P = [5]
print(f"The list addition is : {L+M+N+O+P}")


# 1️⃣1️⃣ Indexing (MOST IMPORTANT)

nums = [10,20,30,40,50]

print(f"The first index elemnt is : {nums[0]}")
print(f"The second index element is {nums[1]}")
print(f"The third index element is {nums[2]}")
print(f"The fourth index element is {nums[3]}")
print(f"The fifth index element is {nums[4]}")

# 1️⃣2️⃣ Slicing

nums = [ 10,20,30,40,50,60,70,80,90]

print(f"I want the access element 2nd index and 4th index is {nums[2:5:2]}")
print(f"I want the first element is this given list {nums[0]}")
print(f"I want the print the last element {nums[-1]}")
print(f"i wnat the aceess the element is in this list is {nums[4:5]}")
total = len(nums)
print(f"Print he total number count is {total}")
result = total//2
print(f"The list mid is {result}")
#print(f"The mid number is in this list {nums[result]}")
final_result = nums[result:result+1]
print(f"The final mid element is in this list is {final_result}")


# 1️⃣3️⃣ List is MUTABLE (VERY IMPORTANT)

nums = [10,20,30,40,50]
nums [1] = 100
print(f"The new updated list is {nums}")

# 1️⃣4️⃣ Iteration (loop)

nums = [10,20,30,40,50]
for i in nums:
    print(f"The iteration is {i}")


# 1️⃣5️⃣  Membership check

nums = [10,20,30,40,50,60,70,80,90]
print(f"check this memership in this list {20 in nums}")
print(f"check this memership in this list {96 in nums}")

# 1️⃣6️⃣ Copy list (important later)

a = [1,2]
print(id(a))
print(f"Print the old element is {a}")
b =a.copy()
print(id(b))
print(f"The copy of ths old element in new elemet {b}")
print(id(a), id(b))

# 1️⃣7️⃣ Try modifying tuple inside list

nums = [(1,2), (3,4)]
print(nums)
print(type(nums))

# 1️⃣8️⃣ Count elements using loop

a = [10,20,30,40,50]
count = 0
for _ in a:
    count +=1
print(count)

# 1️⃣9️⃣ Modify last element

a =  [10,20,30,40,50,60,70,80,90]
a [-1] = 100
print(f"the last element modified is the {a}")


# 2️⃣0️⃣ Loop with index

a = [10, 20, 30]
for i in range(len(a)):
    print(i, a[i])


a = [10,20,30,40,50,60,70,80,90]
for i , value in enumerate(a):
    print(i, value)


# Core logic without built in function like len and enumerator 

a = [10, 20, 30]
index = 0
for value in a:
    print(index, value)
    index = index + 1


# 2️⃣1️⃣  Compare lists

a = [10,20]
b = [10,20]
print(a==b)
print(a is not b)










