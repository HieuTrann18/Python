from typing import List, Optional
from models import Student

students_list: List[Student] = []

def find_student(student_id: int) -> Optional[Student]:
    for student in students_list:
        if student.id == student_id:
            return student
    return None

def create_student(id: int, name: str, age: int, email: Optional[str]) -> Student:
    if find_student(id):
        raise ValueError("Student ID already exists")
    new_student = Student(id=id, name=name, age=age, email=email)
    students_list.append(new_student)
    return new_student

def get_all_students() -> List[Student]:
    return students_list

def update_student(student_id: int, name: Optional[str], age: Optional[int], email: Optional[str]) -> Student:
    student = find_student(student_id)
    if not student:
        raise ValueError("Student not found")
    if name:
        student.name = name
    if age:
        student.age = age
    if email:
        student.email = email
    return student

def delete_student(student_id: int) -> None:
    student = find_student(student_id)
    if not student:
        raise ValueError("Student not found")
    students_list.remove(student)
