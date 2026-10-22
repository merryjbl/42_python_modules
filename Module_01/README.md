# Python Module 01 - Object-Oriented Programming
 
## 📚 Overview

Python Module 01 focuses on the fundamentals of Object-Oriented Programming (OOP). Through a series of exercises, I explored how to model real-world systems using classes, objects, inheritance, and encapsulation while following clean coding practices and using Python type annotations.

This module helped me understand how larger software projects are structured and how code can be organized to promote reusability, maintainability, and scalability.

---
 
## 🎯 Learning Objectives
 
Throughout this module, I learned to:
 
- Create and instantiate classes and objects
- Use constructors (`__init__`)
- Define and manage object attributes
- Apply encapsulation principles
- Implement getters and setters
- Validate data through controlled access
- Use inheritance to build class hierarchies
- Override methods in child classes
- Reuse parent functionality with `super()`
- Create and use static methods
- Create and use class methods
- Implement nested classes
- Track object behavior using internal analytics
- Understand basic polymorphism
- Write code with type hints and annotations
 
---
 
## 🧠 Object-Oriented Programming Concepts
 
### Classes and Objects

A class acts as a blueprint, while objects are instances created from that blueprint.

```python
class Plant:
pass

rose = Plant()
```
 
---
### Encapsulation

Encapsulation protects internal object data and controls how it can be accessed or modified.
 
```python
self._height
```

Instead of modifying attributes directly, getters and setters can be used to ensure data remains valid.

---

### Getters and Setters

Used to safely access and update object attributes.
 
```python
def get_height(self) -> float:
return self._height
```
 
```python
def set_height(self, new_height: float) -> None:
if new_height >= 0:
self._height = new_height
```
 
---

### Inheritance

Inheritance allows child classes to reuse functionality from parent classes.
 
```python
class Flower(Plant):
pass
```

Class hierarchy used in this module:
 
```text
Plant
├── Flower
│ └── Seed
└── Tree
```
 
---

### Method Overriding

Child classes can redefine parent methods to provide specialized behavior.
 
```python
def show(self) -> None:
super().show()
print("Additional information")
```

---

### `super()`

The `super()` function allows child classes to call methods from their parent class.
 
```python
super().__init__(name, height, age)
```

---

### Static Methods

Methods that belong to the class and do not require access to object attributes.
 
```python
@staticmethod
def is_year_old(days: int) -> bool:
return days > 365
```
 
Usage:
 
```python
Plant.is_year_old(400)
```
 
---

### Class Methods

Methods that receive the class itself as a parameter and are commonly used as alternative constructors.
 
```python
@classmethod
def create_anonymous(cls):
return cls("Unknown plant", 0.0, 0)
```
 
---

### Nested Classes

Classes can be defined inside other classes to organize related functionality.
 
```python
class Plant:
 
class Statistics:
pass
```
 
---

### Polymorphism

Polymorphism allows different objects to respond differently to the same method call.
 
```python
plant.show()
```
The actual method executed depends on whether the object is a `Plant`, `Flower`, `Tree`, or `Seed`.

---
 
## 🌱 Project Highlights
 
This module includes a garden management system that demonstrates:
 
- Object-Oriented Design
- Data Encapsulation
- Class Hierarchies
- Statistics Tracking
- Type Annotations
- Method Overriding
- Static and Class Methods
- Nested Classes
 
Implemented classes:
 
- `Plant`
- `Flower`
- `Tree`
- `Seed`
- `Statistics`
 
---
 
## 🛠️ Technologies Used

- Python 3
- Type Hints
- mypy
- Object-Oriented Programming
 
---
 
## 🚀 Skills Acquired

- Writing maintainable Python code
- Designing class hierarchies
- Applying OOP principles
- Using inheritance and encapsulation effectively
- Organizing complex relationships between classes
- Understanding polymorphism
- Improving code readability through type annotations
 
---
 
## 👨‍💻 Author

**Meriem Jebali**

**PhD in Complex Engineering Systems |
Student at 42 Málalga Fundacíon Télefonica**

GitHub: https://github.com/merryjbl

---
 
## 📝 Note

This repository contains educational projects completed as part of the 42 School curriculum. The goal of these exercises is to strengthen programming fundamentals and develop a deeper understanding of software design principles using Python.
