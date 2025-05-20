# -------------------------------
# Example using the 'is' operator
# -------------------------------

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Value comparison: Do 'a' and 'b' have the same content?
print(a == b)  # True: The values inside the lists are the same

# Identity comparison: Are 'a' and 'b' pointing to the same memory location?
print(a is b)  # False: Although the values are same, they are two separate list objects

# Identity comparison: Are 'a' and 'c' the same object in memory?
print(a is c)  # True: 'c' is just another reference to the same object as 'a'

# You can also verify memory locations using the id() function
print("ID of a:", id(a))
print("ID of b:", id(b))
print("ID of c:", id(c))

# Summary:
# '==' compares values/content
# 'is' checks if both variables point to the exact same object in memory

# --------------------------------
# Example using the 'in' operator
# --------------------------------

fruits = ["apple", "banana", "cherry"]

# Membership test: Is 'banana' one of the elements in the list?
print("banana" in fruits)  # True: Found in the list

# Membership test: Is 'grape' in the list?
print("grape" in fruits)   # False: Not found in the list

# Membership test with string
message = "Learning Python is fun"
print("Python" in message)  # True: 'Python' is a substring of the message
print("Java" in message)    # False: 'Java' is not present in the string

# Membership test with dictionary (checks only keys)
student = {"name": "Alice", "age": 20, "grade": "A"}
print("name" in student)    # True: 'name' is a key in the dictionary
print("Alice" in student)   # False: 'Alice' is a value, not a key

# Summary:
# 'in' checks for existence:
# - In lists/tuples/sets: checks if value exists
# - In strings: checks if substring exists
# - In dictionaries: checks if key exists
