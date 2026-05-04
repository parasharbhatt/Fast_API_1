# Fast_API_1
Fast_API_1 for testing

Project Setup:
Create a project folder and setup for Git
along with .Gitignore, readme.md, license

Create venv and activate it

update .gitignore to exclude .venv setup and files/folders related to it.

Need to install:

pip install fastapi uvicorn sqlalchemy pyodbc pydantic

Note: Ensure you have the Microsoft ODBC Driver for SQL Server installed on your system:
             msodbcsql.msi for the version of SQL Server


Launch your API using Uvicorn: [1, 2]
bash
uvicorn main:app –reload

Use code with caution.
Once running, navigate to http://127.0.0.1:8000/docs 
      to access the interactive Swagger UI 
      for testing your endpoints


To run server from terminal: uvicorn main:app –reload
To test:
http://127.0.0.1:8000/docs#/default/read_user_users__user_id__get
http://127.0.0.1:8000/docs#/default/create_user_users__post

