from app.model.attendance_model import Attendance
from app.repositories.attendence_repo import AttendanceRepo
from app.config.db_config import attendence_collection

class AttendanceService:
    @staticmethod
    async def get_all():
        attendances = []
        async for attendance in attendence_collection.find():
            attendances.append({
                "id": str(attendance["_id"]),
                "student_id": attendance["student_id"],
                "date": attendance["date"],
                "status": attendance["status"]
            })
        return attendances
    
    @staticmethod
    async def get_attendance():
        response = await AttendanceRepo.get_all_attendence()
        return response

    @staticmethod
    async def create_attendance(attendance: Attendance):
        result = await AttendanceRepo.create_attendance(attendance.dict())
        return result

    @staticmethod
    async def update_attendance(id: str, attendance: Attendance):
        result = await AttendanceRepo.update_attendance(id, attendance)
        return result
    
    @staticmethod
    async def delete_attendance(id: str):
        response = await AttendanceRepo.delete_attendance(id)
        return response