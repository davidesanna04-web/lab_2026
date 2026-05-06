from pydantic import BaseModel
from typing import Annotated
from sqlmodel import SQLModel,Field

class BookBase(SQLModel):
    title:str
    author:str
    review: Annotated[int,Field(ge=1,le=5)]=None

class BookCreate(BookBase):
    pass


class BookPublic(BookBase):
    id:int

class BookDB(BookBase, table=True):
    id:int = Field(default=None, primary_key=True)

class Book(SQLModel,table=True):
    id: int
    title: str
    author: str
    review: Annotated[int, Field(ge=1, le=5)] = None


    model_config = {
        "json_schema_extra": {
            "example": [{
                "id": 1,
                "title": "Il nome della rosa",
                "author": "Umberto Eco",
                "review": 5
            }
        ]
        }
    }

books = {
    0: Book(id=0, title="Il nome della rosa", author= "Umberto eco", review=5 ),
    1: Book(id=1, title="Il giovo del sei", author= "davide ", review=4 ),
    2: Book(id=2, title="Il gioco dei sette", author= "ciao ", review=3 )
}


b = Book(id=1, title= "Test", author="test")
b.title
