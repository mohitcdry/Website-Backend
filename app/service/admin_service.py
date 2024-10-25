from app.repositories.admin_repo import AdminRepo
from app.model.admin_model import Admin
from bson import ObjectId

class AdminServices:
    @staticmethod
    async def create_admin(admin: Admin):
        result = await AdminRepo.create_admin(admin.dict())
        return result