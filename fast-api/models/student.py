from pydantic import BaseModel

class Student:
    def __init__(self, id: int, name: str, age: int, grade: str):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age, "grade": self.grade}

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    grade: str | None = None

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    grade: str
    
    class Config:
            orm_mode = True