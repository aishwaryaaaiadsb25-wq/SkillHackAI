# SkillHackAI - In-App Course Library
# Upgraded course structure:
# Lesson -> Video -> Explanation -> Example -> Practice -> Quiz

courses = {

    "python": {
        "title": "Python Programming",
        "description": "Learn Python programming from fundamentals to practical programming.",
        "icon": "🐍",

        "lessons": [

            {
                "title": "Python Basics",
                "video": "",
                "content": """
Python is a beginner-friendly programming language.

In this topic you will learn:
- Variables
- Data types
- Input and output
- Basic operators

Example:

name = "Aishwarya"
age = 20

print(name)
print(age)
                """,

                "example": """
name = "Aishwarya"
age = 20

print("Name:", name)
print("Age:", age)
                """,

                "practice": [
                    "Create a variable called name and store your name.",
                    "Create a variable called age and store your age.",
                    "Print both variables."
                ],

                "quiz": [
                    {
                        "question": "Which function is used to display output in Python?",
                        "options": ["input()", "print()", "display()", "show()"],
                        "answer": "print()"
                    },
                    {
                        "question": "Which symbol is used to assign a value to a variable?",
                        "options": ["=", "==", ":", "->"],
                        "answer": "="
                    }
                ]
            },

            {
                "title": "Conditions",
                "video": "",
                "content": """
Conditional statements allow a program to make decisions.

Python commonly uses:
- if
- elif
- else
                """,

                "example": """
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
                """,

                "practice": [
                    "Write a program to check whether a number is positive.",
                    "Write a program to check whether a person is eligible to vote."
                ],

                "quiz": [
                    {
                        "question": "Which keyword is used for a condition?",
                        "options": ["if", "for", "def", "class"],
                        "answer": "if"
                    },
                    {
                        "question": "Which keyword handles another condition?",
                        "options": ["else", "elif", "other", "next"],
                        "answer": "elif"
                    }
                ]
            },

            {
                "title": "Loops",
                "video": "",
                "content": """
Loops are used when we want to repeat a block of code.

Python provides:
- for loop
- while loop
                """,

                "example": """
for i in range(5):
    print(i)
                """,

                "practice": [
                    "Print numbers from 1 to 10.",
                    "Print all even numbers from 1 to 20."
                ],

                "quiz": [
                    {
                        "question": "Which loop is commonly used to iterate over a sequence?",
                        "options": ["for", "if", "class", "try"],
                        "answer": "for"
                    },
                    {
                        "question": "Which function generates a sequence of numbers?",
                        "options": ["numbers()", "range()", "sequence()", "loop()"],
                        "answer": "range()"
                    }
                ]
            },

            {
                "title": "Functions",
                "video": "",
                "content": """
Functions allow us to organize reusable blocks of code.

A Python function is created using the def keyword.
                """,

                "example": """
def greet(name):
    print("Hello", name)

greet("Aishwarya")
                """,

                "practice": [
                    "Create a function that adds two numbers.",
                    "Create a function that checks whether a number is even."
                ],

                "quiz": [
                    {
                        "question": "Which keyword creates a function?",
                        "options": ["function", "def", "fun", "create"],
                        "answer": "def"
                    },
                    {
                        "question": "Why are functions useful?",
                        "options": [
                            "They remove variables",
                            "They allow code reuse",
                            "They stop programs",
                            "They delete data"
                        ],
                        "answer": "They allow code reuse"
                    }
                ]
            }
        ],

        "final_quiz": [
            {
                "question": "Which keyword creates a function?",
                "options": ["function", "def", "fun", "method"],
                "answer": "def"
            },
            {
                "question": "Which function displays output?",
                "options": ["input()", "print()", "output()", "show()"],
                "answer": "print()"
            },
            {
                "question": "Which statement is used for decision making?",
                "options": ["if", "for", "def", "import"],
                "answer": "if"
            },
            {
                "question": "Which loop can iterate through a sequence?",
                "options": ["for", "if", "def", "class"],
                "answer": "for"
            }
        ]
    },


    # ==========================================================
    # SQL
    # ==========================================================

    "sql": {
        "title": "SQL & Database Fundamentals",
        "description": "Learn databases and SQL queries from beginner level.",
        "icon": "🗄️",

        "lessons": [

            {
                "title": "Database Basics",
                "video": "",
                "content": """
A database stores and organizes information.

Important concepts:
- Database
- Table
- Row
- Column
- Primary key
                """,

                "example": """
CREATE TABLE students (
    id INT,
    name VARCHAR(100),
    age INT
);
                """,

                "practice": [
                    "Identify rows and columns in a student table.",
                    "Create a simple students table."
                ],

                "quiz": [
                    {
                        "question": "What stores data in rows and columns?",
                        "options": ["Table", "Function", "Loop", "Variable"],
                        "answer": "Table"
                    },
                    {
                        "question": "Which key uniquely identifies a record?",
                        "options": ["Foreign key", "Primary key", "Normal key", "Index key"],
                        "answer": "Primary key"
                    }
                ]
            },

            {
                "title": "SELECT Queries",
                "video": "",
                "content": """
SELECT is used to retrieve data from a database table.
                """,

                "example": """
SELECT name, age
FROM students;
                """,

                "practice": [
                    "Write a query to display all students.",
                    "Write a query to display only student names."
                ],

                "quiz": [
                    {
                        "question": "Which SQL command retrieves data?",
                        "options": ["SELECT", "GET", "FETCH", "READ"],
                        "answer": "SELECT"
                    },
                    {
                        "question": "Which keyword specifies the table?",
                        "options": ["FROM", "TABLE", "WHERE", "IN"],
                        "answer": "FROM"
                    }
                ]
            },

            {
                "title": "Filtering Data",
                "video": "",
                "content": """
The WHERE clause filters records according to a condition.
                """,

                "example": """
SELECT *
FROM students
WHERE age >= 18;
                """,

                "practice": [
                    "Find students whose age is greater than 20.",
                    "Find students with a particular name."
                ],

                "quiz": [
                    {
                        "question": "Which clause filters rows?",
                        "options": ["WHERE", "FILTER", "CHECK", "IF"],
                        "answer": "WHERE"
                    }
                ]
            },

            {
                "title": "Sorting and Grouping",
                "video": "",
                "content": """
ORDER BY sorts records.

GROUP BY groups records based on one or more columns.
                """,

                "example": """
SELECT *
FROM students
ORDER BY age DESC;
                """,

                "practice": [
                    "Sort students by age.",
                    "Group records by department."
                ],

                "quiz": [
                    {
                        "question": "Which clause sorts records?",
                        "options": ["ORDER BY", "SORT", "GROUP", "ARRANGE"],
                        "answer": "ORDER BY"
                    }
                ]
            }
        ],

        "final_quiz": [
            {
                "question": "Which command retrieves data?",
                "options": ["SELECT", "INSERT", "DELETE", "UPDATE"],
                "answer": "SELECT"
            },
            {
                "question": "Which clause filters records?",
                "options": ["WHERE", "ORDER BY", "GROUP BY", "FROM"],
                "answer": "WHERE"
            },
            {
                "question": "Which clause sorts data?",
                "options": ["ORDER BY", "WHERE", "SELECT", "GROUP BY"],
                "answer": "ORDER BY"
            }
        ]
    },


    # ==========================================================
    # MACHINE LEARNING
    # ==========================================================

    "machine learning": {
        "title": "Machine Learning Fundamentals",
        "description": "Understand the basic concepts of machine learning.",
        "icon": "🤖",

        "lessons": [

            {
                "title": "Introduction to Machine Learning",
                "video": "",
                "content": """
Machine Learning allows computers to learn patterns from data.

Main types:
- Supervised learning
- Unsupervised learning
- Reinforcement learning
                """,

                "example": """
Example:

House size -> House price

The model learns the relationship between the input and output.
                """,

                "practice": [
                    "Give one real-world example of machine learning.",
                    "Identify whether a problem is supervised or unsupervised."
                ],

                "quiz": [
                    {
                        "question": "What does machine learning learn from?",
                        "options": ["Data", "Only images", "Only text", "Nothing"],
                        "answer": "Data"
                    }
                ]
            },

            {
                "title": "Supervised Learning",
                "video": "",
                "content": """
Supervised learning uses labelled training data.

Common tasks:
- Classification
- Regression
                """,

                "example": """
Email -> Spam / Not Spam

This is a classification problem.
                """,

                "practice": [
                    "Identify a classification problem.",
                    "Identify a regression problem."
                ],

                "quiz": [
                    {
                        "question": "What type of data does supervised learning use?",
                        "options": [
                            "Labelled data",
                            "No data",
                            "Only random data",
                            "Images only"
                        ],
                        "answer": "Labelled data"
                    }
                ]
            },

            {
                "title": "Data Preparation",
                "video": "",
                "content": """
Data preparation is an important part of machine learning.

Common steps:
- Cleaning
- Handling missing values
- Encoding
- Scaling
                """,

                "example": """
Missing age values can be replaced with the median age.
                """,

                "practice": [
                    "Identify missing values in a dataset.",
                    "Explain why data cleaning is important."
                ],

                "quiz": [
                    {
                        "question": "Which step handles missing values?",
                        "options": [
                            "Data cleaning",
                            "Prediction",
                            "Deployment",
                            "Testing only"
                        ],
                        "answer": "Data cleaning"
                    }
                ]
            },

            {
                "title": "Model Evaluation",
                "video": "",
                "content": """
Models must be evaluated to understand their performance.

Common metrics include:
- Accuracy
- Precision
- Recall
- F1-score
                """,

                "example": """
Accuracy = Correct Predictions / Total Predictions
                """,

                "practice": [
                    "Explain accuracy in your own words.",
                    "List two classification metrics."
                ],

                "quiz": [
                    {
                        "question": "Which metric measures the proportion of correct predictions?",
                        "options": ["Accuracy", "Recall", "Loss", "Error"],
                        "answer": "Accuracy"
                    }
                ]
            }
        ],

        "final_quiz": [
            {
                "question": "Machine learning learns patterns from what?",
                "options": ["Data", "Keyboard", "Monitor", "Nothing"],
                "answer": "Data"
            },
            {
                "question": "Which learning uses labelled data?",
                "options": [
                    "Supervised learning",
                    "Unsupervised learning",
                    "Random learning",
                    "Manual learning"
                ],
                "answer": "Supervised learning"
            },
            {
                "question": "Which metric measures correct predictions?",
                "options": ["Accuracy", "Recall", "Input", "Feature"],
                "answer": "Accuracy"
            }
        ]
    },


    # ==========================================================
    # WEB DEVELOPMENT
    # ==========================================================

    "web development": {
        "title": "Web Development",
        "description": "Learn the foundations of modern web development.",
        "icon": "🌐",

        "lessons": [

            {
                "title": "HTML Basics",
                "video": "",
                "content": """
HTML creates the structure of a web page.

Important elements:
- html
- head
- body
- heading
- paragraph
- button
                """,

                "example": """
<h1>SkillHackAI</h1>
<p>AI Career Platform</p>
                """,

                "practice": [
                    "Create a page with a heading.",
                    "Add a paragraph describing yourself."
                ],

                "quiz": [
                    {
                        "question": "What does HTML provide?",
                        "options": ["Structure", "Database", "Server", "AI model"],
                        "answer": "Structure"
                    }
                ]
            },

            {
                "title": "CSS Basics",
                "video": "",
                "content": """
CSS controls the appearance of a web page.

CSS can change:
- Colors
- Fonts
- Spacing
- Layout
                """,

                "example": """
h1 {
    font-size: 32px;
}
                """,

                "practice": [
                    "Change the color of a heading.",
                    "Change the font size of a paragraph."
                ],

                "quiz": [
                    {
                        "question": "What does CSS control?",
                        "options": ["Appearance", "Database", "Python", "Server"],
                        "answer": "Appearance"
                    }
                ]
            },

            {
                "title": "JavaScript Basics",
                "video": "",
                "content": """
JavaScript adds behavior and interactivity to web pages.
                """,

                "example": """
<button onclick="alert('Hello!')">
    Click Me
</button>
                """,

                "practice": [
                    "Create a button.",
                    "Display an alert when the button is clicked."
                ],

                "quiz": [
                    {
                        "question": "What does JavaScript add?",
                        "options": ["Interactivity", "Only colors", "Database tables", "Operating system"],
                        "answer": "Interactivity"
                    }
                ]
            },

            {
                "title": "Responsive Design",
                "video": "",
                "content": """
Responsive design allows websites to work on different screen sizes.

Important concepts:
- Flexible layouts
- Media queries
- Mobile-friendly design
                """,

                "example": """
@media (max-width: 600px) {
    body {
        font-size: 16px;
    }
}
                """,

                "practice": [
                    "Create a mobile-friendly page.",
                    "Use a media query."
                ],

                "quiz": [
                    {
                        "question": "What is responsive design?",
                        "options": [
                            "Design that adapts to screen size",
                            "A database",
                            "A programming language",
                            "A server"
                        ],
                        "answer": "Design that adapts to screen size"
                    }
                ]
            }
        ],

        "final_quiz": [
            {
                "question": "What provides webpage structure?",
                "options": ["HTML", "CSS", "SQL", "Docker"],
                "answer": "HTML"
            },
            {
                "question": "What controls webpage appearance?",
                "options": ["CSS", "HTML", "Python", "SQL"],
                "answer": "CSS"
            },
            {
                "question": "What adds interactivity?",
                "options": ["JavaScript", "HTML", "SQL", "Git"],
                "answer": "JavaScript"
            }
        ]
    },


    # ==========================================================
    # GIT & GITHUB
    # ==========================================================

    "git": {
        "title": "Git & GitHub",
        "description": "Learn version control and collaborative development.",
        "icon": "🔀",

        "lessons": [

            {
                "title": "Git Basics",
                "video": "",
                "content": """
Git is a version control system.

It helps developers track changes in code.
                """,

                "example": """
git init
                """,

                "practice": [
                    "Create a Git repository.",
                    "Check the Git status."
                ],

                "quiz": [
                    {
                        "question": "What is Git?",
                        "options": [
                            "Version control system",
                            "Database",
                            "Programming language",
                            "Operating system"
                        ],
                        "answer": "Version control system"
                    }
                ]
            },

            {
                "title": "Git Workflow",
                "video": "",
                "content": """
A common Git workflow is:

Working Directory
       ↓
Staging Area
       ↓
Repository
                """,

                "example": """
git add .
git commit -m "Initial commit"
                """,

                "practice": [
                    "Stage a file.",
                    "Create a commit."
                ],

                "quiz": [
                    {
                        "question": "Which command stages files?",
                        "options": ["git add", "git save", "git stagefile", "git push"],
                        "answer": "git add"
                    }
                ]
            },

            {
                "title": "GitHub",
                "video": "",
                "content": """
GitHub is a platform for hosting and collaborating on Git repositories.
                """,

                "example": """
git push origin main
                """,

                "practice": [
                    "Create a GitHub repository.",
                    "Push a project to GitHub."
                ],

                "quiz": [
                    {
                        "question": "What is GitHub?",
                        "options": [
                            "Code hosting and collaboration platform",
                            "Database",
                            "Compiler",
                            "Operating system"
                        ],
                        "answer": "Code hosting and collaboration platform"
                    }
                ]
            },

            {
                "title": "Branches",
                "video": "",
                "content": """
Branches allow developers to work on different versions of a project independently.
                """,

                "example": """
git branch feature
git checkout feature
                """,

                "practice": [
                    "Create a feature branch.",
                    "Switch between branches."
                ],

                "quiz": [
                    {
                        "question": "Why are branches used?",
                        "options": [
                            "Independent development",
                            "Deleting repositories",
                            "Installing Python",
                            "Creating databases"
                        ],
                        "answer": "Independent development"
                    }
                ]
            }
        ],

        "final_quiz": [
            {
                "question": "What is Git?",
                "options": [
                    "Version control system",
                    "Database",
                    "Programming language",
                    "Browser"
                ],
                "answer": "Version control system"
            },
            {
                "question": "Which command stages files?",
                "options": ["git add", "git push", "git run", "git stage"],
                "answer": "git add"
            },
            {
                "question": "Which command sends commits to GitHub?",
                "options": ["git push", "git add", "git save", "git upload"],
                "answer": "git push"
            }
        ]
    },


    # ==========================================================
    # DOCKER
    # ==========================================================

    "docker": {
        "title": "Docker & Containerization",
        "description": "Learn containerization and Docker fundamentals.",
        "icon": "🐳",

        "lessons": [

            {
                "title": "Docker Basics",
                "video": "",
                "content": """
Docker is a platform used to build and run applications inside containers.

Containers package an application with its dependencies.
                """,

                "example": """
docker --version
                """,

                "practice": [
                    "Check whether Docker is installed.",
                    "Explain what a container is."
                ],

                "quiz": [
                    {
                        "question": "What is Docker mainly used for?",
                        "options": [
                            "Containerization",
                            "Spreadsheet editing",
                            "Image editing",
                            "Database design"
                        ],
                        "answer": "Containerization"
                    }
                ]
            },

            {
                "title": "Docker Images",
                "video": "",
                "content": """
A Docker image contains the instructions and files required to create a container.
                """,

                "example": """
docker pull python
                """,

                "practice": [
                    "Pull a Docker image.",
                    "List Docker images."
                ],

                "quiz": [
                    {
                        "question": "What is used to create a container?",
                        "options": [
                            "Docker image",
                            "Git branch",
                            "SQL table",
                            "Python variable"
                        ],
                        "answer": "Docker image"
                    }
                ]
            },

            {
                "title": "Docker Containers",
                "video": "",
                "content": """
A container is a running instance of a Docker image.
                """,

                "example": """
docker run python
                """,

                "practice": [
                    "Run a Docker container.",
                    "List running containers."
                ],

                "quiz": [
                    {
                        "question": "A running instance of an image is called what?",
                        "options": ["Container", "Repository", "Branch", "Package"],
                        "answer": "Container"
                    }
                ]
            },

            {
                "title": "Dockerfile",
                "video": "",
                "content": """
A Dockerfile contains instructions used to build a Docker image.
                """,

                "example": """
FROM python:3.13

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
                """,

                "practice": [
                    "Create a simple Dockerfile.",
                    "Build an image using a Dockerfile."
                ],

                "quiz": [
                    {
                        "question": "Which file contains Docker build instructions?",
                        "options": ["Dockerfile", "docker.txt", "container.py", "image.txt"],
                        "answer": "Dockerfile"
                    }
                ]
            }
        ],

        "final_quiz": [
            {
                "question": "What is Docker mainly used for?",
                "options": [
                    "Containerization",
                    "Database management",
                    "Video editing",
                    "Web browsing"
                ],
                "answer": "Containerization"
            },
            {
                "question": "What creates a container?",
                "options": [
                    "Docker image",
                    "Python file",
                    "Git branch",
                    "SQL query"
                ],
                "answer": "Docker image"
            },
            {
                "question": "Which file defines image build instructions?",
                "options": [
                    "Dockerfile",
                    "docker.py",
                    "image.txt",
                    "container.txt"
                ],
                "answer": "Dockerfile"
            }
        ]
    }
}