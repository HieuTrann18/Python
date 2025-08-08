from fastapi import HTTPException
from models.student import Student, StudentCreate, StudentResponse, StudentUpdate

class StudentService:
    def __init__(self, db):
        self.db = db
    
    def create_student(self, student: StudentCreate) -> StudentResponse:
        with self.db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
            values = (student.name, student.age, student.grade)
            cursor.execute(query, values)
            conn.commit()
            student_id = cursor.lastrowid
            cursor.execute("SELECT * FROM students WHERE id = %s", (student_id, ))
            result = cursor.fetchone()
            cursor.close()
            return StudentResponse(**result)