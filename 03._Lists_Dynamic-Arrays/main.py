# main.py
# (Including more detailed explanations for advanced concepts)

print("📚 **3. Lists (Dynamic Arrays)** 📚\n")

# --- 📌 Definition ---
print("--- 📌 Definition ---")
mixed_list = [1, "hello", True, 3.14, None]
print(f"A list can hold mixed data types: {mixed_list}")
print("Lists are ordered (maintain the order you add items).")
print("Lists are mutable (you can change them after creation).")
print("-" * 20) # Separator



# --- 🛠 1. Creation & Access ---
print("\n--- 🛠 1. Creation & Access ---")
fruits = ["apple", "banana", "cherry"]
print(f"Created list 'fruits': {fruits}")
print(f"Element at index 0: {fruits[0]}")
print(f"Element at index 2: {fruits[2]}")
print(f"Last element (index -1): {fruits[-1]}")
print(f"Second last element (index -2): {fruits[-2]}")
print("-" * 20) # Separator



# --- 🛠 2. Modifying Lists ---
print("\n--- 🛠 2. Modifying Lists ---")
fruits = ["apple", "banana", "cherry"]
print(f"Initial fruits list: {fruits}")
fruits.append("orange")
print(f"After append('orange'): {fruits}")
fruits.insert(1, "mango")
print(f"After insert(1, 'mango'): {fruits}")
more_fruits = ["kiwi", "grape"]
fruits.extend(more_fruits)
print(f"After extend(['kiwi', 'grape']): {fruits}")
last_item = fruits.pop()
print(f"Removed last item using pop(): '{last_item}'")
print(f"List after pop(): {fruits}")
item_at_index_1 = fruits.pop(1)
print(f"Removed item at index 1 using pop(1): '{item_at_index_1}'")
print(f"List after pop(1): {fruits}")
try:
    fruits.remove("apple")
    print(f"After remove('apple'): {fruits}")
except ValueError:
    print("'apple' was not found in the list.")
try:
    fruits.remove("pineapple")
    print(f"After remove('pineapple'): {fruits}")
except ValueError:
    print("'pineapple' was not found, so remove() raised a ValueError (as expected).")
print(f"\nList before sort: {fruits}")
fruits.sort()
print(f"After sort(): {fruits}")
fruits.reverse()
print(f"After reverse(): {fruits}")
print("-" * 20) # Separator



# --- 🛠 3. Other Useful Methods ---
print("\n--- 🛠 3. Other Useful Methods ---")
numbers = [1, 5, 2, 5, 3, 5]
print(f"Numbers list: {numbers}")
count_of_5 = numbers.count(5)
print(f"Count of '5' in numbers: {count_of_5}")
numbers_copy = numbers.copy()
print(f"Original numbers: {numbers}")
print(f"Copied numbers:   {numbers_copy}")
numbers_copy.append(100)
print(f"Modified copy:  {numbers_copy}")
print(f"Original is unchanged: {numbers}")
print(f"\nNumbers copy before clear: {numbers_copy}")
numbers_copy.clear()
print(f"Numbers copy after clear(): {numbers_copy}")
print("-" * 20) # Separator



# --- 💡 Examples ---
print("\n--- 💡 Examples ---")
# 1. Slicing
numbers = [10, 20, 30, 40, 50, 60]
print(f"\nSlicing on list: {numbers}")
print(f"numbers[1:4]: {numbers[1:4]}")
print(f"numbers[:3]: {numbers[:3]}")
print(f"numbers[2:]: {numbers[2:]}")
print(f"numbers[::2]: {numbers[::2]}")
print(f"numbers[::-1]: {numbers[::-1]}")
# 2. List Repetition & Concatenation
list_a = [1, 2]
list_b = [3, 4]
combined_list = list_a + list_b
print(f"\nConcatenation: {list_a} + {list_b} = {combined_list}")
repeated_list = ["Hi"] * 3
print(f"Repetition: ['Hi'] * 3 = {repeated_list}")
# 3. Checking Membership
current_fruits = ["banana", "cherry", "grape", "kiwi"]
print(f"\nMembership check in: {current_fruits}")
print(f"Is 'banana' in fruits? {'banana' in current_fruits}")
print(f"Is 'apple' in fruits? {'apple' in current_fruits}")
print(f"Is 'mango' not in fruits? {'mango' not in current_fruits}")
print("-" * 20) # Separator



# --- 📝 Key Notes ---
print("\n--- 📝 Key Notes ---")
print("1. Mutability: Lists can be changed after creation.")
key_list = [10, 20, 30]
print(f"   Original list: {key_list}")
key_list[0] = 99
print(f"   After changing index 0: {key_list}")
print("\n2. Performance:")
print("   - .append() / .pop() (from end) are generally fast.")
print("   - .insert() / .pop(i) / .remove() can be slower on large lists.")
print("\n3. Copying Importance:")
list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()
print(f"   list1 = {list1}")
print(f"   list2 = list1  (Points to same list)")
print(f"   list3 = list1.copy() (Is a new list)")
list2.append(4)
print(f"   After list2.append(4):")
print(f"      list1 = {list1}")
print(f"      list2 = {list2}")
print(f"      list3 = {list3} (unaffected)")
list3.append(5)
print(f"   After list3.append(5):")
print(f"      list1 = {list1}")
print(f"      list2 = {list2}")
print(f"      list3 = {list3}")
print("   => Use .copy() or list(original_list) to create independent copies.")
print("-" * 20) # Separator



# --- 🚀 Advanced Tricks (Detailed Explanations) ---
print("\n--- 🚀 Advanced Tricks (Detailed Explanations) ---")

# 1. List Comprehensions
print("\n**1. List Comprehensions**")
print("   A concise and often more readable way to create a NEW list.")
print("   It follows the pattern: [expression for item in iterable if condition]")
print("   The 'if condition' part is optional.")

# Example 1: Creating a list of squares
print("\n   * Example 1: Squares *")
# Traditional way using a for loop:
squares_loop = []
for x in range(5): # range(5) gives numbers 0, 1, 2, 3, 4
    squares_loop.append(x * x) # Calculate square and add to list
print(f"   Using a loop: {squares_loop}")

# Using list comprehension:
# Read as: "Create a new list containing 'x * x' for each 'x' in the sequence generated by range(5)."
squares_comp = [x * x for x in range(5)]
# Breakdown:
#   [        ]  => We are creating a new list.
#    x * x      => This is the 'expression'. What we want in the new list for each item.
#          for x in range(5) => This is the loop part. 'x' takes values 0, 1, 2, 3, 4.
print(f"   Using comprehension: {squares_comp}")
print("   Benefit: More compact code for simple list generation.")

# Example 2: Creating a list of even numbers with a condition
print("\n   * Example 2: Even Numbers (with condition) *")
# Traditional way using a for loop:
even_numbers_loop = []
for num in range(10): # range(10) gives 0, 1, 2, ..., 9
    if num % 2 == 0: # Check if the number is even (remainder when divided by 2 is 0)
        even_numbers_loop.append(num) # Add the even number to the list
print(f"   Using a loop: {even_numbers_loop}")

# Using list comprehension with a condition:
# Read as: "Create a new list containing 'num' for each 'num' in range(10) IF 'num % 2 == 0' is true."
even_numbers_comp = [num for num in range(10) if num % 2 == 0]
# Breakdown:
#   [        ]  => We are creating a new list.
#    num        => This is the 'expression'. We want the number itself in the list.
#        for num in range(10) => This is the loop part. 'num' takes values 0 through 9.
#                      if num % 2 == 0 => This is the 'condition'. Only include 'num' if it's even.
print(f"   Using comprehension: {even_numbers_comp}")
print("   Benefit: Combines loop and conditional logic concisely.")

# ---
print("\n**2. Nested Lists**")
print("   A list that contains other lists as its elements.")
print("   Useful for representing grids, matrices, or structured data.")

# Example: A 3x3 matrix
print("\n   * Example: A 3x3 Matrix *")
matrix = [
    [1, 2, 3],  # Row 0 (This is the first element of 'matrix', which is a list)
    [4, 5, 6],  # Row 1 (This is the second element of 'matrix')
    [7, 8, 9]   # Row 2 (This is the third element of 'matrix')
]
print(f"   Nested list (matrix):\n   {matrix[0]}\n   {matrix[1]}\n   {matrix[2]}")
print(f"   The whole matrix list: {matrix}")

# Accessing elements in a nested list
print("\n   * Accessing Elements *")
print("   Use multiple index brackets: outer_list[row_index][column_index]")

# Get the element in the second row (index 1) and third column (index 2)
row_index = 1
col_index = 2
element = matrix[row_index][col_index]
# How it works:
# 1. matrix[row_index] => matrix[1] => This gets the list at index 1 of 'matrix', which is [4, 5, 6]
# 2. (...)[col_index] => [4, 5, 6][2] => This gets the element at index 2 of the inner list [4, 5, 6], which is 6
print(f"   Element at matrix[{row_index}][{col_index}]: {element}") # Should be 6

# Get the first row (which is a list itself)
first_row = matrix[0]
print(f"   Getting the first row (matrix[0]): {first_row}") # Should be [1, 2, 3]

# Get the first element of the first row
element_0_0 = matrix[0][0]
print(f"   Element at matrix[0][0]: {element_0_0}") # Should be 1
print("-" * 20) # Separator


print("\nEnd of Detailed Advanced Tricks!")
print("\nEnd of Lists (Dynamic Arrays)!")
