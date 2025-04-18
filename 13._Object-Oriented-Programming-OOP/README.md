# 🏗️ **13. Object-Oriented Programming (OOP) in Python**  
*Organize code into reusable classes and objects for modular design.*

---

## 📌 **13.1 Introduction to OOP**  
### **Core Concepts**  
| Concept        | Description                                                                 | Example                              |  
|----------------|-----------------------------------------------------------------------------|--------------------------------------|  
| **Class**      | Blueprint for creating objects (defines attributes and methods).            | `class Car:`                         |  
| **Object**     | Instance of a class with unique data.                                       | `my_car = Car("Toyota")`             |  
| **Encapsulation** | Bundling data (attributes) and methods that operate on that data.        | `self.__private_data`                |  
| **Inheritance**  | Creating new classes from existing ones to reuse code.                    | `class ElectricCar(Car):`            |  
| **Polymorphism** | Ability to use a common interface for different forms (objects).         | `animal.speak()` (Dog → "Woof!")     |  
| **Abstraction**  | Hiding complex implementation details behind simple interfaces.           | `@abstractmethod`                    |  

---

## 🔹 **13.2 Classes & Objects**  
### **Basic Class Structure**  
```python
class Person:
    def __init__(self, name: str, age: int):  # Constructor
        self.name = name  # Instance attribute
        self.age = age

    def greet(self) -> str:  # Method
        return f"Hello, I'm {self.name}!"

# Create an object
person1 = Person("Alice", 30)
print(person1.greet())  # Output: "Hello, I'm Alice!"
```

---

## 🔹 **13.3 Inheritance**  
### **Single Inheritance**  
```python
class Student(Person):  # Inherits from Person
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id

    def study(self) -> str:
        return f"{self.name} is studying."

student = Student("Bob", 20, "S123")
print(student.greet())  # Inherited method
print(student.study())  # New method
```

### **Multiple Inheritance**  
```python
class Father:
    def father_method(self):
        return "Father's method"

class Mother:
    def mother_method(self):
        return "Mother's method"

class Child(Father, Mother):  # Inherits from both
    pass

child = Child()
print(child.father_method())  # Output: "Father's method"
print(child.mother_method())  # Output: "Mother's method"
```

### **Method Resolution Order (MRO)**  
```python
print(Child.__mro__)  # Shows inheritance search order
```

---

## 🔹 **13.4 Polymorphism**  
### **Method Overriding**  
```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: "Woof!" then "Meow!"
```

### **Duck Typing**  
```python
class Bird:
    def speak(self):
        return "Chirp!"

def make_sound(obj):  # Works if obj has speak()
    print(obj.speak())

make_sound(Dog())  # Output: "Woof!"
make_sound(Bird())  # Output: "Chirp!"
```

---

## 🔹 **13.5 Encapsulation**  
### **Access Control**  
| Syntax        | Meaning                          |  
|--------------|----------------------------------|  
| `self.name`   | Public (accessible anywhere).    |  
| `self._name`  | Protected (convention-only).     |  
| `self.__name` | Private (name-mangled).          |  

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private

    def deposit(self, amount: int):
        if amount > 0:
            self.__balance += amount

    def get_balance(self) -> int:  # Getter
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Output: 100
# print(account.__balance)   # ❌ Error: AttributeError
```

---

## 🔹 **13.6 Abstraction**  
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Base Class
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):  # Must implement
        return "Engine started!"

car = Car()
print(car.start())  # Output: "Engine started!"
```

---

## 🔹 **13.7 Class Variables & Methods**  
### **Static Methods**  
```python
class MathUtils:
    PI = 3.14159  # Class variable

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

print(MathUtils.PI)        # Output: 3.14159
print(MathUtils.add(2, 3)) # Output: 5
```

---

## 🔹 **13.8 Special Methods**  
### **Magic/Dunder Methods**  
```python
class Book:
    def __init__(self, title: str):
        self.title = title

    def __str__(self) -> str:  # String representation
        return f"Book: {self.title}"

    def __len__(self) -> int:  # Custom length
        return len(self.title)

book = Book("Python OOP")
print(book)    # Output: "Book: Python OOP"
print(len(book))  # Output: 9
```

---

## 🚀 **13.9 Best Practices**  
1. **Naming Conventions**:  
   - `PascalCase` for class names (`class MyClass`).  
   - `snake_case` for methods/variables (`def my_method`).  
2. **Composition Over Inheritance**: Favor composing objects over deep inheritance hierarchies.  
3. **Type Hints**: Use annotations for clarity (`def __init__(self, name: str)`).  
4. **Docstrings**: Document classes and methods:  
   ```python
   class Calculator:
       """Performs basic arithmetic operations."""
       def add(self, a: int, b: int) -> int:
           """Returns the sum of two numbers."""
           return a + b
   ```

---

## 🛠 **Practical Use Cases**  
1. **Data Modeling**:  
   ```python
   class User:
       def __init__(self, username: str, email: str):
           self.username = username
           self.email = email
   ```  
2. **Game Development**:  
   ```python
   class Character:
       def __init__(self, name: str, health: int):
           self.name = name
           self.health = health
   ```  

--- 