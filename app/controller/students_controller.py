from fastapi import APIRouter
from app.model.student_model import Student
from app.service.student_service import StudentService

student_route = APIRouter()

@student_route.get('/student/')
async def get_student():
    reponse = await StudentService.read_student()
    return reponse

@student_route.post('/student')
async def post_student(student: Student):
   response = await StudentService.create_student(student)
   return response

@student_route.put('/student/{id}')
async def update_student(id:str,student:Student):
    response = await StudentService.update_student(id,student)
    return response

@student_route.delete('/admim/{id}')
async def delete_student(id:str):
    response = await StudentService.delete_student(id)
    return response
