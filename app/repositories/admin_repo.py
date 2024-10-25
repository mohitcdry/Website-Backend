from app.config.db_config import admin_collection
from bson import ObjectId
from app.model.admin_model import Admin

class AdminRepo:
    @staticmethod
    async def create_admin(admin: dict):
        response = await admin_collection.insert_one(admin)
        return {"inserted_id": str(response.inserted_id)}
    
   
        
    
    