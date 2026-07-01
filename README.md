# special-method

# Python Special Methods (Dunder Methods)

This project demonstrates how Python’s special methods (also called *dunder methods*) allow custom classes to behave like native Python objects. Each example shows how to implement and use these methods.

---

## 📖 Contents
- Constructor (`__init__`)
- Informal Representation (`__str__`)
- Formal Representation (`__repr__`)
- Length Method (`__len__`)
- Equality Comparison (`__eq__`)
- Operator Overloading (`__add__`, `__sub__`, `__mul__`)
- Item Access (`__getitem__`)
- Item Assignment (`__setitem__`)
- Membership Testing (`__contains__`)
- Callable Objects (`__call__`)
- Iteration Support (`__iter__`, `__next__`)
- Boolean Evaluation (`__bool__`)
- Destructor (`__del__`)

---

## Constructor (`__init__`)
Initializes attributes when an object is created.
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## Informal Representation (`__str__`)
Human-readable string for end users.
```python
class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"student: {self.name}"
```

---

## Formal Representation (`__repr__`)
Developer-focused, ideally unambiguous.
```python
class Student:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Student(name={self.name!r})"
```

---

## Length Method (`__len__`)
Defines behavior of `len(obj)`.
```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    def __len__(self):
        return len(self.songs)
```

---

## Equality Comparison (`__eq__`)
Customizes how `==` works.
```python
class Student:
    def __init__(self, student_id):
        self.student_id = student_id
    def __eq__(self, other):
        return self.student_id == other.student_id
```

---

## Operator Overloading
Redefines operators for custom objects.

### Addition (`__add__`)
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

### Subtraction (`__sub__`)
```python
class Vector:
    def __init__(self, x):
        self.x = x
    def __sub__(self, other):
        return Vector(self.x - other.x)
```

### Multiplication (`__mul__`)
```python
class Number:
    def __init__(self, value):
        self.value = value
    def __mul__(self, other):
        return Number(self.value * other.value)
```

---

## Item Access (`__getitem__`)
Supports indexing.
```python
class Grades:
    def __init__(self):
        self.data = [85, 90, 78]
    def __getitem__(self, index):
        return self.data[index]
```

---

## Item Assignment (`__setitem__`)
Supports assignment.
```python
class Grades:
    def __init__(self):
        self.data = [85, 90, 78]
    def __setitem__(self, index, value):
        self.data[index] = value
```

---

## Membership Testing (`__contains__`)
Supports `in` keyword.
```python
class Course:
    def __init__(self):
        self.students = ["Ella", "Sandra", "Joe"]
    def __contains__(self, student):
        return student in self.students
```

---

## Callable Objects (`__call__`)
Makes objects behave like functions.
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, number):
        return number * self.factor
```

---

## Iteration Support (`__iter__`, `__next__`)
Allows looping with `for ... in`.
```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
```

---

## Boolean Evaluation (`__bool__`)
Defines truthiness.
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __bool__(self):
        return self.balance > 0
```

---

## Destructor (`__del__`)
Cleans up resources when object is destroyed.
```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        print("File opened")
    def __del__(self):
        print("File closed")
```

---

## 🎯 Purpose
This project is a **learning resource** for understanding Python’s special methods. By experimenting with these examples, you’ll see how to make custom classes behave like built-in types.
```

---

This is now one complete README file — ready to copy and paste into your assignment.
