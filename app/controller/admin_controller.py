from fastapi import APIRouter
from app.model.admin_model import Admin
from app.service.admin_service import AdminServices
from app.config.logger_config import get_logger

admin_route = APIRouter()
logger = get_logger()

@admin_route.post('/admin')
async def post_admin(admin: Admin):
   response = await AdminServices.create_admin(admin)
   return response
