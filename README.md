# Python Learning Notes: From Basics to Advanced 🐍

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python) ![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Welcome to my comprehensive guide on Python programming! This document covers everything from beginner-friendly basics to advanced concepts. Whether you're starting out or leveling up, this resource is designed to help you master Python with clear explanations, practical examples, and best practices.

---

## Table of Contents

- [1. Python Basics](#1-python-basics)
- [2. Strings & String Methods](#2-strings--string-methods)
- [3. Lists (Dynamic Arrays)](#3-lists-dynamic-arrays)
- [4. Loops](#4-loops)
- [5. Tuple (Immutable List)](#5-tuple-immutable-list)
- [6. Set (Unique Unordered Collection)](#6-set-unique-unordered-collection)
- [7. Dictionary (Key-Value Pairs)](#7-dictionary-key-value-pairs)
- [8. Comprehensions](#8-comprehensions)
- [9. Lambda, Map, Filter, Reduce](#9-lambda-map-filter-reduce)
- [10. Functions](#10-functions)
- [11. Modules & Imports](#11-modules--imports)
- [12. Error/Exception Handling](#12-errorexception-handling)
- [13. Object-Oriented Programming (OOP)](#13-object-oriented-programming-oop)
- [14. File Handling](#14-file-handling)
- [15. Advanced Topics](#15-advanced-topics)
- [16. Async/Await (Asynchronous Programming)](#16-asyncawait-asynchronous-programming)
- [17. Unpacking in Python](#17-unpacking-in-python)
- [18. Using `if` in One Line (Ternary Operator)](#18-using-if-in-one-line-ternary-operator)
- [19. Context Managers](#19-context-managers)

---

## 1. Python Basics

### 1.1 Printing & Memory Check 📝

- **Definition**: Print statements display output, and `id()` returns an object's memory address.
- **Example**:
  ```python
  name = "riaz"
  print(id(name))  # Output: Memory address of 'name'
  ```

### 1.2 Comments 💬

- **Single-line**:
  ```python
  # This is a single-line comment
  ```

- **Multi-line**:
  ```python
  """
  This is a multi-line comment.
  It can span multiple lines.
  """
  ```

### 1.3 Data Types & Variables 🗃️

- **Definition**: Variables store data; Python supports multiple built-in types.
- **Common Types**: `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, `dict`
- **Type Hints & Naming (PEP-8, snake_case)**:
  ```python
  name: str = "Riaz"
  age: int = 28
  height: float = 5.9
  is_student: bool = True
  ```

### 1.4 Operators ⚙️

- **Arithmetic**: `+`, `-`, `*`, `/`, `**` (exponent), `//` (floor division), `%` (modulus)
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`
- **Membership**: `in`, `not in`
- **Identity**: `is`, `is not`
- **Example**:
  ```python
  a, b = 5, 10
  print(a ** 2)        # Output: 25
  print(b // a)        # Output: 2
  print(a < b and a != b)  # Output: True
  ```

### 1.5 Input from User ⌨️

- **Example**:
  ```python
  name = input("Enter your name: ")
  print(f"Hello, {name}")
  ```

---

## 2. Strings & String Methods 🔤

- **Definition**: A string is a sequence of characters enclosed in quotes.
- **Common Methods**: `.lower()`, `.upper()`, `.capitalize()`, `.title()`, `.strip()`, `.index()`, `.count()`, `.replace()`, `.split()`, `.join()`, `.isalnum()`
- **Examples**:
  ```python
  text = "Hello World"
  print(text.upper())                    # Output: HELLO WORLD
  print(text.replace("World", "Python")) # Output: Hello Python

  # Using f-strings and checking length
  name = "riaz"
  print(f"Hello, {name}")  # Output: Hello, riaz
  print(len(name))         # Output: 4

  # Rounding a float
  value = 10.5678
  print(round(value, 2))   # Output: 10.57
  ```

---

## 3. Lists (Dynamic Arrays) 📚

- **Definition**: An ordered, mutable collection of items.
- **Common Operations**:
  - **Creation & Access**:
    ```python
    my_list = [1, 2, 3]
    print(my_list[0])  # Output: 1
    ```
  - **Modifying Lists**:
    ```python
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")   # Add element
    fruits.insert(1, "mango") # Insert at index
    fruits.extend(["kiwi", "grape"])  # Merge lists
    fruits.pop()              # Remove last
    fruits.pop(1)             # Remove at index
    fruits.remove("apple")    # Remove by value
    fruits.sort()             # Sort
    fruits.reverse()          # Reverse
    print(fruits)
    ```
  - **Other Methods**: `.count()`, `.clear()`, `.copy()`, slicing (`list[start:end]`), repeating (`[value] * n`)

---

## 4. Loops 🔄

### 4.1 For Loop

- **Definition**: Iterates over a sequence.
- **Example**:
  ```python
  my_list = [1, 2, 3, 4, 5]
  for item in my_list:
      print(item)

  # Using enumerate
  for index, value in enumerate(my_list):
      print(f"Index {index}: {value}")
  ```

### 4.2 While Loop

- **Definition**: Repeats while a condition is true.
- **Example**:
  ```python
  count = 1
  while count <= 5:
      print(count)
      count += 1
  ```

### 4.3 Else with Loops

- **Definition**: `else` runs if the loop completes without a `break`.
- **Example**:
  ```python
  for i in range(3):
      print(i)
  else:
      print("Loop completed")
  ```

---

## 5. Tuple (Immutable List) 🔒

- **Definition**: An ordered, immutable sequence.
- **Example**:
  ```python
  names: tuple[str, str, str] = ("Riaz", "Hussian", "Alex")
  print(names[0])  # Output: Riaz
  print(names[0:2]) # Output: ("Riaz", "Hussian")
  ```

> **Note**: Tuples are immutable, so their content cannot be changed after creation.

- **Methods**:
  - `index(value)`: Returns first index of value.
  - `count(value)`: Counts occurrences of value.

- **Accessing Values**:
  ```python
  my_tuple = (10, 20, 30, 40, 30)
  print(my_tuple[2])  # Output: 30
  print(my_tuple.index(30))  # Output: 2
  print(my_tuple.count(30))  # Output: 2
  print(my_tuple[1:4])  # Output: (20, 30, 40)
  ```

---

## 6. Set (Unique Unordered Collection) 🗂️

- **Definition**: An unordered collection of unique items.
- **Example**:
  ```python
  my_set: set[str] = {"a", "b", "c", "a"}
  print(my_set)  # Output: {'a', 'b', 'c'}

  my_set.add("d")
  my_set.remove("b")
  print(my_set)
  ```

> **Note**: Sets don’t support indexing due to their unordered nature.

- **Common Methods**:
  - `add(element)`
  - `remove(element)` (raises `KeyError` if not found)
  - `discard(element)` (no error if not found)
  - `pop()` (removes arbitrary element)
  - `clear()`
  - `update(other_set)`
  - Set operations: `union()`, `intersection()`, `difference()`, `symmetric_difference()`

- **Accessing Values**:
  ```python
  my_set = {1, 2, 3, 4, 5}
  for value in my_set:
      print(value)

  my_set.add(6)
  print(my_set)
  my_set.remove(2)
  my_set.discard(3)
  popped = my_set.pop()
  print(f"Popped: {popped}")
  print(my_set)
  ```

### Why Use Sets? 🚀

1. **Uniqueness**: Automatically removes duplicates.
   ```python
   my_set = {1, 2, 3, 3, 4}
   print(my_set)  # Output: {1, 2, 3, 4}
   ```
2. **Fast Lookups**: O(1) complexity due to hashing.
   ```python
   my_set = {"apple", "banana", "cherry"}
   print("banana" in my_set)  # Output: True
   ```

### Hashing vs. Non-Hashing

- **Lists**: Linear search (O(n)).
- **Sets**: Hash table (O(1) average).
- **Hashing Example**:
  | Name     | Hash | Bucket |
  |----------|------|--------|
  | Alice    | 102  | 2      |
  | Charlie  | 178  | 3      |
  | Eve      | 157  | 2      |

- **Collisions**: Handled via chaining (linked lists in buckets).
- **Key Takeaway**: Use sets for unique values and fast lookups; use lists for order.

### Set Operations

- **Example**:
  ```python
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
  print(set1 & set2)  # Intersection: {3}
  print(set1 - set2)  # Difference: {1, 2}
  ```

---

## 7. Dictionary (Key-Value Pairs) 📖

- **Definition**: Stores data in key-value pairs.
- **Examples**:
  ```python
  my_dict: dict[str, any] = {"name": "Riaz", "age": 28}
  print(my_dict["name"])  # Output: Riaz

  my_dict["name"] = "Hussian"
  my_dict["city"] = "Cairo"
  del my_dict["age"]
  my_dict.pop("city", None)
  print(my_dict.get("name", "Default Name"))

  for key, value in my_dict.items():
      print(f"{key}: {value}")
  ```

- **Iterating**:
  - **Keys**:
    ```python
    my_dict = {"name": "Riaz", "age": 22, "city": "Lahore"}
    for key in my_dict:
        print(key)
    ```
  - **Values**:
    ```python
    for value in my_dict.values():
        print(value)
    ```
  - **Key-Value Pairs**:
    ```python
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    ```

- **Using `get()`**:
  ```python
  print(my_dict.get("name", "Default Name"))  # Output: Riaz
  print(my_dict.get("unknown", "Default Name"))  # Output: Default Name
  ```

> **Tip**: Use `get()` to avoid `KeyError` when accessing keys.

---

## 8. Comprehensions ✨

- **Definition**: Concise way to create lists, sets, or dictionaries.

### 8.1 List Comprehension

- **Example**:
  ```python
  squared = [x**2 for x in range(10)]
  print(squared)
  ```

- **Use Cases**:
  - Squaring:
    ```python
    squared = [x**2 for x in range(10)]
    ```
  - Filtering:
    ```python
    even_numbers = [x for x in range(20) if x % 2 == 0]
    print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    ```
  - Transforming:
    ```python
    words = ["hello", "world", "python"]
    uppercase = [word.upper() for word in words]
    print(uppercase)  # Output: ['HELLO', 'WORLD', 'PYTHON']
    ```

### 8.2 Set & Dictionary Comprehension

- **Examples**:
  ```python
  unique_nums = {x for x in range(10)}
  print(unique_nums)

  squared_dict = {x: x**2 for x in range(5)}
  print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```

- **Use Cases**:
  - **Set**: Remove duplicates.
    ```python
    numbers = [1, 2, 3, 4, 5, 5, 6, 6, 7]
    unique = {x for x in numbers}
    print(unique)  # Output: {1, 2, 3, 4, 5, 6, 7}
    ```
  - **Dictionary**: Create mappings.
    ```python
    sentence = "hello world hello python"
    word_count = {word: sentence.split().count(word) for word in sentence.split()}
    print(word_count)  # Output: {'hello': 2, 'world': 1, 'python': 1}
    ```

---

## 9. Lambda, Map, Filter, Reduce 🔧

### 9.1 Lambda (Anonymous Function)

- **Definition**: Small, unnamed function using `lambda`.
- **Example**:
  ```python
  add = lambda a, b: a + b
  print(add(2, 3))  # Output: 5
  ```

### 9.2 Map

- **Example**:
  ```python
  numbers = [1, 2, 3, 4]
  squared = list(map(lambda x: x ** 2, numbers))
  print(squared)  # Output: [1, 4, 9, 16]
  ```

### 9.3 Filter

- **Example**:
  ```python
  even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
  print(even_numbers)  # Output: [2, 4]
  ```

### 9.4 Reduce

- **Example**:
  ```python
  from functools import reduce
  result = reduce(lambda x, y: x + y, numbers)
  print(result)  # Output: 10
  ```

---

## 10. Functions 🛠️

- **Definition**: Reusable code block for specific tasks.
- **Example**:
  ```python
  def greet(name: str) -> str:
      return f"Hello, {name}"

  print(greet("Riaz"))  # Output: Hello, Riaz

  def func(pos1, pos2, *args, **kwargs):
      print(pos1, pos2)
      print(args)
      print(kwargs)

  func("first", "second", "extra1", "extra2", key1="value1", key2="value2")
  ```

- **Flexible Arguments**:
  ```python
  def demo(a, b, *args, greeting="Hello", **kwargs):
      print("Positional:", a, b)
      print("Extra positional:", args)
      print("Greeting:", greeting)
      print("Extra keyword:", kwargs)

  demo(10, 20, 30, 40, greeting="Hi", extra="value")
  ```

---

## 11. Modules & Imports 📦

- **Definition**: Organize and reuse code across files.
- **Examples**:
  ```python
  import math
  print(math.sqrt(25))  # Output: 5.0

  from math import pow
  print(pow(2, 3))  # Output: 8

  import datetime as dt
  print(dt.datetime.now())
  ```

- **Script Example**:
  ```python
  def main():
      print("Hello from project-01!")

  if __name__ == "__main__":
      main()
  ```

- **Importing**:
  ```python
  import project_01
  project_01.main()  # Output: Hello from project-01!
  ```

---

## 12. Error/Exception Handling 🚨

- **Definition**: Handle errors gracefully with try-except.
- **Examples**:
  - **ZeroDivisionError**:
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    ```
  - **IndexError**:
    ```python
    try:
        lst = [1, 2, 3]
        result = lst[5]
    except IndexError:
        print("List index out of range.")
    ```
  - **KeyError**:
    ```python
    try:
        dct = {"a": 1, "b": 2}
        result = dct["c"]
    except KeyError:
        print("Key not found.")
    ```
  - **ValueError**:
    ```python
    try:
        result = int("not a number")
    except ValueError:
        print("Invalid value.")
    ```
  - **FileNotFoundError**:
    ```python
    try:
        with open("non_existent_file.txt", "r") as file:
            result = file.read()
    except FileNotFoundError:
        print("File not found.")
    ```
  - **Custom Error**:
    ```python
    class CustomError(Exception):
        pass

    try:
        raise CustomError("Custom error message.")
    except CustomError as e:
        print(f"Caught: {e}")
    ```

---

## 13. Object-Oriented Programming (OOP) 🏗️

### 13.1 Introduction to OOP

- **Definition**: Organizes code into classes and objects.
- **Analogy**: A class is a blueprint (e.g., for a house), and objects are instances with unique traits.

### 13.2 Classes and Objects

- **Example**:
  ```python
  class Person:
      def __init__(self, name: str, age: int):
          self.name = name
          self.age = age

      def greet(self):
          return f"Hello, my name is {self.name} and I am {self.age} years old."

  person1 = Person("Alice", 30)
  print(person1.greet())
  ```

### 13.3 Inheritance

- **Single Inheritance**:
  ```python
  class Student(Person):
      def __init__(self, name: str, age: int, student_id: int):
          super().__init__(name, age)
          self.student_id = student_id

      def greet(self):
          return f"Hello, I am {self.name}, {self.age} years old, ID: {self.student_id}."

  student1 = Student("Bob", 20, 12345)
  print(student1.greet())
  ```

- **Multiple Inheritance**:
  ```python
  class Father:
      def __init__(self, father_name: str):
          self.father_name = father_name

      def show_father_name(self):
          return f"Father's Name: {self.father_name}"

  class Mother:
      def __init__(self, mother_name: str):
          self.mother_name = mother_name

      def show_mother_name(self):
          return f"Mother's Name: {self.mother_name}"

  class Child(Father, Mother):
      def __init__(self, father_name: str, mother_name: str, child_name: str):
          Father.__init__(self, father_name)
          Mother.__init__(self, mother_name)
          self.child_name = child_name

      def show_child_name(self):
          return f"Child's Name: {self.child_name}"

  child = Child("John", "Emma", "Liam")
  print(child.show_father_name())
  print(child.show_mother_name())
  print(child.show_child_name())
  ```

- **Method Resolution Order (MRO)**:
  ```python
  print(Child.__mro__)
  ```

### 13.4 Polymorphism

- **Method Overriding**:
  ```python
  class Animal:
      def speak(self):
          pass

  class Dog(Animal):
      def speak(self):
          return "Woof!"

  class Cat(Animal):
      def speak(self):
          return "Meow!"

  dog = Dog()
  cat = Cat()
  print(dog.speak())
  print(cat.speak())
  ```

- **Duck Typing**:
  ```python
  class Bird:
      def speak(self):
          return "Chirp!"

  def animal_sound(animal):
      print(animal.speak())

  animal_sound(Dog())
  animal_sound(Cat())
  animal_sound(Bird())
  ```

### 13.5 Encapsulation

- **Example**:
  ```python
  class Person:
      def __init__(self, name: str, age: int):
          self.name = name
          self._age = age
          self.__ssn = "123-45-6789"

      def get_ssn(self):
          return self.__ssn

      def set_age(self, age: int):
          if age > 0:
              self._age = age

      def get_age(self):
          return self._age

  person = Person("Alice", 30)
  print(person.name)
  print(person._age)
  print(person.get_ssn())
  person.set_age(35)
  print(person.get_age())
  ```

- **Private Attributes**:
  ```python
  class Person:
      def __init__(self, name: str, age: int):
          self.name = name
          self._age = age
          self.__balance = 0

      def get_method(self):
          return self.__balance

  person = Person("Riaz", 20)
  print(person.name)
  person.name = "Hussian"
  print(person.name)
  print(person._age)
  person._age = 100
  print(person._age)
  print(person.get_method())
  person.__balance = 15
  print(person.get_method())
  ```

### 13.6 Abstraction

- **Example**:
  ```python
  from abc import ABC, abstractmethod

  class Vehicle(ABC):
      @abstractmethod
      def start(self):
          pass

  class Car(Vehicle):
      def start(self):
          return "Car engine started!"

  car = Car()
  print(car.start())
  ```

### 13.7 Class Variables and Methods

- **Example**:
  ```python
  class MathOperations:
      pi = 3.14159

      @staticmethod
      def add(a: float, b: float) -> float:
          return a + b

  print(MathOperations.pi)
  print(MathOperations.add(10, 20))
  ```

### 13.8 Additional Concepts

- **Callable Objects**:
  ```python
  class Counter:
      def __init__(self):
          self.count = 0

      def __call__(self):
          self.count += 1
          return self.count

  counter = Counter()
  print(counter())
  print(counter())
  ```

- **Inspecting with `dir()`**:
  ```python
  class Person:
      def __init__(self):
          self.name = "Riaz"
          self.age = 20

      def walk(self):
          print(f"{self.name} is walking")

  print([attr for attr in dir(Person()) if not attr.startswith('__')])
  ```

- **Importing Classes**:
  - `person.py`:
    ```python
    class Person:
        def __init__(self, name: str):
            self.name = name

        def greet(self):
            return f"Hello, {self.name}!"
    ```
  - `main.py`:
    ```python
    from person import Person
    person = Person("Alice")
    print(person.greet())
    ```

### 13.9 Special Methods

- **Example**:
  ```python
  class Counter:
      def __init__(self):
          self.count = 0

      def __call__(self):
          return self.count

      def __str__(self):
          return f"Counter value: {self.count}"

  counter = Counter()
  print(counter())
  print(counter)
  ```

### 13.10 Best Practices

- Use **PascalCase** for classes, **snake_case** for methods/variables.
- Keep attributes private with `__` when needed.
- Use docstrings and comments for clarity.
- Organize classes into modules.

---

## 14. File Handling 📂

- **Definition**: Reading/writing files.
- **Examples**:
  ```python
  with open("file.txt", "r") as f:
      content = f.read()
      print(content)

  with open("file.txt", "w") as file:
      file.write("Hello, Python!")
  ```

---

## 15. Advanced Topics 🌟

### 15.1 Decorators

- **Definition**: Wraps a function to extend its behavior.
- **Example**:
  ```python
  def decorator(func):
      def wrapper():
          print("Before execution")
          func()
          print("After execution")
      return wrapper

  @decorator
  def my_function():
      print("Inside function")

  my_function()
  ```

### 15.2 Generators

- **Definition**: Yields values using `yield`.
- **Example**:
  ```python
  def my_gen():
      for i in range(3):
          yield i

  gen = my_gen()
  print(next(gen))  # Output: 0
  print(next(gen))  # Output: 1
  print(next(gen))  # Output: 2
  ```

---

## 16. Async/Await (Asynchronous Programming) ⚡️

- **Definition**: Runs tasks concurrently without blocking.
- **Example**:
  ```python
  import asyncio

  async def say_hello():
      await asyncio.sleep(2)
      print("Hello, Async World!")

  asyncio.run(say_hello())
  ```

- **Multiple Tasks**:
  ```python
  async def task_one():
      await asyncio.sleep(2)
      print("Task One Completed")

  async def task_two():
      await asyncio.sleep(1)
      print("Task Two Completed")

  async def main():
      await asyncio.gather(task_one(), task_two())

  asyncio.run(main())
  ```

---

## 17. Unpacking in Python 📦

- **Definition**: Extracts values into variables.
- **Examples**:
  - **List**:
    ```python
    fruits = ["apple", "banana", "cherry"]
    first, second, third = fruits
    print(first, second, third)
    ```
  - **Tuple**:
    ```python
    coordinates = (10, 20, 30)
    x, y, z = coordinates
    print(x, y, z)
    ```
  - **Dictionary**:
    ```python
    person = {"name": "Alice", "age": 25, "city": "New York"}
    name, age, city = person.values()
    print(name, age, city)
    ```

---

## 18. Using `if` in One Line (Ternary Operator) ✅

- **Example**:
  ```python
  age = 20
  status = "Adult" if age >= 18 else "Minor"
  print(status)  # Output: Adult
  ```

---

## 19. Context Managers 🔧

### 19.1 Introduction

- **Definition**: Manages resources (e.g., files, connections) with automatic setup and cleanup.
- **Why Use?**: Simplifies code, ensures proper resource handling.

### 19.2 Using `with`

- **File Reading**:
  ```python
  with open("example.txt", "r") as file:
      content = file.read()
      print(content)
  ```

- **File Writing**:
  ```python
  with open("output.txt", "w") as file:
      file.write("Hello, Context Manager!")
  ```

### 19.3 Custom Context Manager

- **Class-Based**:
  ```python
  class Timer:
      def __init__(self):
          self.start = None

      def __enter__(self):
          import time
          self.start = time.time()
          return self

      def __exit__(self, exc_type, exc_value, traceback):
          import time
          elapsed = time.time() - self.start
          print(f"Elapsed time: {elapsed:.2f} seconds")

  with Timer() as t:
      for _ in range(1000000):
          pass
  ```

- **Using `contextlib`**:
  ```python
  from contextlib import contextmanager
  import time

  @contextmanager
  def timer():
      start = time.time()
      yield
      elapsed = time.time() - start
      print(f"Elapsed time: {elapsed:.2f} seconds")

  with timer():
      for _ in range(1000000):
          pass
  ```

### 19.4 When to Use?

- **Good For**: File handling, database connections, timing code.
- **Avoid**: Simple operations without resource management.

---

Happy coding! 🚀  
