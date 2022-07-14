# Library Management System

This project contains backend API's for a simple library management system. The functionalities include:

There are two roles in the system; LIBRARIAN and MEMBER

As a User:

1. I can signup either as LIBRARIAN and MEMBER using username and password
2. I can login using username/password and get JWT access token

As a Librarian:

1. I can add, update, and remove Books from the system
2. I can add, update, view, and remove Member from the system

As a Member:

1. I can view, borrow, and return available Books
2. Once a book is borrowed, its status will change to BORROWED
3. Once a book is returned, its status will change to AVAILABLE
4. I can delete my own account

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the solution.

```bash
pip install -r requirements.txt
```
