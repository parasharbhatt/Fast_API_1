# Fast_API_1

## Project Category

**EDA (Data Analysis)** · **Data Engineering** · **API Development** · **Backend Development**

## Tools

**Python** · **FastAPI** · **SQLAlchemy** · **Microsoft SQL Server** · **pyodbc** · **Pydantic** · **Uvicorn** · **Swagger / OpenAPI** · **unittest**

### Tags

`EDA` `Data Analysis` `Data Engineering` `Python` `FastAPI` `REST API` `SQLAlchemy` `Microsoft SQL Server` `pyodbc` `Pydantic` `Uvicorn` `Swagger` `OpenAPI` `unittest`

About Project:

The code is developed for API GET and POST methods using 'FASTAPI'.
The application connects SQL Server database using environment variables.
Users can retrieve user information and a FilmDetail view record by FilmID using GET endpoints, and add user information (Name and Email) using the POST endpoint.

Interactive Swagger UI is used for testing the GET and POST endpoints.



Fast_API_1 for testing

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

TCP is enabled for SQL Server.

userid and password saved in environment variable.

Launch your API using Uvicorn: \[1, 2]
bash
Scripts\uvicorn main:app –reload  or just uvicorn main:app


Once running, navigate to http://127.0.0.1:8000/docs
to access the interactive Swagger UI
for testing your endpoints



To run server from terminal: uvicorn main:app –reload or just uvicorn main:app

To test API:
http://127.0.0.1:8000/docs#/default/read\_user\_users\_\_user\_id\_\_get
http://127.0.0.1:8000/docs#/default/create\_user\_users\_\_post
http://127.0.0.1:8000/docs#/default/read\_film\_details\_film\_details\_\_film\_id\_\_get

The `GET /film-details/{film_id}` endpoint returns the matching row from the SQL Server
`FilmDetail` view, or a 404 response if the FilmID is not found.

Run the integration tests with `.\Scripts\python.exe -m unittest -v test_main.py`. They use
the configured Movies SQL Server database and create then remove a temporary user record.
Each run saves a detailed report to `test_report.txt` in the project root; Git ignores this
generated report.

