from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace with your actual SQL Server details
# Example: Server=localhost\SQLEXPRESS; Database=TestDB;
SERVER = ': PB_DELL_M18'
DATABASE = 'Movies'
DRIVER = 'ODBC+Driver+18+for+SQL+Server'

DATABASE_URL = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
