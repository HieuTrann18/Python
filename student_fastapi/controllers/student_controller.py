from fastapi import HTTPException
from typing import List, Optional
from models import Student
from services import create_student, get_all_students, find_student, update_student, delete_student

def create_student_controller(id: int, name: str, age: int, email: Optional[str]) -> Student:
    try:
        return create_student(id, name, age, email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_students_controller() -> List[Student]:
    return get_all_students()

def get_student_controller(student_id: int) -> Student:
    student = find_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

def update_student_controller(student_id: int, name: Optional[str], age: Optional[int], email: Optional[str]) -> Student:
    try:
        return update_student(student_id, name, age, email)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

def delete_student_controller(student_id: int):
    try:
        delete_student(student_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
