from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List
from controllers import (
    create_student_controller, get_students_controller, get_student_controller,
    update_student_controller, delete_student_controller
)

router = APIRouter()

# Pydantic schemas được định nghĩa luôn ở đây (bỏ schemas.py)
class StudentCreate(BaseModel):
    id: int
    name: str
    age: int
    email: Optional[str] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

@router.post("/students/")
async def create_student_endpoint(student: StudentCreate):
    new_student = create_student_controller(student.id, student.name, student.age, student.email)
    return new_student.to_dict()

@router.get("/students/")
async def read_students():
    students = get_students_controller()
    return [student.to_dict() for student in students]

@router.get("/students/{student_id}")
async def read_student(student_id: int):
    student = get_student_controller(student_id)
    return student.to_dict()

@router.put("/students/{student_id}")
async def update_student_endpoint(student_id: int, student_update: StudentUpdate):
    updated_student = update_student_controller(student_id, student_update.name, student_update.age, student_update.email)
    return updated_student.to_dict()

@router.delete("/students/{student_id}")
async def delete_student_endpoint(student_id: int):
    delete_student_controller(student_id)
    return {"message": "Student deleted successfully"}
