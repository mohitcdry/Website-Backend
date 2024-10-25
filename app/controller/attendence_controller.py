from fastapi import APIRouter
from app.model.attendance_model import Attendance
from app.service.attendence_service import AttendanceService
from app.config.logger_config import get_logger

attendence_route = APIRouter()
logger=get_logger()

@attendence_route.get('/attendance')
async def get_all():
   logger.info(f"ENDPOINT CALLED: / Attendances Reterived Sucessfully")
   response = await AttendanceService.get_all()
   return response


@attendence_route.get('/attendance')
async def get_attendence():
   response = await AttendanceService.get_attendance()
   return response

@attendence_route.post('/attendance')
async def post_attendence(attendance: Attendance):
    response = await AttendanceService.create_attendance(attendance)
    return response


# @attendence_route.put('/student/{id}')
# async def update_attendence():
#     response = await AttendanceService.update_attendence(id)
#     return response

@attendence_route.delete('/student/{id}')
async def delete_attendence(id: str):
    response = await AttendanceService.delete_attendance(id)
    return response