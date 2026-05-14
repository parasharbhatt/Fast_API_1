# Fast\_API\_1


About Project:

The code is developed for API Get and Post method using 'FASTAPI'.
It connects SQL Server database using environment variable
It lets retrieve user information using Get method and Lets to add
user info (Name and Email) using POST method.

Interactive Swagger UI is used for testing both (GET and POST) endpoints.



Fast\_API\_1 for testing

Project Setup:
Create a project folder and setup for Git
along with .Gitignore, readme.md, license

Create venv and activate it

update .gitignore to exclude .venv setup and files/folders related to it.

Need to install:
Python version used: 3.12.1
pip install fastapi uvicorn sqlalchemy pyodbc pydantic

Note: Ensure you have the Microsoft ODBC Driver for SQL Server installed on your system:
("msodbcsql.msi") for the version of your SQL Server



Launch your API using Uvicorn: \[1, 2]
bash
uvicorn main:app –reload  or just uvicorn main:app

Use code with caution.
Once running, navigate to http://127.0.0.1:8000/docs
to access the interactive Swagger UI
for testing your endpoints



To run server from terminal: uvicorn main:app –reload or just uvicorn main:app

To test API:
http://127.0.0.1:8000/docs#/default/read\_user\_users\_\_user\_id\_\_get
http://127.0.0.1:8000/docs#/default/create\_user\_users\_\_post

