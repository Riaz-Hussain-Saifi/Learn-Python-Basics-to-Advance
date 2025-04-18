# 🛠️ **10. Functions in Python**  
*Reusable blocks of code that perform specific tasks.*

---

## 📌 **Definition**  
- **Functions** encapsulate logic for reuse and clarity.  
- Defined using `def` followed by a name and parameters.  
- Can accept inputs (arguments) and return outputs.  

---

## 🔹 **Basic Function Syntax**  
```python
def function_name(parameters) -> return_type:
    """Docstring (optional)."""
    # Function body
    return value
```

### **Example**  
```python
def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}"

print(greet("Riaz"))  # Output: "Hello, Riaz"
```

---

## 🔹 **Flexible Arguments**  
Python functions support various argument types:  

| Argument Type  | Syntax          | Purpose                          |  
|---------------|-----------------|----------------------------------|  
| **Positional** | `def func(a, b)` | Required arguments in order.     |  
| **Default**    | `def func(a=1)`  | Optional arguments with defaults.|  
| **Variable-length (`*args`)** | `def func(*args)` | Captures extra positional args as a tuple. |  
| **Keyword (`**kwargs`)** | `def func(**kwargs)` | Captures extra keyword args as a dict. |  

### **Example**  
```python
def func(pos1, pos2, *args, greeting="Hello", **kwargs):
    print("Positional:", pos1, pos2)          # Required
    print("Extra positional:", args)          # Tuple: ("extra1", "extra2")
    print("Greeting:", greeting)              # Default: "Hello" (can be overridden)
    print("Extra keyword:", kwargs)           # Dict: {"key1": "value1", "key2": "value2"}

func("first", "second", "extra1", "extra2", greeting="Hi", key1="value1", key2="value2")
```

**Output**:  
```
Positional: first second  
Extra positional: ('extra1', 'extra2')  
Greeting: Hi  
Extra keyword: {'key1': 'value1', 'key2': 'value2'}  
```

---

## 🔹 **Return Values**  
- Use `return` to send a value back to the caller.  
- A function without `return` implicitly returns `None`.  

### **Multiple Returns**  
```python
def check_even(num: int) -> bool | str:
    if num % 2 == 0:
        return True
    return "Odd"

print(check_even(4))  # Output: True
print(check_even(3))  # Output: "Odd"
```

---

## 🔹 **Scope Rules**  
- **Local Scope**: Variables defined inside a function.  
- **Global Scope**: Variables defined outside all functions (use `global` to modify).  

### **Example**  
```python
count = 0  # Global

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```

---

## 🚀 **Best Practices**  
1. **Type Hints**: Use annotations (e.g., `def func(a: int) -> str`) for clarity.  
2. **Single Responsibility**: Each function should do one thing well.  
3. **Docstrings**: Describe purpose, args, and returns (supports `help(func)`).  
   ```python
   def add(a: int, b: int) -> int:
       """Returns the sum of two integers."""
       return a + b
   ```  
4. **Avoid Mutable Defaults**: Default args are evaluated once (use `None` instead).  
   ```python
   def safe_append(item, lst=None):
       lst = lst or []
       lst.append(item)
       return lst
   ```

---

## 🛠 **Practical Use Cases**  
1. **Data Validation**:  
   ```python
   def validate_email(email: str) -> bool:
       return "@" in email and "." in email.split("@")[-1]
   ```  
2. **API Wrapper**:  
   ```python
   def fetch_data(url: str, **params) -> dict:
       response = requests.get(url, params=params)
       return response.json()
   ```  

--- 