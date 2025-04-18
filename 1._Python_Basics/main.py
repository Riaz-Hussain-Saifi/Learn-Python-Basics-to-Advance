# main.py
# This file demonstrates the basic Python concepts outlined in README.md


# -------------------------------------
# 1.1 Printing & Memory Check
# -------------------------------------
print("--- 1.1 Printing & Memory Check ---")
print("Hello, Python!")  # Basic print statement

name_example = "Riaz"
print(f"The variable 'name_example' contains: {name_example}")
print(f"The memory address (id) of 'name_example' is: {id(name_example)}")
print("-" * 20) # Separator



# -------------------------------------
# 1.2 Comments
# -------------------------------------
print("--- 1.2 Comments ---")
# This is a single-line comment. It's ignored by the interpreter.
print("Single-line comments start with #")

"""
This is a multi-line comment (technically a docstring when used like this).
It can span multiple lines and is often used for documentation.
Python ignores string literals that are not assigned to a variable.
"""
print("Multi-line comments can be enclosed in triple quotes.")
print("-" * 20) # Separator



# -------------------------------------
# 1.3 Data Types & Variables
# -------------------------------------
print("--- 1.3 Data Types & Variables ---")
# Using type hints (PEP-8 recommends snake_case for variable names)
first_name: str = "Riaz"
user_age: int = 28
user_height: float = 5.9
is_learning: bool = True

# Examples of other common types
my_list: list = [1, "apple", 3.14]
my_tuple: tuple = (1, "banana", 3.14) # Tuples are immutable
my_set: set = {1, "cherry", 3.14, 1} # Sets store unique items, order not guaranteed
my_dict: dict = {"name": "Alice", "age": 30} # Key-value pairs

print(f"String: {first_name} (Type: {type(first_name)})")
print(f"Integer: {user_age} (Type: {type(user_age)})")
print(f"Float: {user_height} (Type: {type(user_height)})")
print(f"Boolean: {is_learning} (Type: {type(is_learning)})")
print(f"List: {my_list} (Type: {type(my_list)})")
print(f"Tuple: {my_tuple} (Type: {type(my_tuple)})")
print(f"Set: {my_set} (Type: {type(my_set)})") # Note: duplicate 1 is removed
print(f"Dictionary: {my_dict} (Type: {type(my_dict)})")
print("-" * 20) # Separator



# -------------------------------------
# 1.4 Operators
# -------------------------------------
print("--- 1.4 Operators ---")
a, b = 5, 10
c = 3
my_string = "hello world"
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

# Arithmetic
print("Arithmetic Operators:")
print(f"{a} + {b} = {a + b}")
print(f"{b} - {a} = {b - a}")
print(f"{a} * {c} = {a * c}")
print(f"{b} / {a} = {b / a}") # Standard division
print(f"{a} ** {c} = {a ** c}") # Exponentiation (5^3)
print(f"{b} // {c} = {b // c}") # Floor division (result is integer)
print(f"{b} % {c} = {b % c}") # Modulus (remainder)

# Comparison
print("\nComparison Operators:")
print(f"{a} == {c * 2 - 1}? {a == c * 2 - 1}") # Equal to (5 == 5) -> True
print(f"{a} != {b}? {a != b}") # Not equal to -> True
print(f"{a} > {c}? {a > c}")   # Greater than -> True
print(f"{a} < {b}? {a < b}")   # Less than -> True
print(f"{a} >= 5? {a >= 5}")   # Greater than or equal to -> True
print(f"{b} <= {a}? {b <= a}") # Less than or equal to -> False

# Logical
print("\nLogical Operators:")
print(f"{a} < {b} and {a} != {b}? {a < b and a != b}") # True and True -> True
print(f"{a} > {b} or {c} < {a}? {a > b or c < a}")   # False or True -> True
print(f"not ({a} == {b})? {not (a == b)}")           # not False -> True

# Membership
print("\nMembership Operators:")
print(f"'world' in '{my_string}'? {'world' in my_string}") # True
print(f"'python' not in '{my_string}'? {'python' not in my_string}") # True
print(f"1 in {list_a}? {1 in list_a}") # True
print(f"4 not in {list_a}? {4 not in list_a}") # True

# Identity
print("\nIdentity Operators:")
print(f"list_a is list_c? {list_a is list_c}") # True - list_c points to the same object as list_a
print(f"list_a is list_b? {list_a is list_b}") # False - list_a and list_b have same content but are different objects
print(f"list_a == list_b? {list_a == list_b}") # True - Contents are the same (value equality)
print(f"list_a is not list_b? {list_a is not list_b}") # True - They are different objects

# Note: For small integers and strings, Python often reuses objects, so 'is' might be True unexpectedly.
x = 5
y = 5
print(f"x = 5, y = 5. x is y? {x is y}") # Often True due to Python optimization

print("-" * 20) # Separator



# -------------------------------------
# 1.5 Input from User
# -------------------------------------
print("--- 1.5 Input from User ---")
# Use a try-except block to prevent errors if the script is run non-interactively
try:
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    user_age_str = input("Enter your age: ")
    # Input is always a string, convert if needed
    try:
        user_age_int = int(user_age_str)
        print(f"You will be {user_age_int + 1} next year.")
    except ValueError:
        print("Invalid age entered. Please enter a number.")

except EOFError:
    print("\nSkipping input section (likely running in a non-interactive environment).")

print("-" * 20) # Separator
print("End of basic Python examples.")
