Library Manager
Description
Library Manager is a console-based library management application written in Python.
The application allows users to manage books, users, genres and borrowing operations. The project combines SQLite database functionality with object-oriented programming principles.

The project demonstrates CRUD operations, SQL JOIN queries, aggregation functions, GROUP BY, HAVING, inheritance, polymorphism, encapsulation, abstraction, multiple inheritance and magic methods.

Features
Book Management
Add books
View all books
Find books by title or author
View a book by ID
Update book information
Delete books
Check book availability
User Management
Add users
View users
Update user email
Delete users
User password encapsulation
Genre Management
Add genres
View genres
Delete genres
Borrowing
Borrow books
Return books
Check book availability before borrowing
Check that the book and user exist
Store borrowing history
Store borrow and return dates
Statistics
The application provides:
Total number of books
Total number of users
Average publication year
Oldest publication year
Newest publication year
Total number of borrowings
Sum of publication years
Number of books by genre
Number of books by author
Number of borrowings by user
Popular genres using HAVING
Active users using HAVING
SQL
The project uses SQLite and Python's built-in sqlite3 module.
The database contains four main tables:

books
users
genres
borrowings
Database relationships:
genres 1 ─── N books

users 1 ─── N borrowings

books 1 ─── N borrowings

The database uses:
PRIMARY KEY
FOREIGN KEY
NOT NULL
UNIQUE
SQL features used in the project:
INSERT
SELECT
UPDATE
DELETE
INNER JOIN
COUNT()
SUM()
AVG()
MIN()
MAX()
GROUP BY
HAVING
Object-Oriented Programming
The project contains separate classes for the main entities.
User and Admin
Admin inherits from User.
User
└── Admin

Both classes implement get_permissions() differently, demonstrating polymorphism.
Abstraction
The abstract class LibraryItem is used as a base class.
LibraryItem
├── Book
└── Magazine

LibraryItem contains an abstract get_info() method.
Encapsulation
The User class contains private attributes:
__password
__books

Access to the user's books is provided through a property.
Password operations are implemented using:

check_password()
change_password()
Multiple Inheritance
Book inherits from several classes:
class Book(LibraryItem, Printable, Borrowable):
    ...

The project demonstrates the Method Resolution Order (MRO).
Magic Methods
The Book class implements:
__str__()
__repr__()
__eq__()
__len__()
Static Method
The Book class contains:
Book.is_valid_year(year)

It checks whether a publication year is valid.
Class Method
The Book class contains:
Book.from_string(...)

It creates a book object from a string:
Python Basics;John Smith;2024;Programming

Project Structure
library_manager/
│
├── database/
│   ├── connection.py
│   ├── models.py
│   ├── queries.py
│   └── __init__.py
│
├── models/
│   ├── book.py
│   ├── user.py
│   ├── admin.py
│   ├── library_item.py
│   ├── magazine.py
│   ├── printable.py
│   └── borrowable.py
│
├── services/
│   └── library_service.py
│
├── main.py
├── library.db
├── .gitignore
└── README.md

Technologies
Python 3
SQLite
sqlite3
SQL
Object-Oriented Programming
Git
GitHub
How to Run
Clone the repository and open the project directory.
Run:

python3 main.py

The application starts with a console menu.
Application Menu
=== LIBRARY MANAGER ===

1. Add book
2. Show books
3. Find book
4. Update book
5. Delete book

6. Add user
7. Show users
8. Delete user
9. Update user email

10. Borrow book
11. Return book
12. Borrowing history

13. Statistics
14. Book details

15. Add genre
16. Show genres
17. Delete genre
18. Books with authors and genres

0. Exit

Example
Example of displaying books:
=== BOOKS ===
ID: 1 | Advanced Python | Author: John Smith | Year: 2025 | Genre ID: 1 | Available
ID: 4 | Python Basics | Author: John Smith | Year: 2024 | Genre ID: 1 | Available

Example of borrowing:
=== BORROW BOOK ===
Book borrowed successfully.

Example of statistics:
=== STATISTICS ===
Books: 2
Users: 2
Average publication year: 2024.5
Oldest publication year: 2024
Newest publication year: 2025
Borrowings: 1
Sum of publication years: 4049

Git
The project was developed using Git feature branches.
Branches:

main
develop
feature/database
feature/oop

The project uses separate feature branches for database and object-oriented functionality.
The completed features were merged into develop and then into main.

The project contains more than 10 meaningful commits describing the development stages.

Repository
The project is hosted on GitHub:
https://github.com/cosinyz/library_manager