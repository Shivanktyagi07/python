"""
Python Typecasting (Type Conversion) - Notes with Code Examples
"""

# 1. Implicit Typecasting (Automatically done by Python)
a = 10   # Integer
b = 2.5  # Float
c = a + b  # Python converts 'a' to float automatically
print(type(c))  # Output: <class 'float'>

# 2. Explicit Typecasting (Manual conversion)
int_val = 100
float_val = float(int_val)  # Converting int to float
string_val = str(int_val)  # Converting int to string
bool_val = bool(int_val)  # Converting int to boolean (Non-zero -> True)

# 3. Converting Strings to Numbers
num_str = "123"
int_from_str = int(num_str)  # String to integer
float_from_str = float(num_str)  # String to float

# 4. Handling Invalid String Conversions
invalid_str = "123abc"
# int(invalid_str)  # ❌ This will throw a ValueError

# 5. Boolean Typecasting
bool_true = bool(1)  # True
bool_false = bool(0)  # False
bool_empty = bool("")  # False (Empty string)
bool_nonempty = bool("Hello")  # True (Non-empty string)

# 6. List, Tuple, Set Typecasting
list1 = [1, 2, 3]
tuple_from_list = tuple(list1)  # List to Tuple
set_from_list = set(list1)  # List to Set
list_from_tuple = list(tuple_from_list)  # Tuple to List

# 7. Dictionary Typecasting (Using `dict()`)
pair_list = [(1, "one"), (2, "two"), (3, "three")]
dict_from_list = dict(pair_list)  # Converting list of tuples to dictionary

# 8. Converting ASCII Character to Integer (Using `ord()` and `chr()`)
char_val = 'A'
char_to_ascii = ord(char_val)  # ASCII value of 'A' (65)
ascii_to_char = chr(65)  # Converts ASCII 65 back to 'A'

# 9. Binary, Octal, and Hexadecimal Conversions
bin_num = bin(10)  # Binary representation ('0b1010')
oct_num = oct(10)  # Octal representation ('0o12')
hex_num = hex(10)  # Hexadecimal representation ('0xa')

# 10. Converting Binary, Octal, Hex to Integer
int_from_bin = int("1010", 2)  # Binary to integer (10)
int_from_oct = int("12", 8)  # Octal to integer (10)
int_from_hex = int("a", 16)  # Hexadecimal to integer (10)

# 11. Using `eval()` for Safe String Conversion (Be Cautious!)
expr = "10 + 20"
eval_result = eval(expr)  # Evaluates expression as Python code (30)

# 12. Converting List of Strings to Integers
str_list = ["1", "2", "3"]
int_list = list(map(int, str_list))  # Converts list of strings to list of integers

# 13. Converting Iterable to String
iterable = [1, 2, 3]
str_from_iterable = "-".join(map(str, iterable))  # '1-2-3'

# 14. Complex Number Typecasting
real = 3
imaginary = 5
complex_num = complex(real, imaginary)  # 3 + 5j

# 15. JSON String to Python Dictionary (Using `json.loads()`)
import json
json_str = '{"name": "Alice", "age": 25}'
dict_from_json = json.loads(json_str)  # Converts JSON string to dictionary

# 16. Dictionary to JSON String (Using `json.dumps()`)
json_from_dict = json.dumps(dict_from_json)  # Converts dictionary to JSON string

# 17. Bytes and String Conversion
byte_str = b"Hello"  # Byte representation of a string
string_from_bytes = byte_str.decode("utf-8")  # Convert bytes to string
string_to_bytes = "Hello".encode("utf-8")  # Convert string to bytes

# 18. Using `astype()` in NumPy for Efficient Typecasting
import numpy as np
np_array = np.array([1.5, 2.3, 3.7])
int_np_array = np_array.astype(int)  # Converts float array to integer array

# 19. Pandas Type Conversion (Using `astype()` and `to_numeric()`)
import pandas as pd
data = pd.Series(["1", "2", "3"])
int_data = data.astype(int)  # Converts Series to integers

# 20. Converting Timestamp to Datetime
from datetime import datetime
timestamp = 1672531199
date_time = datetime.fromtimestamp(timestamp)  # Converts UNIX timestamp to datetime

# Print examples for testing
print("Converted Float:", float_val)
print("Converted Boolean:", bool_val)
print("Converted Tuple:", tuple_from_list)
print("Converted Dict:", dict_from_list)
print("ASCII Value:", char_to_ascii)
print("Binary Representation:", bin_num)
print("Evaluated Expression:", eval_result)
print("JSON to Dict:", dict_from_json)
print("Bytes to String:", string_from_bytes)
print("NumPy Array Typecasted:", int_np_array)
