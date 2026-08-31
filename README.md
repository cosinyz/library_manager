Library Manager
Library Manager is a console-based library management application written in Python.
The project uses SQLite for data storage and demonstrates CRUD operations, SQL queries, object-oriented programming, inheritance, polymorphism, encapsulation, and database relationships.

Features
Add, update, delete and view books
Search books by title or author
Add, update and delete users
Add and delete genres
Borrow and return books
View borrowing history
View library statistics
SQL JOIN queries
Aggregation queries with COUNT, AVG, MIN, MAX and SUM
Object-oriented models for books and users
User and Admin roles
Encapsulation and password management
Polymorphism and multiple inheritance
Technologies
Python 3
SQLite
SQL
Object-Oriented Programming
Git
Project Structure
library_manager/
│
├── database/
│   ├── connection.py
│   ├── schema.py
│   └── queries.py
│
├── models/
│   ├── book.py
│   ├── user.py
│   ├── admin.py
│   ├── library_item.py
│   ├── borrowable.py
│   └── printable.py
│
├── services/
│   └── library_service.py
│
├── main.py
├── library.db
├── .gitignore
└── README.md

How to Run
Clone or open the project and run:
python3 main.py

The application provides a console menu for managing books, users, genres and borrowing operations.
Database
The application uses SQLite.
The main database tables are:

books
users
genres
borrowings
The database stores books, users, genres and the history of borrowing and returning books.
Git Branches
The project is developed using Git feature branches.
Current development branch:

feature/database