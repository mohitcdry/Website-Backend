from app.repositories.student_repo import StudentsRepo
from app.model.student_model import Student

class StudentService:
    @staticmethod
    async def create_student(student: Student):
        result = await StudentsRepo.create_students(student)
        return result
    
    @staticmethod
    async def read_student():
        result = await StudentsRepo.get_all_student()
        return result
    
    @staticmethod
    async def delete_student(student_id:str):
        result= await StudentsRepo.delete_students(student_id)
        return result

    @staticmethod
    async def update_student(student_id: str, student: Student):
        result= await StudentsRepo.update_students(student_id, student)
        return result
    
