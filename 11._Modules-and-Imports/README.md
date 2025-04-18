# 📦 **11. Modules & Imports**  
*Organize, reuse, and share code efficiently across projects.*  

---

## 📌 **What is a Module?**  
A **module** is a Python file (`.py`) containing reusable functions, classes, or variables.  
✔ **Promotes code organization**  
✔ **Avoids repetition**  
✔ **Enables sharing across projects**  

---

## 🛠 **Importing Modules**  

### 🔹 **Basic Import**  
```python
import math
print(math.sqrt(25))  # Output: 5.0
```

### 🔹 **Import Specific Functions**  
```python
from math import pow
print(pow(2, 3))  # Output: 8.0
```

### 🔹 **Import with Alias**  
```python
import datetime as dt
print(dt.datetime.now())  # Output: Current datetime
```

---

## 🧩 **The `__name__` Guard**  
### **Why Use It?**  
- Ensures code only runs when the script is **executed directly**, not when imported.  
- Makes scripts **reusable** as modules.  

### **Example Script** (`project_01.py`)  
```python
def main():
    print("Hello from project-01!")

if __name__ == "__main__":
    main()  # Runs only when executed directly
```

### **Importing the Script**  
```python
import project_01  # No output (main() doesn't auto-run)
project_01.main()  # Output: Hello from project-01!
```

---

## 💡 **Key Takeaways**  
✔ **`import module`** → Access all contents via `module.function()`.  
✔ **`from module import x`** → Import specific items directly.  
✔ **`import module as alias`** → Shorten names for convenience.  
✔ **`if __name__ == "__main__":`** → Critical for reusable scripts!  

---

## 🔗 **Further Reading**  
- [Python Docs: Modules](https://docs.python.org/3/tutorial/modules.html)  
- [Real Python: Imports Guide](https://realpython.com/python-import/)  

---

### 🌟 **Pro Tip**  
Use `__all__` in `__init__.py` to control what gets imported with `from module import *`!  

---