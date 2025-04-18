# 🗂️ **6. Sets (Unique Unordered Collections)**  
*Store unique elements with O(1) lookups using hash tables.*

---

## 📌 **Definition**  
- **Unordered** collection of **unique** items.  
- Defined with curly braces: `{item1, item2, ...}`.  
- **No indexing** (elements are stored via hashing).  
- **Mutable**: Can add/remove items after creation.  

---

## 🛠 **Common Methods**  

| Method                 | Example                          | Effect                                  |
|------------------------|----------------------------------|-----------------------------------------|
| `.add(x)`              | `my_set.add("d")`                | Adds `x` to the set.                    |
| `.remove(x)`           | `my_set.remove("b")`             | Removes `x`; raises `KeyError` if missing. |
| `.discard(x)`          | `my_set.discard("x")`            | Removes `x` (no error if missing).      |
| `.pop()`               | `popped = my_set.pop()`          | Removes/returns an **arbitrary** element. |
| `.clear()`             | `my_set.clear()`                 | Empties the set.                        |
| `.update(other_set)`    | `my_set.update({4, 5})`          | Merges another set.                     |

---

## 💡 **Examples**  

### **1. Basic Usage**  
```python
my_set: set[str] = {"a", "b", "c", "a"}  # Duplicates auto-removed
print(my_set)  # Output: {'a', 'b', 'c'}

my_set.add("d")
my_set.remove("b")
print(my_set)  # Output: {'a', 'c', 'd'}
```

### **2. Set Operations**  
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference (in set1 not set2): {1, 2}
print(set1 ^ set2)  # Symmetric difference: {1, 2, 4, 5}
```

### **3. Fast Membership Testing**  
```python
my_set = {"apple", "banana", "cherry"}
print("banana" in my_set)  # Output: True (O(1) lookup)
```

---

## 🚀 **Why Use Sets?**  
### **1. Uniqueness Guarantee**  
```python
nums = {1, 2, 2, 3}  
print(nums)  # Output: {1, 2, 3}  
```

### **2. Performance**  
- **O(1)** for `add`, `remove`, and membership checks (vs. O(n) for lists).  

### **3. Mathematical Operations**  
- **Union (`|`)**, **Intersection (`&`)**, **Difference (`-`)**, etc.  

---

## 🔍 **Under the Hood: Hashing**  
- Each element is hashed to a unique integer (e.g., `hash("apple") → 12345`).  
- Stored in **hash buckets** for O(1) access.  
- **Collisions** resolved via chaining (linked lists in buckets).  

| Element  | Hash  | Bucket |
|----------|-------|--------|
| "Alice"  | 102   | 2      |
| "Charlie"| 178   | 3      |
| "Eve"    | 157   | 2      |

---

## 📝 **Key Notes**  
- **Immutable Alternatives**: Use `frozenset` for immutable sets (e.g., dictionary keys).  
- **Ordered Variant**: Python 3.7+ preserves insertion order in `dict`, but sets remain unordered.  

---

## 🛠 **Practical Use Cases**  
1. **Removing Duplicates**:  
   ```python
   unique = list(set([1, 2, 2, 3]))  # [1, 2, 3]
   ```  
2. **Tracking Visited Items**:  
   ```python
   visited = set()
   visited.add("user123")
   ```  

--- 