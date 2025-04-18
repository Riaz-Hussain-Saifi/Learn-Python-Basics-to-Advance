# 📜 **2. Strings & String Methods**  
*Working with text data in Python using string operations and methods.*  

---

## 📌 **Definition**  
A **string** is a sequence of characters enclosed in:  
- Single quotes: `'Hello'`  
- Double quotes: `"World"`  
- Triple quotes (for multi-line): `"""Python"""`  

**Strings are immutable** (cannot be changed after creation).  

---

## 🔤 **Common String Methods**  

| Method          | Example                          | Output              | Description                          |  
|-----------------|----------------------------------|---------------------|--------------------------------------|  
| `.lower()`      | `"HELLO".lower()`                | `'hello'`           | Converts to lowercase                |  
| `.upper()`      | `"hello".upper()`                | `'HELLO'`           | Converts to uppercase                |  
| `.capitalize()` | `"hello".capitalize()`           | `'Hello'`           | Capitalizes first letter             |  
| `.title()`      | `"hello world".title()`          | `'Hello World'`     | Title case (each word capitalized)   |  
| `.strip()`      | `"  hello  ".strip()`            | `'hello'`           | Removes leading/trailing whitespace  |  
| `.index()`      | `"hello".index('e')`             | `1`                 | Returns index of substring           |  
| `.count()`      | `"hello".count('l')`             | `2`                 | Counts substring occurrences         |  
| `.replace()`    | `"Hello".replace("H", "J")`      | `'Jello'`           | Replaces substring                   |  
| `.split()`      | `"a,b,c".split(',')`             | `['a', 'b', 'c']`   | Splits into a list                   |  
| `.join()`       | `",".join(['a', 'b', 'c'])`      | `'a,b,c'`           | Joins list into a string             |  
| `.isalnum()`    | `"abc123".isalnum()`             | `True`              | Checks alphanumeric characters       |  

---

## 💡 **Examples**  

### **1. Basic String Operations**  
```python
text = "Hello World"  
print(text.upper())                    # Output: "HELLO WORLD"  
print(text.replace("World", "Python")) # Output: "Hello Python"  
```  

### **2. f-strings (Formatted Strings)**  
```python
name = "riaz"  
print(f"Hello, {name}")  # Output: "Hello, riaz"  
print(len(name))         # Output: 4 (length of string)  
```  

### **3. Rounding Floats in Strings**  
```python
value = 10.5678  
print(round(value, 2))   # Output: 10.57 (rounded to 2 decimal places)  
```  

---

## 🛠 **Practical Tips**  
- **Escape Characters**: Use `\` for special characters (e.g., `\n` for newline).  
- **Multiline Strings**: Use triple quotes (`"""` or `'''`).  
- **String Slicing**: Extract parts using indices (e.g., `"hello"[1:4]` → `'ell'`).  

---

## 📝 **Key Notes**  
- **Immutability**: Strings cannot be modified in-place (e.g., `text[0] = 'h'` raises an error).  
- **Use `in` for Substrings**: Check if a substring exists (`"world" in "Hello world"` → `True`).  

--- 