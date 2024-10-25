from app.config.db_config import mentors_collection
from bson import ObjectId
from app.model.mentors_model import Mentors

class MentorsRepo:
    @staticmethod
    async def create_mentors(mentors: Mentors):
        result = await mentors_collection.insert_one(mentors.dict())
        return {"inserted_id": str(result.inserted_id)}
    
    @staticmethod
    async def get_all_mentors():
        cursor = mentors_collection.find({})
        mentors = []
        async for admin in cursor:
            admin["_id"] = str(admin["_id"])
            mentors.append(admin)
        return mentors
    
    @staticmethod
    async def read_mentors(mentors_id: str):
        _id = ObjectId(mentors_id)
        mentors = await mentors_collection.find_one({"_id": _id})
        if mentors:
            mentors["_id"] = str(mentors["_id"])
            return mentors
        return {"error": "Mentors ID not found"}

    # @staticmethod
    # async def read_mentors( mentor_id: str):
    #     _id=ObjectId(mentor_id)
    #     result = await mentors_collection.find_one({"_id":_id})
    #     if result:
    #         return result
    #     else:
    #         return "ID not found"
        
    @staticmethod
    async def delete_mentors(mentor_id:str):
        _id=ObjectId(mentor_id)
        result=await mentors_collection.delete_one({"_id":_id})
        if result:
            return "mentor deleted sucessfully from database"
        else:
            return "Error while deleting"
        
    @staticmethod
    async def update_mentors(mentor_id: str, mentors: Mentors):
        _id=ObjectId(mentor_id)
        result=await mentors_collection.update_one({"_id":_id},{"$set":mentors.dict()})
        if result.modified_count>0:
            return "mentor updated sucessfully"
        else:
            return "error updating mentor"
        
