# 📖 **7. Dictionaries (Key-Value Pairs)**  
*Unordered collections of unique `key: value` pairs with O(1) lookups.*

---

## 📌 **Definition**  
- **Mutable**, **unordered** collections of `key: value` pairs.  
- Defined with curly braces: `{key1: value1, key2: value2}`.  
- **Keys must be immutable** (strings, numbers, tuples).  
- **Values can be any type** (including lists/dictionaries).  

---

## 🛠 **Common Operations**  

| Operation               | Example                          | Effect                                  |
|-------------------------|----------------------------------|-----------------------------------------|
| **Access**              | `my_dict["name"]`               | Gets value for `"name"` (raises `KeyError` if missing). |
| **Add/Update**          | `my_dict["city"] = "Cairo"`     | Adds/updates the key.                   |
| **Delete**              | `del my_dict["age"]`            | Removes the key-value pair.             |
| **Safe Access**         | `my_dict.get("name", "Default")`| Returns `"Default"` if key is missing.  |
| **Remove + Return**     | `my_dict.pop("city", None)`     | Removes key and returns its value (or `None`). |

---

## 💡 **Examples**  

### **1. Basic Usage**  
```python
my_dict: dict[str, any] = {"name": "Riaz", "age": 28}  
print(my_dict["name"])   # Output: "Riaz"  

my_dict["name"] = "Hussian"  # Update  
my_dict["city"] = "Cairo"    # Add  
del my_dict["age"]           # Delete  

print(my_dict.get("unknown", "Default"))  # Output: "Default"  
```

### **2. Iterating**  
```python
my_dict = {"name": "Riaz", "age": 22, "city": "Lahore"}  

# Keys  
for key in my_dict:  
    print(key)  # Output: "name", "age", "city"  

# Values  
for value in my_dict.values():  
    print(value)  # Output: "Riaz", 22, "Lahore"  

# Key-Value Pairs  
for key, value in my_dict.items():  
    print(f"{key}: {value}")  
```

### **3. Dictionary Methods**  
| Method          | Example                          | Output/Effect                   |  
|-----------------|----------------------------------|---------------------------------|  
| `.keys()`       | `my_dict.keys()`                | `dict_keys(["name", "age"])`    |  
| `.values()`     | `my_dict.values()`              | `dict_values(["Riaz", 28])`     |  
| `.items()`      | `my_dict.items()`               | `dict_items([("name", "Riaz")])`|  
| `.update()`     | `my_dict.update({"age": 29})`   | Updates multiple keys.          |  
| `.clear()`      | `my_dict.clear()`               | Empties the dictionary.         |  

---

## 🚀 **Why Use Dictionaries?**  
1. **Fast Lookups**: O(1) time complexity for access/insertion (uses hashing).  
2. **Flexible Storage**: Values can be any data type (e.g., lists, nested dicts).  
3. **JSON-Like Structure**: Perfect for APIs and configuration files.  

---

## 🔍 **Under the Hood: Hashing**  
- Keys are hashed to integers for quick bucket lookup.  
- **Collisions** resolved via open addressing or chaining.  

| Key     | Hash  | Bucket |  
|---------|-------|--------|  
| "name"  | 12345 | 5      |  
| "age"   | 45678 | 2      |  

---

## 📝 **Key Notes**  
- **Avoid Mutable Keys**: Lists/dictionaries can’t be keys (use tuples instead).  
- **Order Preservation**: Python 3.7+ maintains insertion order.  
- **Default Values**: Use `collections.defaultdict` for automatic defaults.  

---

## 🛠 **Practical Use Cases**  
1. **Counting Items**:  
   ```python
   counts = {}  
   for item in ["a", "b", "a"]:  
       counts[item] = counts.get(item, 0) + 1  
   print(counts)  # Output: {"a": 2, "b": 1}  
   ```  
2. **Nested Dictionaries**:  
   ```python
   users = {  
       "user1": {"name": "Riaz", "age": 28},  
       "user2": {"name": "Alex", "age": 30}  
   }  
   ```

--- 