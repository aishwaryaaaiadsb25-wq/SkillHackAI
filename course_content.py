# ============================================================
# SkillHackAI - Complete Course Content Engine
# ============================================================

course_content = {

    # ========================================================
    # PYTHON
    # ========================================================

    "python": {

        "title": "Python Mastery",
        "category": "Programming",
        "level": "Beginner to Advanced",

        "modules": [

            {
                "title": "Module 1 - Python Fundamentals",

                "topics": [

                    {
                        "title": "Introduction to Python",
                        "duration": "30 minutes",

                        "content": """
Python is a high-level, general-purpose programming language.
It is widely used for web development, automation, data science,
artificial intelligence, machine learning and scripting.

Python programs are usually easy to read because Python uses
simple and clean syntax.

Example:

print("Hello, SkillHackAI!")

The print() function displays information on the screen.
""",

                        "example": """
name = "Aishwarya"
print("Hello", name)
""",

                        "practice": [
                            "Print your name.",
                            "Print your college name.",
                            "Print three different messages.",
                            "Print the result of 10 + 20."
                        ],

                        "video": {
                            "title": "Python Full Course",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which language is used in this course?",
                                "options": [
                                    "Python",
                                    "Java",
                                    "HTML",
                                    "SQL"
                                ],
                                "answer": "Python"
                            },
                            {
                                "question": "Which function displays output in Python?",
                                "options": [
                                    "display()",
                                    "print()",
                                    "show()",
                                    "output()"
                                ],
                                "answer": "print()"
                            }
                        ]
                    },

                    {
                        "title": "Variables",
                        "duration": "35 minutes",

                        "content": """
A variable is a name used to store a value.

Python does not require you to explicitly declare the
data type of a variable.

Example:

name = "Aishwarya"
age = 20
marks = 85.5

Here:
name stores a string,
age stores an integer,
marks stores a floating-point value.
""",

                        "example": """
name = "Aishwarya"
age = 20

print(name)
print(age)
""",

                        "practice": [
                            "Create a variable called name.",
                            "Create a variable called age.",
                            "Create a variable called college.",
                            "Create three variables and print them."
                        ],

                        "video": {
                            "title": "Python Variables",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which symbol is commonly used for assignment?",
                                "options": [
                                    "=",
                                    "==",
                                    "!=",
                                    ":="
                                ],
                                "answer": "="
                            },
                            {
                                "question": "Which variable can store text?",
                                "options": [
                                    "name",
                                    "age",
                                    "count",
                                    "number"
                                ],
                                "answer": "name"
                            }
                        ]
                    },

                    {
                        "title": "Data Types",
                        "duration": "45 minutes",

                        "content": """
Python provides several built-in data types.

Common types include:

int
float
str
bool
list
tuple
set
dict

Examples:

age = 20
price = 99.50
name = "Python"
is_student = True
""",

                        "example": """
age = 20
price = 99.5
name = "Python"
is_student = True

print(type(age))
print(type(price))
print(type(name))
print(type(is_student))
""",

                        "practice": [
                            "Create an integer variable.",
                            "Create a float variable.",
                            "Create a string variable.",
                            "Create a Boolean variable.",
                            "Use type() to identify each type."
                        ],

                        "video": {
                            "title": "Python Data Types",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which type stores True or False?",
                                "options": [
                                    "int",
                                    "str",
                                    "bool",
                                    "float"
                                ],
                                "answer": "bool"
                            },
                            {
                                "question": "What type is 25?",
                                "options": [
                                    "str",
                                    "int",
                                    "float",
                                    "bool"
                                ],
                                "answer": "int"
                            }
                        ]
                    },

                    {
                        "title": "Input and Output",
                        "duration": "40 minutes",

                        "content": """
The input() function is used to receive information
from the user.

The print() function displays information.

Example:

name = input("Enter your name: ")
print("Hello", name)

input() normally returns a string.
""",

                        "example": """
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
""",

                        "practice": [
                            "Ask the user for their name.",
                            "Ask the user for their age.",
                            "Ask for two numbers and add them.",
                            "Create a simple student information program."
                        ],

                        "video": {
                            "title": "Python Input and Output",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which function receives user input?",
                                "options": [
                                    "input()",
                                    "scan()",
                                    "read()",
                                    "get()"
                                ],
                                "answer": "input()"
                            }
                        ]
                    },

                    {
                        "title": "Type Conversion",
                        "duration": "35 minutes",

                        "content": """
Type conversion means changing one data type into another.

Common functions:

int()
float()
str()
bool()

Example:

age = int("20")
price = float("99.5")
number = str(100)
""",

                        "example": """
a = "10"
b = "20"

a = int(a)
b = int(b)

print(a + b)
""",

                        "practice": [
                            "Convert a string to integer.",
                            "Convert an integer to string.",
                            "Convert a string to float.",
                            "Create a calculator using input conversion."
                        ],

                        "video": {
                            "title": "Python Type Conversion",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which function converts a value to integer?",
                                "options": [
                                    "integer()",
                                    "int()",
                                    "number()",
                                    "convert()"
                                ],
                                "answer": "int()"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 2 - Operators",

                "topics": [

                    {
                        "title": "Arithmetic Operators",
                        "duration": "35 minutes",

                        "content": """
Arithmetic operators perform mathematical calculations.

+ addition
- subtraction
* multiplication
/ division
// floor division
% modulus
** exponentiation
""",

                        "example": """
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
""",

                        "practice": [
                            "Create a simple calculator.",
                            "Find the remainder of two numbers.",
                            "Calculate the square of a number.",
                            "Calculate the area of a rectangle."
                        ],

                        "video": {
                            "title": "Python Operators",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which operator gives the remainder?",
                                "options": [
                                    "/",
                                    "//",
                                    "%",
                                    "**"
                                ],
                                "answer": "%"
                            }
                        ]
                    },

                    {
                        "title": "Comparison Operators",
                        "duration": "30 minutes",

                        "content": """
Comparison operators compare values.

==
!=
>
<
>=
<=

The result of a comparison is normally True or False.
""",

                        "example": """
age = 20

print(age == 20)
print(age > 18)
print(age < 18)
""",

                        "practice": [
                            "Compare two numbers.",
                            "Check whether a number is greater than 50.",
                            "Check whether two strings are equal."
                        ],

                        "video": {
                            "title": "Python Comparison Operators",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which operator checks equality?",
                                "options": [
                                    "=",
                                    "==",
                                    "!=",
                                    ">="
                                ],
                                "answer": "=="
                            }
                        ]
                    },

                    {
                        "title": "Logical Operators",
                        "duration": "35 minutes",

                        "content": """
Logical operators combine conditions.

and
or
not

Example:

age >= 18 and age <= 60

Both conditions must be true when using and.
""",

                        "example": """
age = 20
has_id = True

print(age >= 18 and has_id)
""",

                        "practice": [
                            "Check whether a person is eligible to vote.",
                            "Check whether a number is between 10 and 100.",
                            "Use and, or and not in examples."
                        ],

                        "video": {
                            "title": "Python Logical Operators",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which operator requires both conditions to be true?",
                                "options": [
                                    "or",
                                    "and",
                                    "not",
                                    "xor"
                                ],
                                "answer": "and"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 3 - Decision Making",

                "topics": [

                    {
                        "title": "if Statement",
                        "duration": "35 minutes",

                        "content": """
The if statement executes code only when a condition is true.

Example:

age = 20

if age >= 18:
    print("Adult")
""",

                        "example": """
marks = 80

if marks >= 50:
    print("Pass")
""",

                        "practice": [
                            "Check whether a number is positive.",
                            "Check whether a student passed.",
                            "Check whether a person is eligible to vote."
                        ],

                        "video": {
                            "title": "Python If Statements",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which keyword starts a conditional statement?",
                                "options": [
                                    "if",
                                    "when",
                                    "check",
                                    "condition"
                                ],
                                "answer": "if"
                            }
                        ]
                    },

                    {
                        "title": "if-else",
                        "duration": "35 minutes",

                        "content": """
if-else provides two possible execution paths.

Example:

if marks >= 50:
    print("Pass")
else:
    print("Fail")
""",

                        "example": """
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
""",

                        "practice": [
                            "Check even or odd.",
                            "Check positive or negative.",
                            "Check pass or fail.",
                            "Check whether a number is divisible by 5."
                        ],

                        "video": {
                            "title": "Python If Else",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which keyword executes when if is false?",
                                "options": [
                                    "otherwise",
                                    "else",
                                    "elif",
                                    "except"
                                ],
                                "answer": "else"
                            }
                        ]
                    },

                    {
                        "title": "elif",
                        "duration": "40 minutes",

                        "content": """
elif allows multiple conditions to be checked.

Example:

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"
""",

                        "example": """
marks = 82

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("F")
""",

                        "practice": [
                            "Create a grade calculator.",
                            "Create an age-category program.",
                            "Create a simple menu program."
                        ],

                        "video": {
                            "title": "Python Elif",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which keyword checks another condition?",
                                "options": [
                                    "elif",
                                    "else",
                                    "another",
                                    "case"
                                ],
                                "answer": "elif"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 4 - Loops",

                "topics": [

                    {
                        "title": "for Loop",
                        "duration": "45 minutes",

                        "content": """
A for loop repeats code for each item in a sequence.

Example:

for i in range(5):
    print(i)

The range function commonly generates a sequence of numbers.
""",

                        "example": """
for i in range(1, 6):
    print(i)
""",

                        "practice": [
                            "Print numbers from 1 to 10.",
                            "Print even numbers from 1 to 20.",
                            "Print a multiplication table.",
                            "Find the sum of numbers from 1 to 100."
                        ],

                        "video": {
                            "title": "Python For Loops",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which loop is commonly used to iterate over a sequence?",
                                "options": [
                                    "for",
                                    "if",
                                    "switch",
                                    "case"
                                ],
                                "answer": "for"
                            }
                        ]
                    },

                    {
                        "title": "while Loop",
                        "duration": "40 minutes",

                        "content": """
A while loop repeats code while a condition remains true.

Example:

count = 1

while count <= 5:
    print(count)
    count += 1
""",

                        "example": """
number = 5

while number > 0:
    print(number)
    number -= 1
""",

                        "practice": [
                            "Print numbers from 1 to 10.",
                            "Create a countdown.",
                            "Create a number guessing loop.",
                            "Keep asking for a password until it is correct."
                        ],

                        "video": {
                            "title": "Python While Loops",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "A while loop continues while what is true?",
                                "options": [
                                    "A condition",
                                    "A class",
                                    "A module",
                                    "A function name"
                                ],
                                "answer": "A condition"
                            }
                        ]
                    },

                    {
                        "title": "break and continue",
                        "duration": "35 minutes",

                        "content": """
break immediately exits a loop.

continue skips the remaining code for the current iteration
and moves to the next iteration.
""",

                        "example": """
for i in range(1, 10):

    if i == 5:
        break

    print(i)
""",

                        "practice": [
                            "Stop a loop when a number reaches 10.",
                            "Skip even numbers.",
                            "Stop searching when an item is found."
                        ],

                        "video": {
                            "title": "Python Break and Continue",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which keyword exits a loop?",
                                "options": [
                                    "stop",
                                    "break",
                                    "exitloop",
                                    "end"
                                ],
                                "answer": "break"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 5 - Data Structures",

                "topics": [

                    {
                        "title": "Lists",
                        "duration": "50 minutes",

                        "content": """
A list stores multiple values in an ordered and mutable collection.

Example:

numbers = [10, 20, 30, 40]

Lists support indexing, slicing, adding, removing and
modifying elements.
""",

                        "example": """
numbers = [10, 20, 30]

numbers.append(40)
numbers.remove(20)

print(numbers)
""",

                        "practice": [
                            "Create a list of five student names.",
                            "Add an element.",
                            "Remove an element.",
                            "Find the largest number.",
                            "Find the sum of a list."
                        ],

                        "video": {
                            "title": "Python Lists",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Are Python lists mutable?",
                                "options": [
                                    "Yes",
                                    "No",
                                    "Only sometimes",
                                    "Only numbers"
                                ],
                                "answer": "Yes"
                            }
                        ]
                    },

                    {
                        "title": "Tuples",
                        "duration": "35 minutes",

                        "content": """
A tuple is an ordered collection that cannot normally be changed
after creation.

Example:

student = ("Aishwarya", 20, "CSE")
""",

                        "example": """
point = (10, 20)

print(point[0])
print(point[1])
""",

                        "practice": [
                            "Create a tuple of three values.",
                            "Access tuple elements.",
                            "Unpack a tuple into variables."
                        ],

                        "video": {
                            "title": "Python Tuples",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Can tuple elements normally be changed?",
                                "options": [
                                    "Yes",
                                    "No",
                                    "Only strings",
                                    "Only integers"
                                ],
                                "answer": "No"
                            }
                        ]
                    },

                    {
                        "title": "Sets",
                        "duration": "35 minutes",

                        "content": """
A set stores unique elements.

Duplicate values are automatically removed.

Example:

numbers = {1, 2, 2, 3}

The resulting set contains unique values.
""",

                        "example": """
skills = {"Python", "SQL", "Python"}

print(skills)
""",

                        "practice": [
                            "Create a set of numbers.",
                            "Remove duplicates from a list.",
                            "Find common elements between two sets.",
                            "Find the union of two sets."
                        ],

                        "video": {
                            "title": "Python Sets",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "What is a major property of a set?",
                                "options": [
                                    "It stores unique elements",
                                    "It stores only strings",
                                    "It is always sorted",
                                    "It stores only numbers"
                                ],
                                "answer": "It stores unique elements"
                            }
                        ]
                    },

                    {
                        "title": "Dictionaries",
                        "duration": "50 minutes",

                        "content": """
A dictionary stores data as key-value pairs.

Example:

student = {
    "name": "Aishwarya",
    "age": 20,
    "department": "CSE"
}

Keys are used to access values.
""",

                        "example": """
student = {
    "name": "Aishwarya",
    "age": 20
}

print(student["name"])
print(student["age"])
""",

                        "practice": [
                            "Create a student dictionary.",
                            "Add a new key.",
                            "Update an existing value.",
                            "Remove a key.",
                            "Loop through dictionary items."
                        ],

                        "video": {
                            "title": "Python Dictionaries",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "A dictionary stores information using what?",
                                "options": [
                                    "Key-value pairs",
                                    "Only indexes",
                                    "Only values",
                                    "Rows"
                                ],
                                "answer": "Key-value pairs"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 6 - Functions",

                "topics": [

                    {
                        "title": "Creating Functions",
                        "duration": "45 minutes",

                        "content": """
A function is a reusable block of code.

Functions are created using the def keyword.

Example:

def greet():
    print("Hello")

greet()
""",

                        "example": """
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
""",

                        "practice": [
                            "Create a function that prints your name.",
                            "Create an addition function.",
                            "Create a function to calculate square.",
                            "Create a function to check even or odd."
                        ],

                        "video": {
                            "title": "Python Functions",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which keyword defines a function?",
                                "options": [
                                    "function",
                                    "def",
                                    "fun",
                                    "define"
                                ],
                                "answer": "def"
                            }
                        ]
                    },

                    {
                        "title": "Parameters and Return Values",
                        "duration": "45 minutes",

                        "content": """
Parameters allow functions to receive information.

The return statement sends a result back to the caller.
""",

                        "example": """
def multiply(a, b):
    return a * b

answer = multiply(5, 4)

print(answer)
""",

                        "practice": [
                            "Create a multiplication function.",
                            "Create a maximum-number function.",
                            "Create a function that returns a grade."
                        ],

                        "video": {
                            "title": "Python Function Parameters",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which statement sends a result back?",
                                "options": [
                                    "send",
                                    "return",
                                    "output",
                                    "result"
                                ],
                                "answer": "return"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 7 - File Handling",

                "topics": [

                    {
                        "title": "Reading and Writing Files",
                        "duration": "50 minutes",

                        "content": """
Python can work with files using the open() function.

Common modes include:

r - read
w - write
a - append

Example:

with open("data.txt", "r") as file:
    content = file.read()
""",

                        "example": """
with open("student.txt", "w") as file:
    file.write("Aishwarya")
""",

                        "practice": [
                            "Create a text file.",
                            "Write student information.",
                            "Read the file.",
                            "Append new information.",
                            "Create a simple notes application."
                        ],

                        "video": {
                            "title": "Python File Handling",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which mode is commonly used for reading?",
                                "options": [
                                    "r",
                                    "w",
                                    "a",
                                    "x"
                                ],
                                "answer": "r"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 8 - Exception Handling",

                "topics": [

                    {
                        "title": "try and except",
                        "duration": "45 minutes",

                        "content": """
Exception handling prevents a program from crashing unexpectedly.

Python commonly uses:

try
except
else
finally

Example:

try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid number")
""",

                        "example": """
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")
""",

                        "practice": [
                            "Handle invalid integer input.",
                            "Handle division by zero.",
                            "Create a safe calculator.",
                            "Use finally in an example."
                        ],

                        "video": {
                            "title": "Python Exception Handling",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which block handles an exception?",
                                "options": [
                                    "except",
                                    "error",
                                    "catch",
                                    "handle"
                                ],
                                "answer": "except"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 9 - Object-Oriented Programming",

                "topics": [

                    {
                        "title": "Classes and Objects",
                        "duration": "60 minutes",

                        "content": """
Object-oriented programming organizes software around objects.

A class is a blueprint.

An object is an instance of a class.

Example:

class Student:

    def __init__(self, name):
        self.name = name

student = Student("Aishwarya")

print(student.name)
""",

                        "example": """
class Car:

    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(self.brand)

car = Car("Toyota")

car.display()
""",

                        "practice": [
                            "Create a Student class.",
                            "Create a BankAccount class.",
                            "Create a Car class.",
                            "Add methods to your classes."
                        ],

                        "video": {
                            "title": "Python OOP",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "A class is best described as what?",
                                "options": [
                                    "A blueprint",
                                    "A variable",
                                    "A loop",
                                    "A file"
                                ],
                                "answer": "A blueprint"
                            }
                        ]
                    },

                    {
                        "title": "Inheritance",
                        "duration": "50 minutes",

                        "content": """
Inheritance allows one class to reuse features from another class.

A child class can inherit attributes and methods from a parent class.
""",

                        "example": """
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def bark(self):
        print("Woof")


dog = Dog()

dog.speak()
dog.bark()
""",

                        "practice": [
                            "Create a parent class.",
                            "Create a child class.",
                            "Reuse a parent method.",
                            "Create a simple vehicle hierarchy."
                        ],

                        "video": {
                            "title": "Python Inheritance",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Inheritance allows a class to do what?",
                                "options": [
                                    "Reuse functionality",
                                    "Delete data",
                                    "Stop execution",
                                    "Create files"
                                ],
                                "answer": "Reuse functionality"
                            }
                        ]
                    },

                    {
                        "title": "Polymorphism",
                        "duration": "45 minutes",

                        "content": """
Polymorphism allows different objects to respond to the same
operation in different ways.

This is an important object-oriented programming concept.
""",

                        "example": """
class Dog:

    def sound(self):
        print("Woof")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
""",

                        "practice": [
                            "Create two classes with the same method.",
                            "Demonstrate different behavior.",
                            "Build a simple payment example."
                        ],

                        "video": {
                            "title": "Python Polymorphism",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Polymorphism refers to what?",
                                "options": [
                                    "Different behaviors through a common interface",
                                    "Only inheritance",
                                    "Only variables",
                                    "File processing"
                                ],
                                "answer": "Different behaviors through a common interface"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 10 - Advanced Python",

                "topics": [

                    {
                        "title": "List Comprehensions",
                        "duration": "40 minutes",

                        "content": """
List comprehensions provide a concise way to create lists.

Example:

squares = [x * x for x in range(1, 6)]
""",

                        "example": """
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)
""",

                        "practice": [
                            "Create a list of squares.",
                            "Create a list of even numbers.",
                            "Create a list using a condition."
                        ],

                        "video": {
                            "title": "Python List Comprehensions",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "List comprehension is mainly used for what?",
                                "options": [
                                    "Concise list creation",
                                    "Database creation",
                                    "File deletion",
                                    "Class inheritance"
                                ],
                                "answer": "Concise list creation"
                            }
                        ]
                    },

                    {
                        "title": "Modules and Packages",
                        "duration": "45 minutes",

                        "content": """
Modules allow Python code to be organized into reusable files.

Packages organize multiple modules.

Example:

import math

print(math.sqrt(25))
""",

                        "example": """
import math

number = 25

print(math.sqrt(number))
""",

                        "practice": [
                            "Import the math module.",
                            "Use random.",
                            "Create your own module.",
                            "Import a function from your module."
                        ],

                        "video": {
                            "title": "Python Modules",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "Which keyword imports a module?",
                                "options": [
                                    "include",
                                    "import",
                                    "use",
                                    "load"
                                ],
                                "answer": "import"
                            }
                        ]
                    },

                    {
                        "title": "Regular Expressions",
                        "duration": "50 minutes",

                        "content": """
Regular expressions are patterns used to search and manipulate text.

Python provides the re module.

Regular expressions are useful for:

- Email validation
- Phone number validation
- Skill extraction
- Text searching
- Data cleaning
""",

                        "example": """
import re

text = "Contact: student@example.com"

pattern = r"\\w+@\\w+\\.\\w+"

result = re.findall(pattern, text)

print(result)
""",

                        "practice": [
                            "Find email addresses.",
                            "Find phone numbers.",
                            "Search for a specific word.",
                            "Build a simple resume skill extractor."
                        ],

                        "video": {
                            "title": "Python Regular Expressions",
                            "url": "https://www.youtube.com/watch?v=K8L6KVGG-7o"
                        },

                        "quiz": [
                            {
                                "question": "Which Python module is used for regular expressions?",
                                "options": [
                                    "regex",
                                    "re",
                                    "pattern",
                                    "search"
                                ],
                                "answer": "re"
                            }
                        ]
                    },

                    {
                        "title": "JSON and APIs",
                        "duration": "60 minutes",

                        "content": """
JSON is a common format for exchanging structured data.

Python provides the json module for working with JSON.

APIs allow applications to communicate with other systems.

This concept is especially important for real-world
web applications and AI applications.
""",

                        "example": """
import json

student = {
    "name": "Aishwarya",
    "age": 20
}

data = json.dumps(student)

print(data)
""",

                        "practice": [
                            "Convert a dictionary to JSON.",
                            "Read JSON data.",
                            "Create a small API request program.",
                            "Build a JSON-based student record."
                        ],

                        "video": {
                            "title": "Python APIs and JSON",
                            "url": "https://www.youtube.com/watch?v=tb8gHvYlCFs"
                        },

                        "quiz": [
                            {
                                "question": "What is JSON commonly used for?",
                                "options": [
                                    "Data exchange",
                                    "Looping",
                                    "Compilation",
                                    "Memory allocation"
                                ],
                                "answer": "Data exchange"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 11 - Real World Projects",

                "topics": [

                    {
                        "title": "Student Management System",
                        "duration": "120 minutes",

                        "content": """
Build a Python application that manages student information.

The project should allow users to:

- Add students
- View students
- Search students
- Update information
- Delete students
- Save data
- Load data
""",

                        "example": """
students = []

student = {
    "name": "Aishwarya",
    "age": 20,
    "department": "CSE"
}

students.append(student)

print(students)
""",

                        "practice": [
                            "Create the menu.",
                            "Implement add student.",
                            "Implement search.",
                            "Implement update.",
                            "Implement delete.",
                            "Add file storage."
                        ],

                        "video": {
                            "title": "Python Project Development",
                            "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
                        },

                        "quiz": [
                            {
                                "question": "What should a student management system store?",
                                "options": [
                                    "Student information",
                                    "Only images",
                                    "Only passwords",
                                    "Only numbers"
                                ],
                                "answer": "Student information"
                            }
                        ]
                    },

                    {
                        "title": "Resume Skill Analyzer",
                        "duration": "180 minutes",

                        "content": """
Build a practical Python project that reads resume text and
identifies technical skills.

The project can use:

- Text processing
- Regular expressions
- Skill dictionaries
- File handling
- Data structures

This project forms the foundation for the SkillHackAI application.
""",

                        "example": """
resume_text = "Python SQL Machine Learning Git"

skills = [
    "python",
    "sql",
    "machine learning",
    "git"
]

found = []

for skill in skills:

    if skill in resume_text.lower():
        found.append(skill)

print(found)
""",

                        "practice": [
                            "Create a skill dictionary.",
                            "Search resume text.",
                            "Extract matching skills.",
                            "Calculate skill coverage.",
                            "Create a simple recommendation system."
                        ],

                        "video": {
                            "title": "Python NLP Project",
                            "url": "https://www.youtube.com/watch?v=K8L6KVGG-7o"
                        },

                        "quiz": [
                            {
                                "question": "What can a resume skill analyzer identify?",
                                "options": [
                                    "Technical skills",
                                    "Only images",
                                    "Only dates",
                                    "Only colors"
                                ],
                                "answer": "Technical skills"
                            }
                        ]
                    }
                ]
            }
        ],

        "final_assessment": [

            {
                "question": "Which keyword defines a function?",
                "options": ["function", "def", "fun", "method"],
                "answer": "def"
            },

            {
                "question": "Which data structure stores key-value pairs?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "answer": "Dictionary"
            },

            {
                "question": "Which keyword is used for exception handling?",
                "options": ["try", "check", "error", "handle"],
                "answer": "try"
            },

            {
                "question": "Which concept allows a child class to reuse a parent class?",
                "options": [
                    "Inheritance",
                    "Iteration",
                    "Compilation",
                    "Parsing"
                ],
                "answer": "Inheritance"
            },

            {
                "question": "Which module is commonly used for regular expressions?",
                "options": ["math", "re", "json", "os"],
                "answer": "re"
            },

            {
                "question": "Which keyword imports a module?",
                "options": ["include", "import", "load", "use"],
                "answer": "import"
            },

            {
                "question": "Which collection stores unique values?",
                "options": ["List", "Set", "Tuple", "String"],
                "answer": "Set"
            },

            {
                "question": "Which function receives user input?",
                "options": ["read()", "input()", "get()", "scan()"],
                "answer": "input()"
            },

            {
                "question": "Which statement immediately exits a loop?",
                "options": ["stop", "break", "exit", "continue"],
                "answer": "break"
            },

            {
                "question": "What is JSON commonly used for?",
                "options": [
                    "Data exchange",
                    "Loop control",
                    "Class inheritance",
                    "Memory allocation"
                ],
                "answer": "Data exchange"
            }
        ],

        "passing_score": 70,
        "certificate": True
    },


    # ========================================================
    # SQL
    # ========================================================

    "sql": {

        "title": "SQL & Database Mastery",
        "category": "Databases",
        "level": "Beginner to Advanced",

        "modules": [

            {
                "title": "Module 1 - SQL Fundamentals",

                "topics": [

                    {
                        "title": "Introduction to Databases",
                        "duration": "40 minutes",

                        "content": """
A database is an organized collection of data.

A relational database stores data in tables.

A table contains rows and columns.

Examples of relational database systems include
MySQL, PostgreSQL, Oracle and SQL Server.
""",

                        "example": """
Students

id | name       | age
1  | Aishwarya  | 20
2  | Arun       | 21
""",

                        "practice": [
                            "Identify rows and columns.",
                            "Design a student table.",
                            "Design an employee table."
                        ],

                        "video": {
                            "title": "SQL Full Course",
                            "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"
                        },

                        "quiz": [
                            {
                                "question": "Where is relational data commonly stored?",
                                "options": [
                                    "Tables",
                                    "Images",
                                    "Folders",
                                    "Classes"
                                ],
                                "answer": "Tables"
                            }
                        ]
                    },

                    {
                        "title": "SELECT Queries",
                        "duration": "45 minutes",

                        "content": """
SELECT is used to retrieve data from a table.

Example:

SELECT * FROM students;

Specific columns can also be selected.
""",

                        "example": """
SELECT name, age
FROM students;
""",

                        "practice": [
                            "Select all students.",
                            "Select only names.",
                            "Select names and ages.",
                            "Retrieve employee information."
                        ],

                        "video": {
                            "title": "SQL SELECT",
                            "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"
                        },

                        "quiz": [
                            {
                                "question": "Which command retrieves data?",
                                "options": [
                                    "SELECT",
                                    "GET",
                                    "READ",
                                    "FETCH"
                                ],
                                "answer": "SELECT"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 2 - Filtering and Sorting",

                "topics": [

                    {
                        "title": "WHERE Clause",
                        "duration": "40 minutes",

                        "content": """
WHERE filters rows according to a condition.

Example:

SELECT *
FROM students
WHERE age > 18;
""",

                        "example": """
SELECT name
FROM students
WHERE marks >= 80;
""",

                        "practice": [
                            "Find students above age 18.",
                            "Find employees with salary above 50000.",
                            "Find products below a specific price."
                        ],

                        "video": {
                            "title": "SQL WHERE Clause",
                            "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"
                        },

                        "quiz": [
                            {
                                "question": "Which clause filters rows?",
                                "options": [
                                    "WHERE",
                                    "FILTER",
                                    "CHECK",
                                    "HAVING"
                                ],
                                "answer": "WHERE"
                            }
                        ]
                    },

                    {
                        "title": "ORDER BY",
                        "duration": "35 minutes",

                        "content": """
ORDER BY sorts query results.

ASC sorts ascending.

DESC sorts descending.
""",

                        "example": """
SELECT *
FROM students
ORDER BY marks DESC;
""",

                        "practice": [
                            "Sort students by marks.",
                            "Sort employees by salary.",
                            "Sort products by price."
                        ],

                        "video": {
                            "title": "SQL ORDER BY",
                            "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"
                        },

                        "quiz": [
                            {
                                "question": "Which keyword sorts descending?",
                                "options": [
                                    "DOWN",
                                    "DESC",
                                    "REVERSE",
                                    "HIGH"
                                ],
                                "answer": "DESC"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 3 - SQL Joins",

                "topics": [

                    {
                        "title": "INNER JOIN",
                        "duration": "60 minutes",

                        "content": """
JOIN operations combine related information from multiple tables.

INNER JOIN returns rows that have matching values in both tables.
""",

                        "example": """
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.id;
""",

                        "practice": [
                            "Join students and courses.",
                            "Join employees and departments.",
                            "Join orders and customers."
                        ],

                        "video": {
                            "title": "SQL Joins",
                            "url": "https://www.youtube.com/watch?v=9yeOJ0ZMUYw"
                        },

                        "quiz": [
                            {
                                "question": "What does INNER JOIN return?",
                                "options": [
                                    "Matching rows",
                                    "Only left rows",
                                    "Only right rows",
                                    "All possible rows"
                                ],
                                "answer": "Matching rows"
                            }
                        ]
                    }
                ]
            }
        ],

        "final_assessment": [

            {
                "question": "Which command retrieves data?",
                "options": ["SELECT", "GET", "FETCH", "READ"],
                "answer": "SELECT"
            },

            {
                "question": "Which clause filters rows?",
                "options": ["WHERE", "ORDER", "GROUP", "SORT"],
                "answer": "WHERE"
            },

            {
                "question": "Which keyword sorts descending?",
                "options": ["DESC", "DOWN", "REVERSE", "HIGH"],
                "answer": "DESC"
            },

            {
                "question": "Which operation combines tables?",
                "options": ["JOIN", "MERGE", "CONNECT", "LINK"],
                "answer": "JOIN"
            }
        ],

        "passing_score": 70,
        "certificate": True
    },


    # ========================================================
    # MACHINE LEARNING
    # ========================================================

    "machine-learning": {

        "title": "Machine Learning Mastery",
        "category": "Artificial Intelligence",
        "level": "Intermediate to Advanced",

        "modules": [

            {
                "title": "Module 1 - ML Fundamentals",

                "topics": [

                    {
                        "title": "What is Machine Learning?",
                        "duration": "50 minutes",

                        "content": """
Machine Learning is a field of artificial intelligence where
computer systems learn patterns from data.

Instead of manually writing every rule, we provide data and
allow an algorithm to learn a useful relationship.

Major categories include:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning
""",

                        "example": """
Example:

Input:
Hours studied

Output:
Exam score

A machine learning model can learn the relationship between
study hours and exam scores.
""",

                        "practice": [
                            "Identify a real-world ML problem.",
                            "Give one supervised learning example.",
                            "Give one unsupervised learning example.",
                            "Explain why training data is important."
                        ],

                        "video": {
                            "title": "Machine Learning Full Course",
                            "url": "https://www.youtube.com/watch?v=GwIo3gDZCVQ"
                        },

                        "quiz": [
                            {
                                "question": "Machine learning primarily learns from what?",
                                "options": [
                                    "Data",
                                    "Only rules",
                                    "Only images",
                                    "Only code"
                                ],
                                "answer": "Data"
                            }
                        ]
                    },

                    {
                        "title": "Training and Testing Data",
                        "duration": "45 minutes",

                        "content": """
A dataset is commonly divided into training and testing data.

Training data is used to learn patterns.

Testing data is used to evaluate how well the trained model
performs on unseen examples.
""",

                        "example": """
A dataset can be divided into:

80% training
20% testing
""",

                        "practice": [
                            "Explain training data.",
                            "Explain testing data.",
                            "Explain why testing is necessary.",
                            "Create a train-test split using Python."
                        ],

                        "video": {
                            "title": "Train Test Split",
                            "url": "https://www.youtube.com/watch?v=GwIo3gDZCVQ"
                        },

                        "quiz": [
                            {
                                "question": "What is testing data used for?",
                                "options": [
                                    "Evaluation",
                                    "Training only",
                                    "Deleting data",
                                    "Creating variables"
                                ],
                                "answer": "Evaluation"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 2 - Regression",

                "topics": [

                    {
                        "title": "Linear Regression",
                        "duration": "60 minutes",

                        "content": """
Linear regression predicts a continuous numerical value.

A simple model attempts to learn a relationship between
input variables and an output variable.

Example applications:

- House price prediction
- Sales prediction
- Temperature prediction
- Salary prediction
""",

                        "example": """
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
""",

                        "practice": [
                            "Build a simple regression model.",
                            "Predict house prices.",
                            "Calculate prediction error.",
                            "Visualize actual vs predicted values."
                        ],

                        "video": {
                            "title": "Linear Regression",
                            "url": "https://www.youtube.com/watch?v=GwIo3gDZCVQ"
                        },

                        "quiz": [
                            {
                                "question": "Regression commonly predicts what type of output?",
                                "options": [
                                    "Continuous numerical value",
                                    "Only text",
                                    "Only images",
                                    "Only categories"
                                ],
                                "answer": "Continuous numerical value"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 3 - Classification",

                "topics": [

                    {
                        "title": "Logistic Regression",
                        "duration": "60 minutes",

                        "content": """
Classification predicts categories.

Logistic regression is commonly used for binary classification.

Example:

Email → Spam / Not Spam

Student → Pass / Fail
""",

                        "example": """
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
""",

                        "practice": [
                            "Build a binary classifier.",
                            "Create a spam classification example.",
                            "Calculate accuracy."
                        ],

                        "video": {
                            "title": "Logistic Regression",
                            "url": "https://www.youtube.com/watch?v=GwIo3gDZCVQ"
                        },

                        "quiz": [
                            {
                                "question": "Classification predicts what?",
                                "options": [
                                    "Categories",
                                    "Only continuous values",
                                    "Only files",
                                    "Only text length"
                                ],
                                "answer": "Categories"
                            }
                        ]
                    }
                ]
            },

            {
                "title": "Module 4 - Decision Trees",

                "topics": [

                    {
                        "title": "Decision Tree",
                        "duration": "60 minutes",

                        "content": """
A decision tree makes predictions by applying a sequence of
decision rules.

It can be used for both classification and regression.
""",

                        "example": """
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
""",

                        "practice": [
                            "Build a decision tree classifier.",
                            "Visualize a simple decision tree.",
                            "Compare tree depth values."
                        ],

                        "video": {
                            "title": "Decision Trees",
                            "url": "https://www.youtube.com/watch?v=GwIo3gDZCVQ"
                        },

                        "quiz": [
                            {
                                "question": "Decision trees can be used for?",
                                "options": [
                                    "Classification and regression",
                                    "Only classification",
                                    "Only regression",
                                    "Only clustering"
                                ],
                                "answer": "Classification and regression"
                            }
                        ]
                    }
                ]
            }
        ],

        "final_assessment": [

            {
                "question": "Machine learning learns patterns from what?",
                "options": ["Data", "Only rules", "Only files", "Only images"],
                "answer": "Data"
            },

            {
                "question": "What is testing data used for?",
                "options": ["Evaluation", "Training", "Deletion", "Formatting"],
                "answer": "Evaluation"
            },

            {
                "question": "Regression commonly predicts?",
                "options": [
                    "Continuous values",
                    "Only categories",
                    "Only text",
                    "Only images"
                ],
                "answer": "Continuous values"
            },

            {
                "question": "Classification predicts?",
                "options": [
                    "Categories",
                    "Only numbers",
                    "Only files",
                    "Only equations"
                ],
                "answer": "Categories"
            }
        ],

        "passing_score": 70,
        "certificate": True
    }
}


# ============================================================
# Helper Functions
# ============================================================

def get_course(course_name):
    """
    Return one course using its course key.
    """
    return course_content.get(course_name)


def get_modules(course_name):
    """
    Return all modules for a course.
    """
    course = get_course(course_name)

    if course:
        return course.get("modules", [])

    return []


def get_topic_count(course_name):
    """
    Count all topics in a course.
    """
    modules = get_modules(course_name)

    count = 0

    for module in modules:
        count += len(module.get("topics", []))

    return count


def get_course_summary(course_name):
    """
    Return useful course statistics.
    """
    course = get_course(course_name)

    if not course:
        return None

    modules = course.get("modules", [])

    topic_count = 0

    for module in modules:
        topic_count += len(module.get("topics", []))

    return {
        "title": course.get("title"),
        "category": course.get("category"),
        "level": course.get("level"),
        "modules": len(modules),
        "topics": topic_count,
        "passing_score": course.get("passing_score", 70),
        "certificate": course.get("certificate", False)
    }