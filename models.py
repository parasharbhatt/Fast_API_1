from sqlalchemy import Column, Integer, String, DateTime, BIGINT,SMALLINT
from database import Base

class Film(Base):
    __tablename__ = "Film"
    Filmid = Column(Integer, primary_key=True, index=True)
    Title = Column(String(255))
    ReleaseDate = Column(DateTime)
    DirectorID = Column(Integer)
    StudioID = Column(Integer)
    Review = Column(String)
    CountryID = Column(Integer)
    LanguageID = Column(Integer)
    GenereID = Column(Integer)
    RunTimeMinutes = Column(SMALLINT)
    CertificateID = Column(Integer)
    BudgetDollars = Column(BIGINT)
    BoxOfficeDollars = Column(BIGINT)
    OscarNominations = Column(SMALLINT)
    OscarWins = Column(SMALLINT)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, index=True)


