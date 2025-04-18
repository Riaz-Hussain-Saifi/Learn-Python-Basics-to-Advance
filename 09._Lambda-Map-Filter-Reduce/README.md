# 🔧 **9. Lambda, Map, Filter, Reduce**  
*Functional programming tools for concise data transformations.*

---

## 📌 **9.1 Lambda (Anonymous Function)**  
### **Definition**  
- Inline, unnamed function defined with `lambda`.  
- Syntax: `lambda arguments: expression`.  

### **Examples**  
```python
# Basic lambda
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

# Sort a list of tuples by the second element
pairs = [(1, 'z'), (2, 'a'), (3, 'b')]
pairs.sort(key=lambda x: x[1])  # Sorts by the string: [(2, 'a'), (3, 'b'), (1, 'z')]
```

---

## 📌 **9.2 Map**  
### **Definition**  
- Applies a function to all items in an iterable.  
- Syntax: `map(function, iterable)`.  

### **Examples**  
```python
numbers = [1, 2, 3, 4]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))  # Output: [1, 4, 9, 16]

# Convert strings to uppercase
words = ["hello", "world"]
uppercase = list(map(str.upper, words))  # Output: ["HELLO", "WORLD"]
```

---

## 📌 **9.3 Filter**  
### **Definition**  
- Filters items based on a condition (returns `True`/`False`).  
- Syntax: `filter(function, iterable)`.  

### **Examples**  
```python
numbers = [1, 2, 3, 4, 5, 6]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))  # Output: [2, 4, 6]

# Filter non-empty strings
words = ["hello", "", "world", ""]
non_empty = list(filter(None, words))  # Output: ["hello", "world"]
```

---

## 📌 **9.4 Reduce**  
### **Definition**  
- Applies a rolling computation to sequential pairs.  
- Syntax: `reduce(function, iterable[, initializer])`.  
- Requires `from functools import reduce`.  

### **Examples**  
```python
from functools import reduce

numbers = [1, 2, 3, 4]

# Sum all numbers
sum_all = reduce(lambda x, y: x + y, numbers)  # Output: 10

# Find the maximum
max_num = reduce(lambda x, y: x if x > y else y, numbers)  # Output: 4
```

---

## 🚀 **Key Comparisons**  
| Tool       | Use Case                          | Lambda Example                  | Equivalent List Comprehension     |  
|------------|-----------------------------------|---------------------------------|-----------------------------------|  
| `map`      | Transform all items               | `map(lambda x: x*2, [1,2,3])`  | `[x*2 for x in [1,2,3]]`          |  
| `filter`   | Select items meeting a condition  | `filter(lambda x: x>1, [1,2,3])`| `[x for x in [1,2,3] if x>1]`     |  
| `reduce`   | Aggregate values (e.g., sum)      | `reduce(lambda x,y: x+y, [1,2,3])` | N/A (requires loop)             |  

---

## 📝 **Best Practices**  
1. **Use `lambda` for simple one-off functions**.  
2. **Prefer list comprehensions** for readability when possible.  
3. **Combine tools**:  
   ```python
   from functools import reduce
   # Sum of squares of even numbers
   result = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
   print(result)  # Output: 20 (4 + 16)
   ```

---

## 🛠 **Practical Use Cases**  
1. **Data Processing Pipeline**:  
   ```python
   # Convert to int, filter negatives, then sum
   data = ["1", "2", "-3", "4"]
   result = reduce(
       lambda x, y: x + y,
       filter(
           lambda x: x > 0,
           map(int, data)
       )
   )
   print(result)  # Output: 7 (1 + 2 + 4)
   ```

2. **Dictionary Aggregation**:  
   ```python
   words = ["apple", "banana", "apple"]
   word_count = reduce(
       lambda d, word: {**d, word: d.get(word, 0) + 1},
       words,
       {}
   )
   print(word_count)  # Output: {"apple": 2, "banana": 1}
   ```

--- 