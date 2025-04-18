# 🚨 **12. Error & Exception Handling**  
*Gracefully manage runtime errors to prevent program crashes.*

---

## 📌 **Definition**  
- **Exceptions** are events that disrupt normal program flow (e.g., dividing by zero).  
- Use `try-except` blocks to handle exceptions elegantly.  

---

## 🔹 **Basic Syntax**  
```python
try:
    # Risky code
except ErrorType:
    # Handle error
else:
    # Runs if no error
finally:
    # Always executes (cleanup)
```

---

## 🛠 **Common Built-in Exceptions**  

| Exception            | Cause                          | Example Handling                     |  
|----------------------|--------------------------------|--------------------------------------|  
| `ZeroDivisionError`  | Division/modulo by zero        | `except ZeroDivisionError: print("Can't divide by zero")` |  
| `IndexError`         | Invalid sequence index         | `except IndexError: print("Index out of range")` |  
| `KeyError`           | Missing dictionary key         | `except KeyError: print("Key not found")` |  
| `ValueError`         | Invalid type/conversion        | `except ValueError: print("Invalid input")` |  
| `FileNotFoundError`  | Missing file                   | `except FileNotFoundError: print("File not found")` |  
| `TypeError`          | Incorrect operation type       | `except TypeError: print("Unsupported operation")` |  

### **Examples**  
```python
# Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Invalid list access
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: Index out of range.")

# File operations
try:
    with open("missing_file.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: File not found.")
```

---

## 🔹 **Advanced Handling**  

### **1. Multiple Exceptions**  
```python
try:
    # Risky code
except (KeyError, IndexError) as e:
    print(f"Error: {e}")
```

### **2. Exception Details**  
```python
try:
    int("NaN")
except ValueError as e:
    print(f"Error: {e}")  # Output: "Error: invalid literal for int() with base 10: 'NaN'"
```

### **3. Else & Finally**  
```python
try:
    print("Success")
except:
    print("Failure")
else:
    print("Runs only if no error")
finally:
    print("Always runs (cleanup)")
```

---

## 🔹 **Custom Exceptions**  
Create user-defined exceptions for specific cases.  

### **Example**  
```python
class InsufficientFundsError(Exception):
    """Raised when account balance is too low."""
    pass

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError("Balance too low!")
    return balance - amount

try:
    withdraw(1000, 500)
except InsufficientFundsError as e:
    print(f"Error: {e}")  # Output: "Error: Balance too low!"
```

---

## 🚀 **Best Practices**  
1. **Be Specific**: Catch only exceptions you can handle.  
   - ❌ Avoid bare `except:` (catches all exceptions, including `KeyboardInterrupt`).  
   - ✅ Use `except ValueError:` instead.  

2. **Log Errors**: Use `logging` for debugging:  
   ```python
   import logging
   try:
       risky_operation()
   except Exception as e:
       logging.error(f"Error: {e}", exc_info=True)
   ```

3. **Resource Cleanup**: Use `finally` or context managers (`with`):  
   ```python
   try:
       file = open("data.txt")
   finally:
       file.close()  # Always executes
   ```

4. **Raising Exceptions**: Use `raise` to propagate errors:  
   ```python
   if invalid_condition:
       raise ValueError("Invalid input")
   ```

--- 