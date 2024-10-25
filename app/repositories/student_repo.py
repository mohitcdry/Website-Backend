    
from app.config.db_config import student_collection
from bson import ObjectId
from app.model.student_model import Student

class StudentsRepo:
    @staticmethod
    async def create_students(students: Student):
        result = await student_collection.insert_one(students.dict())
        return {"inserted_id": str(result.inserted_id)}
    
    # @staticmethod
    # async def read_students( student_id: str):
    #     _id=ObjectId(student_id)
    #     result = await student_collection.find_one({"_id":_id})
    #     if result:
    #         return result
    #     else:
    #         return "ID not found"
        
    @staticmethod
    async def read_student(student_id: str):
        _id = ObjectId(student_id)
        student = await student_collection.find_one({"_id": _id})
        if student:
            student["_id"] = str(student["_id"])
            return student
        return {"error": "Student ID not found"}

    @staticmethod
    async def get_all_student():
        cursor = student_collection.find({})
        student = []
        async for admin in cursor:
            admin["_id"] = str(admin["_id"])
            student.append(admin)
        return student
        
    @staticmethod
    async def delete_students(student_id:str):
        _id=ObjectId(student_id)
        result=await student_collection.delete_one({"_id":_id})
        if result:
            return "student deleted sucessfully from database"
        else:
            return "Error while deleting"
        
    @staticmethod
    async def update_students(student_id: str, students: Student):
        _id=ObjectId(student_id)
        result=await student_collection.update_one({"_id":_id},{"$set":students.dict()})
        if result.modified_count>0:
            return "student updated sucessfully"
        else:
            return "error updating student"