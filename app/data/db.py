from sqlmodel import create_engine,SQLModel, Session
from typing import Annotated
from fastapi import  Depends
from schemas.book import BookDB 

sqlite_file_name = "/home/davide/lab_2026/app/data/database.db"
sqlite_url = f"sqlite://{sqlite_file_name}"
engine = create_engine(
    sqlite_url, 
    connect_args={"check_same_thread": False}, 
    echo = True
)#crea il motore del DB

def init_database():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep= Annotated[Session,Depends(get_session)]










