from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
import models, database

app = FastAPI()

# Create tables in SQL Server on startup
models.Base.metadata.create_all(bind=database.engine)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(database.get_db)):
    new_user = models.User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/film-details/{film_id}")
def read_film_details(film_id: int, db: Session = Depends(database.get_db)):
    result = db.execute(
        text("SELECT * FROM FilmDetail WHERE Filmid = :film_id"),
        {"film_id": film_id},
    )
    film = result.mappings().first()
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return dict(film)
