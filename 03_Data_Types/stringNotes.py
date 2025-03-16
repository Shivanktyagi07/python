"""
Python Strings - Notes with Code Examples
"""

# 1. Creating Strings
string1 = "Hello, World!"  # Using double quotes
string2 = 'Python is awesome'  # Using single quotes
string3 = """This is a 
multi-line string"""  # Triple-quoted multi-line string

# 2. Accessing Characters in a String
char = string1[0]  # First character ('H')
last_char = string1[-1]  # Last character ('!')

# 3. Slicing Strings
substring = string1[0:5]  # 'Hello'
reverse_string = string1[::-1]  # Reverse string

# 4. String Concatenation and Repetition
concatenated = string1 + " " + string2  # Combining strings
repeated = "Python " * 3  # Repeating a string

# 5. String Formatting
name = "John"
age = 25
formatted1 = "My name is {} and I am {} years old".format(name, age)  # Using format()
formatted2 = f"My name is {name} and I am {age} years old"  # f-string (Python 3.6+)

# 6. Common String Methods
upper_case = string1.upper()  # Convert to uppercase
lower_case = string1.lower()  # Convert to lowercase
strip_string = "  Python  ".strip()  # Removes leading/trailing whitespace
replaced_string = string1.replace("World", "Python")  # Replace substring
split_string = "apple,banana,orange".split(",")  # Splitting into a list
joined_string = "-".join(["Python", "is", "fun"])  # Joining list elements

# 7. Checking Substring Presence
contains_word = "Python" in string2  # Returns True

# 8. String Encoding and Decoding
utf8_encoded = string1.encode("utf-8")  # Convert string to bytes
utf8_decoded = utf8_encoded.decode("utf-8")  # Convert bytes back to string

# 9. Advanced String Formatting
pi_value = 3.14159
formatted_pi = "{:.2f}".format(pi_value)  # Rounds to 2 decimal places
formatted_pi_f = f"{pi_value:.2f}"  # Using f-string formatting

# 10. Regular Expressions with Strings (Advanced)
import re
pattern = r"\d+"  # Pattern to find digits in a string
text = "My phone number is 12345"
matches = re.findall(pattern, text)  # Returns ['12345']

# 11. Raw Strings (Useful for Regex)
raw_string = r"C:\\Users\\Name"  # Avoids escaping backslashes

# 12. String Interpolation (Legacy, but still used)
legacy_format = "My name is %s and I am %d years old" % (name, age)  # Old-style formatting

# 13. String Translation Table (Useful for replacing multiple characters)
trans_table = str.maketrans("aeiou", "12345")  # Replace vowels with numbers
translated_string = "hello".translate(trans_table)  # 'h2ll4'

# 14. Checking String Properties
is_alpha = "Python".isalpha()  # Checks if all characters are alphabets
is_digit = "1234".isdigit()  # Checks if all characters are digits
is_alnum = "Python123".isalnum()  # Checks if alphanumeric

# 15. Mutable String Alternative (Using list)
mutable_string = list("Python")
mutable_string[0] = "J"  # Changing 'P' to 'J'
new_string = "".join(mutable_string)  # 'Jython'

# 16. String Buffer for Performance (Using io.StringIO)
import io
buffer = io.StringIO()
buffer.write("Efficient ")
buffer.write("String Handling")
optimized_string = buffer.getvalue()

# 17. Casefold (Stronger lowercase conversion)
casefolded = "ß".casefold()  # Converts German ß to ss

# 18. Unicode and Special Characters
unicode_string = "Hello \u2605"  # Unicode star character
emoji_string = "Python is fun \U0001F600"  # Smiley emoji

# 19. Removing Punctuation using Translation Table
import string
translator = str.maketrans("", "", string.punctuation)
cleaned_string = "Hello, World!".translate(translator)  # 'Hello World'

# 20. Reversing Words in a Sentence
sentence = "Python is awesome"
reversed_sentence = " ".join(sentence.split()[::-1])  # 'awesome is Python'

# 21. Finding Substring Index
index = string1.find("World")  # Returns index of 'World', -1 if not found

# 22. Count Occurrences of a Substring
count = "banana".count("a")  # Returns 3

# 23. Checking Start and End of a String
starts_with = string1.startswith("Hello")  # True
ends_with = string1.endswith("!")  # True

# 24. Multi-line String Processing
multiline_text = """Line1
Line2
Line3""".splitlines()  # ['Line1', 'Line2', 'Line3']

# 25. String Padding
padded_string = "Python".center(20, "*")  # '*******Python*******'
left_padded = "Python".rjust(10, "-")  # '----Python'
right_padded = "Python".ljust(10, "-")  # 'Python----'

# 26. Checking Unicode Normalization
import unicodedata
normalized = unicodedata.normalize("NFKC", "café")  # Normalizes accents, ligatures

# 27. Efficient String Search (Using re.compile for performance)
compiled_pattern = re.compile(r"\bPython\b")  # Matches whole word 'Python'
search_result = compiled_pattern.search("I love Python!")  # Returns match object

# Print examples for testing
print("Formatted String:", formatted1)
print("Upper Case:", upper_case)
print("Reversed String:", reverse_string)
print("Matches:", matches)
print("Translated String:", translated_string)
print("Optimized String:", optimized_string)
print("Emoji String:", emoji_string)
print("Padded String:", padded_string)
