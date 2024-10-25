from app.config.db_config import attendence_collection
from bson import ObjectId
from app.model.attendance_model import Attendance

class AttendanceRepo:
    @staticmethod
    async def create_attendance(attendance: dict):
        response = await attendence_collection.insert_one(attendance)
        return {"inserted_id": str(response.inserted_id)}
    
    @staticmethod
    async def get_all_attendence():
        cursor = attendence_collection.find({})
        attendence = []
        async for admin in cursor:
            admin["_id"] = str(admin["_id"])
            attendence.append(admin)
        return attendence
    
    @staticmethod
    async def read_attendance(attendance_id: str):
        _id = ObjectId(attendance_id)
        attendance = await attendence_collection.find_one({"_id": _id})
        if attendance:
            attendance["_id"] = str(attendance["_id"])
            return attendance
        return {"error": "Attendance ID not found"}

    @staticmethod
    async def delete_attendance(attendance_id: str):
        _id = ObjectId(attendance_id)
        result = await attendence_collection.delete_one({"_id": _id})
        if result.deleted_count > 0:
            return {"message": "Student attendance deleted successfully"}
        return {"error": "Error while deleting"}
        
    @staticmethod
    async def update_attendance(attendance_id: str, attendance: Attendance):
        _id = ObjectId(attendance_id)
        result = await attendence_collection.update_one({"_id": _id}, {"$set": attendance.dict()})
        if result.modified_count > 0:
            return {"message": "Student attendance updated successfully"}
        return {"error": "Error updating attendance"}