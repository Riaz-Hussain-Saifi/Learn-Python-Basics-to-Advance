# ✨ **8. Comprehensions**  
*Concise syntax to create **lists**, **sets**, and **dictionaries** in one line.*

---

## 📌 **Definition**  
- **Pythonic** way to transform/filter iterables.  
- **Faster** than traditional loops for simple operations.  
- Available for:  
  - **Lists**: `[expression for item in iterable]`  
  - **Sets**: `{expression for item in iterable}`  
  - **Dictionaries**: `{key: value for item in iterable}`  

---

## 🔹 **8.1 List Comprehension**  
### **Basic Syntax**  
```python
[expression for item in iterable if condition]
```

### **Examples**  
| Use Case          | Example                          | Output                     |  
|-------------------|----------------------------------|----------------------------|  
| **Squaring**      | `[x**2 for x in range(5)]`       | `[0, 1, 4, 9, 16]`         |  
| **Filtering**     | `[x for x in range(10) if x % 2 == 0]` | `[0, 2, 4, 6, 8]` |  
| **Transforming**  | `[word.upper() for word in ["hello", "world"]]` | `["HELLO", "WORLD"]` |  

**Code:**  
```python
# Squaring numbers
squared = [x**2 for x in range(10)]  

# Filtering even numbers
evens = [x for x in range(20) if x % 2 == 0]  

# Uppercasing strings
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]  
```

---

## 🔹 **8.2 Set & Dictionary Comprehension**  
### **Set Comprehension**  
```python
{expression for item in iterable if condition}
```  
**Example:**  
```python
# Remove duplicates
numbers = [1, 2, 2, 3, 4, 4]
unique_nums = {x for x in numbers}  # Output: {1, 2, 3, 4}
```

### **Dictionary Comprehension**  
```python
{key: value for item in iterable if condition}
```  
**Examples:**  
| Use Case          | Example                          | Output                     |  
|-------------------|----------------------------------|----------------------------|  
| **Squaring Map**  | `{x: x**2 for x in range(5)}`    | `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}` |  
| **Word Count**    | `{word: sentence.count(word) for word in sentence.split()}` | `{"hello": 2, "world": 1}` |  

**Code:**  
```python
# Create a squared mapping
squared_dict = {x: x**2 for x in range(5)}  

# Count word occurrences
sentence = "hello world hello python"
word_count = {word: sentence.split().count(word) for word in sentence.split()}  
```

---

## 🚀 **Why Use Comprehensions?**  
1. **Conciseness**: Replace 3-4 lines of loops with one line.  
2. **Readability**: Clear intent for transformations/filters.  
3. **Performance**: Often faster than equivalent `for` loops.  

---

## 📝 **Key Notes**  
- **Avoid Nested Complexity**: Use traditional loops for multi-step logic.  
- **Memory Efficiency**: Generator expressions (`(x for x in iterable)`) save memory for large data.  
- **PEP 8**: Break long comprehensions into multiple lines for readability:  
  ```python
  results = [
      x**2 
      for x in range(100) 
      if x % 2 == 0
  ]
  ```

---

## 🛠 **Practical Use Cases**  
1. **Flattening a Matrix**:  
   ```python
   matrix = [[1, 2], [3, 4], [5, 6]]
   flat = [num for row in matrix for num in row]  # Output: [1, 2, 3, 4, 5, 6]
   ```  
2. **Conditional Dictionary**:  
   ```python
   users = {"Alice": 28, "Bob": 15, "Charlie": 35}
   adults = {name: age for name, age in users.items() if age >= 18}  # Output: {"Alice": 28, "Charlie": 35}
   ```  

--- 