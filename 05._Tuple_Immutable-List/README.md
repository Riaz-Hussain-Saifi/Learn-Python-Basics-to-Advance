# 🔒 **5. Tuples (Immutable Lists)**  
*Ordered, immutable sequences in Python.*  

---

## 📌 **Definition**  
- **Tuples** are **ordered**, **immutable** (unchangeable) sequences.  
- Defined using parentheses: `(item1, item2, ...)`.  
- Can store **mixed data types** (e.g., `(1, "apple", True)`).  
- **Faster** than lists for fixed data due to immutability.  

---

## 🛠 **Common Operations**  

### **1. Creation & Access**  
```python
names: tuple[str, str, str] = ("Riaz", "Hussian", "Alex")  # Type-hinted tuple
print(names[0])      # Output: "Riaz" (access by index)
print(names[0:2])    # Output: ("Riaz", "Hussian") (slicing)
```

### **2. Tuple Methods**  
| Method          | Example                          | Output/Effect                   |  
|-----------------|----------------------------------|---------------------------------|  
| `.index(x)`     | `(10, 20, 30).index(20)`         | `1` (first index of `x`)        |  
| `.count(x)`     | `(10, 20, 30, 20).count(20)`     | `2` (counts occurrences)        |  

**Example:**  
```python
my_tuple = (10, 20, 30, 40, 30)  
print(my_tuple.index(30))   # Output: 2  
print(my_tuple.count(30))   # Output: 2  
```

---

## 💡 **Examples**  

### **1. Immutability in Action**  
```python
my_tuple = (1, 2, 3)  
# my_tuple[0] = 10  # ❌ Error! Tuples are immutable.  
```

### **2. Unpacking Tuples**  
```python
point = (3, 5)  
x, y = point  # Unpacking  
print(x, y)   # Output: 3 5  
```

### **3. Tuples vs. Lists**  
| Feature        | Tuple (`()`)           | List (`[]`)            |  
|---------------|------------------------|------------------------|  
| **Mutability** | Immutable (safe)       | Mutable (flexible)      |  
| **Speed**      | Faster iteration       | Slower                 |  
| **Use Case**   | Fixed data (e.g., coordinates) | Dynamic data (e.g., shopping cart) |  

---

## 📝 **Key Notes**  
- **Single-Element Tuple**: Use a trailing comma: `(1,)` (without comma, it’s not a tuple).  
- **Heterogeneous Data**: Tuples often store different data types (e.g., `(name, age, height)`).  
- **Dictionary Keys**: Tuples can be keys in dictionaries (lists cannot).  

---

## 🚀 **Advanced Use Cases**  

### **1. Returning Multiple Values from Functions**  
```python
def get_user():  
    return ("Riaz", 28, 5.9)  # Packing  

name, age, height = get_user()  # Unpacking  
```

### **2. Named Tuples (Readable Code)**  
```python
from collections import namedtuple  
Person = namedtuple("Person", ["name", "age"])  
user = Person(name="Riaz", age=28)  
print(user.name)  # Output: "Riaz"  
```

--- 