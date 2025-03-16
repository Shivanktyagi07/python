"""
Python Mutability & Immutability - In-Depth Explanation with Code Examples
"""

# 1. Understanding Mutability and Immutability
# - Mutable objects can be changed after creation.
# - Immutable objects cannot be changed after creation.

# 2. Immutable Objects in Python
# Immutable objects include: int, float, bool, str, tuple, frozenset

# Integer (Immutable)
a = 10
print(id(a))  # Memory address of 'a'
a = a + 5  # Creates a new object instead of modifying 'a'
print(id(a))  # New memory address

# String (Immutable)
string1 = "Hello"
print(id(string1))
string1 += " World"  # Creates a new string object
print(id(string1))  # New memory address

# Tuple (Immutable)
tuple1 = (1, 2, 3)
print(id(tuple1))
tuple1 += (4, 5)  # Creates a new tuple object
print(id(tuple1))  # New memory address

# 3. Mutable Objects in Python
# Mutable objects include: list, dict, set, bytearray

# List (Mutable)
list1 = [1, 2, 3]
print(id(list1))
list1.append(4)  # Modifies the existing list
print(id(list1))  # Same memory address

# Dictionary (Mutable)
dict1 = {"name": "Alice", "age": 25}
print(id(dict1))
dict1["age"] = 26  # Modifies the existing dictionary
print(id(dict1))  # Same memory address

# Set (Mutable)
set1 = {1, 2, 3}
print(id(set1))
set1.add(4)  # Modifies the existing set
print(id(set1))  # Same memory address

# 4. Demonstrating Immutability in Function Arguments
def modify_string(s):
    print("Inside function before modification:", id(s))
    s += "!"  # Creates a new string object
    print("Inside function after modification:", id(s))

str_val = "Hello"
print("Outside before function call:", id(str_val))
modify_string(str_val)
print("Outside after function call:", id(str_val))  # Original remains unchanged

# 5. Demonstrating Mutability in Function Arguments
def modify_list(lst):
    print("Inside function before modification:", id(lst))
    lst.append(4)  # Modifies the original list
    print("Inside function after modification:", id(lst))

list_val = [1, 2, 3]
print("Outside before function call:", id(list_val))
modify_list(list_val)
print("Outside after function call:", id(list_val))  # Original list is modified

# 6. Copying Mutable Objects
# - Shallow Copy (References inner objects, changes reflect)
# - Deep Copy (Creates independent copies of nested objects)

import copy
nested_list = [[1, 2], [3, 4]]
shallow_copy = copy.copy(nested_list)  # Shallow copy
nested_list[0].append(99)  # Modifies original and affects shallow copy
print("Original List:", nested_list)
print("Shallow Copy:", shallow_copy)

deep_copy = copy.deepcopy(nested_list)  # Deep copy
nested_list[1].append(100)  # Modifies original but not deep copy
print("Original List:", nested_list)
print("Deep Copy:", deep_copy)

# 7. Converting Immutable to Mutable and Vice Versa
immutable_tuple = (1, 2, 3)
mutable_list = list(immutable_tuple)  # Convert tuple to list (mutable)
mutable_list.append(4)
immutable_tuple = tuple(mutable_list)  # Convert back to tuple (immutable)
print("Updated Immutable Tuple:", immutable_tuple)

mutable_list = [1, 2, 3]
immutable_frozenset = frozenset(mutable_list)  # Convert list to frozenset (immutable)
print("Immutable Frozenset:", immutable_frozenset)

# Summary:
# - Immutable: int, float, str, tuple, frozenset (Cannot be changed, new objects created)
# - Mutable: list, dict, set, bytearray (Can be changed in-place)
# - Functions: Immutable arguments remain unchanged, mutable arguments can be modified
# - Copying: Use deep copy to prevent unintended modifications in nested structures
