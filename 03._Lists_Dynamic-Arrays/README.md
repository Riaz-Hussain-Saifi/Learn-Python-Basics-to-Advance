# 📚 **3. Lists (Dynamic Arrays)**  
*Ordered, mutable collections of items in Python.*  

---

## 📌 **Definition**  
- **Lists** are **ordered**, **mutable** (changeable) sequences.  
- Can store **mixed data types** (e.g., `[1, "apple", True]`).  
- Similar to arrays in other languages but more flexible.  

---

## 🛠 **Common Operations**  

### **1. Creation & Access**  
```python
my_list = [1, 2, 3]          # Create a list  
print(my_list[0])             # Output: 1 (access by index)  
print(my_list[-1])            # Output: 3 (negative index = from end)  
```

### **2. Modifying Lists**  
| Method          | Example                          | Action                           |  
|-----------------|----------------------------------|----------------------------------|  
| `.append(x)`    | `fruits.append("orange")`        | Adds `x` to the **end**.         |  
| `.insert(i, x)` | `fruits.insert(1, "mango")`      | Inserts `x` at index `i`.        |  
| `.extend(L)`    | `fruits.extend(["kiwi", "grape"])`| Merges list `L` into the list.   |  
| `.pop()`        | `fruits.pop()`                   | Removes/returns **last item**.   |  
| `.pop(i)`       | `fruits.pop(1)`                  | Removes/returns item at index `i`. |  
| `.remove(x)`    | `fruits.remove("apple")`         | Removes **first occurrence** of `x`. |  
| `.sort()`       | `fruits.sort()`                  | Sorts the list **in-place**.     |  
| `.reverse()`    | `fruits.reverse()`               | Reverses the list **in-place**.  |  

**Example:**  
```python
fruits = ["apple", "banana", "cherry"]  
fruits.append("orange")  
fruits.insert(1, "mango")  
fruits.extend(["kiwi", "grape"])  
fruits.pop()        # Removes "grape"  
fruits.pop(1)       # Removes "mango"  
fruits.remove("apple")  
fruits.sort()       # Sorts alphabetically  
print(fruits)       # Output: ["banana", "cherry", "kiwi", "orange"]  
```

### **3. Other Useful Methods**  
| Method          | Example                          | Output/Effect                   |  
|-----------------|----------------------------------|---------------------------------|  
| `.count(x)`     | `[1, 2, 2, 3].count(2)`          | `2` (counts occurrences of `x`) |  
| `.clear()`      | `fruits.clear()`                 | `[]` (empties the list)         |  
| `.copy()`       | `new_list = fruits.copy()`       | Creates a **shallow copy**.     |  
| **Slicing**     | `[1, 2, 3, 4][1:3]`              | `[2, 3]` (subset of list)       |  
| **Repetition**  | `[0] * 3`                        | `[0, 0, 0]`                     |  

---

## 💡 **Examples**  

### **1. Slicing**  
```python
numbers = [10, 20, 30, 40, 50]  
print(numbers[1:4])    # Output: [20, 30, 40] (indices 1 to 3)  
print(numbers[:3])     # Output: [10, 20, 30] (start to index 2)  
print(numbers[2:])     # Output: [30, 40, 50] (index 2 to end)  
```

### **2. List Repetition & Concatenation**  
```python
print([1, 2] + [3, 4])   # Output: [1, 2, 3, 4] (concatenation)  
print(["Hi"] * 3)        # Output: ["Hi", "Hi", "Hi"]  
```

### **3. Checking Membership**  
```python
fruits = ["apple", "banana"]  
print("banana" in fruits)   # Output: True  
print("mango" not in fruits) # Output: True  
```

---

## 📝 **Key Notes**  
- **Mutability**: Lists can be modified after creation (unlike tuples).  
- **Performance**:  
  - `append()`/`pop()` are **O(1)** (fast).  
  - `insert()`/`remove()` are **O(n)** (slow for large lists).  
- **Copying**: Use `.copy()` or `list(old_list)` to avoid modifying the original list.  

---

## 🚀 **Advanced Tricks**  
- **List Comprehensions**:  
  ```python
  squares = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]  
  ```  
- **Nested Lists**:  
  ```python
  matrix = [[1, 2], [3, 4]]  
  print(matrix[0][1])  # Output: 2  
  ```  

--- 
