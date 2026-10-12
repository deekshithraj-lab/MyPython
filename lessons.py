
# lessons.py
# Stores Python lessons for the PyLearn application.


class Lesson:
    """Represents a single Python lesson."""

    def __init__(self, title, explanation, example, output):
        self.title = title
        self.explanation = explanation
        self.example = example
        self.output = output


# All lessons are stored in this list.
LESSONS = [

    # 1. Introduction to Python
    Lesson(
        "1. Introduction to Python",
        "Python is a beginner-friendly programming language used to build apps, websites, and more.",
        'print("Hello, World!")',
        "Hello, World!"
    ),

    # 2. Variables
    Lesson(
        "2. Variables",
        "Variables store information that can be used later.",
        'name = "Ravi"\nage = 20\nprint(name)\nprint(age)',
        "Ravi\n20"
    ),

    # 3. Data Types
    Lesson(
        "3. Data Types",
        "Common data types include strings, integers, floats, and booleans.",
        'name = "Ravi"\nage = 20\nheight = 5.8\nis_student = True\n\nprint(type(name))\nprint(type(age))\nprint(type(height))\nprint(type(is_student))',
        "<class 'str'>\n<class 'int'>\n<class 'float'>\n<class 'bool'>"
    ),

    # 4. User Input
    Lesson(
        "4. User Input",
        "The input() function allows users to enter information.",
        'name = input("Enter your name: ")\nprint("Hello", name)',
        "Example input: Ravi\nExample output: Hello Ravi"
    ),

    # 5. Operators
    Lesson(
        "5. Operators",
        "Operators perform calculations and comparisons.",
        'a = 10\nb = 3\nprint(a + b)\nprint(a * b)\nprint(a > b)',
        "13\n30\nTrue"
    ),

    # 6. If Statements
    Lesson(
        "6. If Statements",
        "If statements allow a program to make decisions.",
        'age = 18\n\nif age >= 18:\n    print("You are an adult")\nelse:\n    print("You are a minor")',
        "You are an adult"
    ),

    # 7. Loops
    Lesson(
        "7. Loops",
        "Loops repeat a block of code. A for loop is useful for iterating over a sequence.",
        'for number in range(1, 6):\n    print(number)',
        "1\n2\n3\n4\n5"
    ),

    # 8. Functions
    Lesson(
        "8. Functions",
        "Functions group reusable code. Use the def keyword to define a function.",
        'def greet(name):\n    print("Hello", name)\n\ngreet("Ravi")',
        "Hello Ravi"
    ),

    # 9. Lists
    Lesson(
        "9. Lists",
        "Lists store multiple values in a single variable.",
        'fruits = ["apple", "banana", "mango"]\nprint(fruits[0])\nprint(len(fruits))',
        "apple\n3"
    ),

    # 10. Dictionaries
    Lesson(
        "10. Dictionaries",
        "Dictionaries store information as key-value pairs.",
        'student = {"name": "Ravi", "age": 20}\nprint(student["name"])\nprint(student["age"])',
        "Ravi\n20"
    ),

    # 11. Classes and Objects
    Lesson(
        "11. Classes and Objects",
        "A class is a blueprint for creating objects. An object is an instance of a class.",
        'class Student:\n    def __init__(self, name):\n        self.name = name\n\n    def introduce(self):\n        print("My name is", self.name)\n\nstudent = Student("Ravi")\nstudent.introduce()',
        "My name is Ravi"
    ),

    # 12. Encapsulation
    Lesson(
        "12. Encapsulation",
        "Encapsulation groups data and methods together. A leading underscore indicates an attribute intended for internal use.",
        'class BankAccount:\n    def __init__(self, balance):\n        self._balance = balance\n\n    def show_balance(self):\n        print(self._balance)\n\naccount = BankAccount(1000)\naccount.show_balance()',
        "1000"
    ),

    # 13. Inheritance
    Lesson(
        "13. Inheritance",
        "Inheritance allows a child class to reuse methods and attributes from a parent class.",
        'class Animal:\n    def speak(self):\n        print("Animal sound")\n\nclass Dog(Animal):\n    pass\n\ndog = Dog()\ndog.speak()',
        "Animal sound"
    ),

    # 14. Polymorphism
    Lesson(
        "14. Polymorphism",
        "Polymorphism allows different classes to implement the same method name in different ways.",
        'class Dog:\n    def speak(self):\n        print("Woof!")\n\nclass Cat:\n    def speak(self):\n        print("Meow!")\n\nanimals = [Dog(), Cat()]\n\nfor animal in animals:\n    animal.speak()',
        "Woof!\nMeow!"
    ),

    # 15. Abstraction
    Lesson(
        "15. Abstraction",
        "Abstraction exposes essential behavior while hiding implementation details. Python supports this using the abc module.",
        'from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\n\nclass Square(Shape):\n    def __init__(self, side):\n        self.side = side\n\n    def area(self):\n        return self.side ** 2\n\nsquare = Square(4)\nprint(square.area())',
        "16"
    ),

    # 16. Exception Handling
    Lesson(
        "16. Exception Handling",
        "try and except allow a program to handle errors gracefully.",
        'try:\n    number = int("abc")\nexcept ValueError:\n    print("Please enter a valid number")',
        "Please enter a valid number"
    ),

    # 17. File Handling
    Lesson(
        "17. File Handling",
        "Python can read and write files. This example creates a file and writes text to it.",
        'with open("example.txt", "w") as file:\n    file.write("Learning Python!")\n\nprint("File created successfully")',
        "File created successfully"
    ),

]

