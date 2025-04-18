# 🔄 **4. Loops in Python**  
*Automate repetitive tasks using `for` and `while` loops.*  

---

## 🔹 **4.1 For Loop**  
### **Definition**  
- Iterates over a **sequence** (list, tuple, string, etc.).  
- Uses the syntax: `for item in sequence:`.  

### **Examples**  
#### Basic Iteration:  
```python
my_list = [1, 2, 3, 4, 5]  
for item in my_list:  
    print(item)  
```  
**Output**:  
```
1  
2  
3  
4  
5  
```  

#### Using `enumerate()` (Index + Value):  
```python
for index, value in enumerate(my_list):  
    print(f"Index {index}: {value}")  
```  
**Output**:  
```
Index 0: 1  
Index 1: 2  
Index 2: 3  
Index 3: 4  
Index 4: 5  
```  

#### Iterating Over a Range:  
```python
for i in range(3):  # 0 to 2  
    print(i)  
```  

---

## 🔹 **4.2 While Loop**  
### **Definition**  
- Executes **while a condition is `True`**.  
- Requires **manual counter updates** to avoid infinite loops.  

### **Example**  
```python
count = 1  
while count <= 5:  
    print(count)  
    count += 1  # Increment to exit loop  
```  
**Output**:  
```
1  
2  
3  
4  
5  
```  

#### Breaking a Loop Early:  
```python
while True:  
    user_input = input("Type 'quit' to exit: ")  
    if user_input == "quit":  
        break  # Exit loop immediately  
```  

---

## 🔹 **4.3 Else with Loops**  
### **Definition**  
- The `else` block runs **only if the loop completes naturally** (no `break`).  
- Works with both `for` and `while` loops.  

### **Example**  
```python
for i in range(3):  
    print(i)  
else:  
    print("Loop completed!")  # Executes after full iteration  
```  
**Output**:  
```
0  
1  
2  
Loop completed!  
```  

#### Contrast with `break`:  
```python
for i in range(3):  
    if i == 1:  
        break  # Exits loop prematurely  
    print(i)  
else:  
    print("This won't run!")  
```  
**Output**:  
```
0  
```  

---

## 📝 **Key Notes**  
- **`for` vs. `while`**:  
  - Use `for` when iterating over known sequences.  
  - Use `while` for conditional looping (e.g., user input).  
- **Avoid Infinite Loops**: Ensure `while` conditions eventually become `False`.  
- **`range()`**: Generates numbers (e.g., `range(5)` → `0, 1, 2, 3, 4`).  

---

## 🚀 **Pro Tips**  
#### Nested Loops:  
```python
for i in range(3):  
    for j in range(2):  
        print(f"({i}, {j})")  
```  

#### List Comprehensions (Loop Shortcut):  
```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]  
```  

--- 