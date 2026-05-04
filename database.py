from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base
import os
# Replace with your actual SQL Server details
# Example: Server=localhost\SQLEXPRESS; Database=TestDB;

SERVER = 'PB_DELL_M18'
DATABASE = 'Movies'
username = os.getenv('testuser')
password = os.getenv('testpswd')
DRIVER = 'ODBC Driver 18 for SQL Server'
port = 1433
connection_url = URL.create(
    "mssql+pyodbc",
    username=username,
    password=password,  # No need to manually escape special characters here
    host=SERVER,
    port=1433,
    database=DATABASE,
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
        "Encrypt": "yes"
    }
)

print(connection_url)

#DATABASE_URL = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"
#engine = create_engine(DATABASE_URL)
engine = create_engine(connection_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
