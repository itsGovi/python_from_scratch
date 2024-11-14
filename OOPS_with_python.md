# OOPs with Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects, which represent both data and the operations (or "methods") that can be performed on the data. Python, being an object-oriented language, is well-suited for OOP, making it an ideal choice for understanding this concept.

Let's dive into the key concepts of OOP and illustrate each with Python examples.

### 1. **Classes and Objects**

- A **class** is like a blueprint for creating objects. It defines a set of properties and methods that an object created from the class can have.
- An **object** is an instance of a class. When you create an object, you create an entity that has the structure and behavior defined by the class.

#### Example:

```python
class Dog:
    # class attribute
    species = "Canis lupus familiaris"
  
    # initializer method (constructor)
    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age
  
    # instance method
    def bark(self):
        return f"{self.name} says Woof!"

# creating instances (objects) of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

print(dog1.bark())  # Output: Buddy says Woof!
print(dog2.bark())  # Output: Lucy says Woof!
```

Here, `Dog` is a class, while `dog1` and `dog2` are instances (objects) of the `Dog` class. Each instance has its own `name` and `age`, but they share the class attribute `species`.

### 2. **Encapsulation**

- **Encapsulation** is the concept of wrapping data (variables) and methods into a single unit, typically a class.
- This means that an object’s internal state is hidden from the outside world and can only be changed by its own methods.
- In Python, encapsulation is achieved using private variables (using an underscore prefix).

#### Example:

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        # private attribute
        self._balance = balance
  
    # public method to get balance
    def get_balance(self):
        return self._balance
  
    # public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}")
  
    # public method to withdraw money
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}")

# creating an account object
my_account = Account("Alice", 100)
my_account.deposit(50)  # Deposited 50. New balance is 150
my_account.withdraw(30)  # Withdrew 30. New balance is 120
```

In this example, `_balance` is a private attribute, meaning it’s intended to be accessed only within the class. The user interacts with it only through `deposit` and `withdraw` methods, which enforce control over the balance.

### 3. **Inheritance**

- **Inheritance** allows one class (child or derived class) to inherit the attributes and methods of another class (parent or base class).
- This promotes reusability and allows new classes to build upon existing ones.

#### Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name
  
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# creating instances of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!
```

Here, `Animal` is the parent class, and `Dog` and `Cat` are subclasses that inherit from `Animal`. Each subclass overrides the `sound` method to implement their specific sounds.

### 4. **Polymorphism**

- **Polymorphism** allows us to use a unified interface for different data types. In Python, it means that the same method can be used on different types of objects.

#### Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name
  
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# function that takes any Animal and calls its speak method
def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
```

In this example, even though `dog` and `cat` are different objects, they can both be passed to the `animal_sound` function, which calls their specific `speak` method. This demonstrates polymorphism, as the same method call works for multiple types.

### 5. **Abstraction**

- **Abstraction** is the concept of hiding the complex implementation details and showing only the essential features of the object.
- This can be achieved using abstract base classes (ABCs) and interfaces, which define methods that must be implemented in derived classes.

#### Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
  
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    def area(self):
        return self.width * self.height
  
    def perimeter(self):
        return 2 * (self.width + self.height)

# attempting to create an instance of Shape will raise an error
# shape = Shape()  # TypeError

rect = Rectangle(5, 10)
print(f"Area: {rect.area()}")  # Output: Area: 50
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30
```

Here, `Shape` is an abstract class with abstract methods `area` and `perimeter`. Any subclass of `Shape` must implement these methods, ensuring that every shape has a way to calculate area and perimeter. `Rectangle` provides the specific implementation of these methods.

---

### Summary of Key Concepts

- **Classes and Objects**: Classes are templates for creating objects, which are instances of classes.
- **Encapsulation**: Keeps data safe and manages access control through public/private members.
- **Inheritance**: Enables creating a new class based on an existing class, promoting reusability.
- **Polymorphism**: Allows methods to process objects differently based on their class types, using the same method name.
- **Abstraction**: Hides unnecessary details, focusing only on essential parts of an interface.

Understanding these concepts gives you a robust foundation in OOP with Python, helping you build scalable, modular, and organized code.


## Q: In encapsulation, I can't check my balance, right? but even though its my account, why is it private and who can access it, explain with a real world example

Great question! Encapsulation can be confusing, especially since it seems to limit access to your own data. Let’s break it down with both a practical explanation and a real-world example to clarify why encapsulation is used in this way and why it can actually benefit you.

### Why Encapsulation Makes Certain Data Private

Encapsulation’s primary purpose is to **protect the integrity of data** by limiting direct access to it. By marking data as "private," you prevent direct, potentially harmful access that could lead to errors or unintended consequences. In Python, data isn't truly private like in some other languages, but by convention, attributes prefixed with an underscore (like `_balance`) are meant to be treated as private and only accessed within the class itself.

So in an encapsulated system, **you can still check your balance**—just not by accessing it directly. Instead, you use a method that the class provides, like `get_balance()`. This method acts as a **controlled way** of retrieving the balance without exposing the actual balance attribute.

### Who Can Access Private Data?

Technically, only methods within the class can access this "private" data. This is beneficial because if you need to change how balance data is stored or modify access control later, you can do it within the class without affecting how users interact with it.

### Real-World Example: Banking ATM System

Think of an **ATM machine** as a real-world example of encapsulation:

- When you want to check your account balance, you don’t access the bank’s internal servers directly. Instead, you interact with the ATM’s interface, which shows you your balance, lets you withdraw money, deposit funds, etc. The ATM acts as a **controlled interface** that mediates your access to the account data.
- **Private Access**: The actual account data (e.g., your balance, transaction history) is stored securely in the bank's internal systems, which you cannot directly access or modify. You can only interact with this data through predefined methods (like viewing balance or making withdrawals), ensuring that you don’t accidentally change the balance or corrupt the data.
- **Why This is Important**: Suppose you could directly access the balance in the bank’s system without using the ATM interface. You might mistakenly add or subtract money from your balance or see incomplete or wrong data due to a system error. By having controlled access (encapsulation), the bank ensures that any balance inquiry or transaction goes through verified processes, preventing accidental or unauthorized changes.

### Python Example Explained with this Real-World Analogy

Here’s how the `Account` class from earlier might fit this analogy:

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # The balance is "private" for protection.
  
    # Public method to check balance, similar to using an ATM to view it.
    def get_balance(self):
        return self._balance
  
    # Public method to deposit money, ensuring only valid amounts are added.
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}")
  
    # Public method to withdraw money, protecting against overdrafts.
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}")

# creating an account object
my_account = Account("Alice", 100)

# Accessing balance through a method, not directly
print("Current Balance:", my_account.get_balance())  # Output: 100
my_account.deposit(50)   # Deposited 50. New balance is 150
my_account.withdraw(20)  # Withdrew 20. New balance is 130
```

In this code:

- `get_balance()` is like the "check balance" option on an ATM. You still get to see your balance but through a **controlled method** that the bank (or `Account` class) provides.
- `_balance` is kept private to prevent accidental or malicious changes. If it were public, other parts of the program could inadvertently modify it, leading to possible errors or security issues.

### Benefits of this Approach

1. **Data Protection**: Ensures balance cannot be modified arbitrarily. Only methods within `Account` can adjust the balance, adding a layer of security.
2. **Error Prevention**: By controlling access to `_balance`, we reduce the chance of unintended or incorrect updates.
3. **Flexibility**: If the bank later decides to change how balance is stored or calculated (e.g., it needs to include fees or rewards), it can modify the `Account` class without affecting how the balance is accessed through `get_balance()`.

### Summary

Encapsulation doesn’t restrict your ability to check your balance—it just controls **how** you access it. By providing you with controlled access methods, encapsulation protects the integrity and security of your account data, much like how an ATM machine ensures secure and accurate banking transactions.
