# main.py
# This file demonstrates the concepts of Python functions as explained in README.md,
# covering different parameter types: positional, *args, keyword arguments (with defaults),
# and **kwargs.

print("--- Python Functions Demo ---")



# --------------------------------------------------
# 1. Basic Function Definition & Call (from README)
# --------------------------------------------------
print("\n--- 1. Basic Function Definition & Call ---")

def greet(name: str) -> str:
    """
    A basic function definition.
    Accepts one positional argument 'name'.
    Uses type hints (name: str) -> str for clarity.
    Returns a formatted string.
    """
    return f"Hello, {name}"

# Calling the function
print("Calling greet('Riaz')...")
message = greet("Riaz")
print(f"Output: {message}") # Output: Hello, Riaz



# --------------------------------------------------
# 2. Parameter Types in Python Functions
# --------------------------------------------------
print("\n--- 2. Parameter Types ---")

# --- 2.1 Positional Arguments (Required) ---
print("\n### 2.1 Positional Arguments (Required) ###")
# These arguments must be provided when calling the function,
# and their order matters.

def describe_pet(animal_type, pet_name):
    """Displays information about a pet using required positional arguments."""
    print(f"I have a {animal_type} named {pet_name}.")

print("Calling describe_pet('dog', 'Buddy')...")
describe_pet('dog', 'Buddy') # Output: I have a dog named Buddy.
# describe_pet('cat') # This would raise a TypeError: missing 1 required positional argument: 'pet_name'

# --- 2.2 Arbitrary Positional Arguments (*args) ---
print("\n### 2.2 Arbitrary Positional Arguments (*args) ###")
# Allows a function to accept any number of extra positional arguments.
# These arguments are collected into a tuple.

def summarize_items(category, *items):
    """Summarizes items in a category using *args."""
    print(f"\nCategory: {category}")
    if items:
        print("Items:")
        for item in items:
            print(f"- {item}")
    else:
        print("No extra items provided.")
    print(f"(*args captured: {items})") # Shows the tuple

print("Calling summarize_items('Fruits', 'Apple', 'Banana', 'Cherry')...")
summarize_items('Fruits', 'Apple', 'Banana', 'Cherry')
# Output:
# Category: Fruits
# Items:
# - Apple
# - Banana
# - Cherry
# (*args captured: ('Apple', 'Banana', 'Cherry'))

print("\nCalling summarize_items('Vegetables')...")
summarize_items('Vegetables')
# Output:
# Category: Vegetables
# No extra items provided.
# (*args captured: ())

# --- 2.3 Keyword Arguments (Default Values) ---
print("\n### 2.3 Keyword Arguments (Default Values) ###")
# Arguments defined with a default value in the function signature.
# They become optional when calling the function.
# Can be passed positionally or using their keyword name.

def power_level(character, level=100, unit="points"):
    """Describes a character's power level, with default values."""
    print(f"{character} has a power level of {level} {unit}.")

print("Calling power_level('Goku')... (uses defaults)")
power_level('Goku') # Output: Goku has a power level of 100 points.

print("\nCalling power_level('Vegeta', 9001)... (overrides level)")
power_level('Vegeta', 9001) # Output: Vegeta has a power level of 9001 points.

print("\nCalling power_level('Frieza', unit='scouters', level=530000)... (overrides both using keywords)")
power_level('Frieza', unit='scouters', level=530000) # Output: Frieza has a power level of 530000 scouters.

# --- 2.4 Arbitrary Keyword Arguments (**kwargs) ---
print("\n### 2.4 Arbitrary Keyword Arguments (**kwargs) ###")
# Allows a function to accept any number of extra keyword arguments.
# These arguments are collected into a dictionary.

def build_profile(first_name, last_name, **user_info):
    """Builds a user profile using required args and **kwargs."""
    profile = {'first': first_name, 'last': last_name}
    print(f"\nBuilding profile for {first_name} {last_name}...")
    if user_info:
        print("Additional Info:")
        for key, value in user_info.items():
            print(f"- {key}: {value}")
            profile[key] = value # Add to the main profile dict
    else:
        print("No additional info provided.")
    print(f"(**kwargs captured: {user_info})") # Shows the dictionary
    # return profile # Optionally return the complete profile

print("Calling build_profile('Ada', 'Lovelace', field='Mathematics', title='Countess')...")
build_profile('Ada', 'Lovelace', field='Mathematics', title='Countess')
# Output:
# Building profile for Ada Lovelace...
# Additional Info:
# - field: Mathematics
# - title: Countess
# (**kwargs captured: {'field': 'Mathematics', 'title': 'Countess'})

print("\nCalling build_profile('Charles', 'Babbage')...")
build_profile('Charles', 'Babbage')
# Output:
# Building profile for Charles Babbage...
# No additional info provided.
# (**kwargs captured: {})



# --------------------------------------------------
# 3. Complete Example: Mixing All Parameter Types (from README)
# --------------------------------------------------
print("\n--- 3. Complete Example: Mixing All Parameter Types ---")
# Demonstrates the standard order:
# 1. Positional arguments
# 2. *args
# 3. Keyword arguments (with or without defaults)
# 4. **kwargs

def demo(a, b, *args, greeting="Hello", **kwargs):
    """
    A function demonstrating the combination of all parameter types.
    - a, b: Required positional arguments.
    - *args: Captures extra positional arguments.
    - greeting: A keyword argument with a default value.
    - **kwargs: Captures extra keyword arguments.
    """
    print("\n--- Inside demo function ---")
    print(f"Positional (Required): a={a}, b={b}")
    print(f"Extra positional (*args): {args}")
    print(f"Keyword arg (Default/Override): greeting='{greeting}'")
    print(f"Extra keyword (**kwargs): {kwargs}")
    print("--------------------------")

# Function call with mixed arguments (matches README example)
print("Calling demo(10, 20, 30, 40, greeting='Hi', extra='value')")
demo(10, 20, 30, 40, greeting="Hi", extra="value")
# Expected Output (similar to README):
# --- Inside demo function ---
# Positional (Required): a=10, b=20
# Extra positional (*args): (30, 40)
# Keyword arg (Default/Override): greeting='Hi'
# Extra keyword (**kwargs): {'extra': 'value'}
# --------------------------

# Another call with different arguments
print("\nCalling demo(1, 2, 'x', 'y', 'z', status='active', id=99)")
demo(1, 2, 'x', 'y', 'z', status='active', id=99)
# Expected Output:
# --- Inside demo function ---
# Positional (Required): a=1, b=2
# Extra positional (*args): ('x', 'y', 'z')
# Keyword arg (Default/Override): greeting='Hello'  (Uses default)
# Extra keyword (**kwargs): {'status': 'active', 'id': 99}
# --------------------------

# Call with only required arguments
print("\nCalling demo(5, 6)")
demo(5, 6)
# Expected Output:
# --- Inside demo function ---
# Positional (Required): a=5, b=6
# Extra positional (*args): ()
# Keyword arg (Default/Override): greeting='Hello'
# Extra keyword (**kwargs): {}
# --------------------------

print("\n--- End of Demo ---")
