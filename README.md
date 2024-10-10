This project is a user authentication web application built using Flask, SQLite, and Jinja2.

It provides functionality for users to register, log in, and view user roles such as "Expert" users. 

The app securely stores user credentials using password hashing and allows registered users to log in, promoting users to "Expert" status via an admin feature.


Features


User Registration: New users can create an account by registering with a username and password.

User Login: Registered users can log in to the system securely using hashed passwords.

Admin Page: Admins can view the list of users and promote them to "Expert" users.

Session Management: The application uses sessions to maintain login state and prevent unauthorized access to certain pages.

Expert Users: Special users can be promoted to "Expert" status, which is reflected in the interface.

Logout: Users can log out, ending their session.



Tech Stack

Backend: Flask (Python)

Database: SQLite (local database for user storage)

Frontend: Jinja2 for templating, HTML, CSS, Bootstrap for basic styling

Security: Passwords are stored securely using werkzeug.security's generate_password_hash and check_password_hash.


Setup and Installation


Prerequisites

Python 3.x

Flask

SQLite
