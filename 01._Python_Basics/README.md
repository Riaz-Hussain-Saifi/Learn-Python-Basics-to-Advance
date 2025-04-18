# 🐍 **1. Python Basics**  
*A beginner-friendly guide to fundamental Python concepts.*  

---

## 📌 **1.1 Printing & Memory Check**  
### **Definition**  
- `print()` displays output to the console.  
- `id()` returns the memory address of an object.  

### **Example**  
```python
name = "riaz"  
print(id(name))  # Output: Memory address of 'name' (e.g., 1402456789456)  
```  

---

## 📌 **1.2 Comments**  
### **Single-line Comment**  
```python
# This is a single-line comment (ignored by Python interpreter).  
```  

### **Multi-line Comment (Docstring)**  
```python
"""
This is a multi-line comment (docstring).  
It can span multiple lines.  
Often used for function/module documentation.  
"""
```  

---

## 📌 **1.3 Data Types & Variables**  
### **Definition**  
- **Variables** store data (no explicit declaration needed).  
- Python supports **dynamic typing** (type inferred at runtime).  

### **Common Data Types**  
| Type      | Example           | Description          |  
|-----------|------------------|----------------------|  
| `int`     | `age = 28`       | Integer              |  
| `float`   | `height = 5.9`   | Decimal number       |  
| `str`     | `name = "Riaz"`  | Text (string)        |  
| `bool`    | `is_student = True` | Boolean (`True/False`)|  
| `list`    | `[1, 2, 3]`      | Mutable sequence     |  
| `tuple`   | `(1, 2, 3)`      | Immutable sequence   |  
| `set`     | `{1, 2, 3}`      | Unordered unique elements |  
| `dict`    | `{"name": "Riaz"}` | Key-value pairs      |  

### **Type Hints & Naming (PEP 8)**  
```python
name: str = "Riaz"     # Snake_case preferred  
age: int = 28          # Type hints (optional but recommended)  
height: float = 5.9  
is_student: bool = True  
```  

---

## 📌 **1.4 Operators**  
### **Arithmetic Operators**  
| Operator | Example   | Result       |  
|----------|----------|-------------|  
| `+`      | `5 + 2`  | `7`         |  
| `-`      | `5 - 2`  | `3`         |  
| `*`      | `5 * 2`  | `10`        |  
| `/`      | `5 / 2`  | `2.5`       |  
| `**`     | `5 ** 2` | `25` (power)|  
| `//`     | `5 // 2` | `2` (floor) |  
| `%`      | `5 % 2`  | `1` (modulo)|  

### **Comparison Operators**  
```python
print(5 == 5)  # True  
print(5 != 3)  # True  
print(5 > 3)   # True  
```  

### **Logical Operators**  
```python
print(True and False)  # False  
print(True or False)   # True  
print(not True)        # False  
```  

### **Membership & Identity Operators**  
```python
nums = [1, 2, 3]  
print(2 in nums)       # True  
print(5 is not None)   # True  
```  

### **Example**  
```python
a, b = 5, 10  
print(a ** 2)          # 25  
print(b // a)          # 2  
print(a < b and a != b) # True  
```  

---

## 📌 **1.5 User Input**  
### **Example**  
```python
name = input("Enter your name: ")  # Waits for user input  
print(f"Hello, {name}!")           # f-string for formatting  
```  

---

### **🔑 Key Notes**  
- Use `type(var)` to check data types (e.g., `type(age)` → `<class 'int'>`).  
- **PEP 8**: Follow naming conventions (`snake_case` for variables).  

--- 