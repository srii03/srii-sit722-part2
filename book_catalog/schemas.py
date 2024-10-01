from pydantic import BaseModel

# Define your Pydantic models here

class BookBase(BaseModel):
    title: str
    author: str
    year: int

class BookCreate(BookBase):
    pass

class BookInDB(BookBase):
    id: int

    class Config:
        from_attributes = True  # Change 'orm_mode' to 'from_attributes'

class BookUpdate(BaseModel):
    title: str = None
    author: str = None
    year: int = None

