    
from app.config.db_config import school_collection
from bson import ObjectId
from app.model.school_model import School

class SchoolsRepo:
    @staticmethod
    async def create_schools(schools: School):
        result = await school_collection.insert_one(schools.dict())
        return {"inserted_id": str(result.inserted_id)}
    
    # @staticmethod
    # async def read_schools( school_id: str):
    #     _id=ObjectId(school_id)
    #     result = await school_collection.find_one({"_id":_id})
    #     if result:
    #         return result
    #     else:
    #         return "ID not found"
        
    @staticmethod
    async def read_school(school_id: str):
        _id = ObjectId(school_id)
        school = await school_collection.find_one({"_id": _id})
        if school:
            school["_id"] = str(school["_id"])
            return school
        return {"error": "School ID not found"}

    @staticmethod
    async def get_all_school():
        cursor = school_collection.find({})
        school = []
        async for admin in cursor:
            admin["_id"] = str(admin["_id"])
            school.append(admin)
        return school
        
    @staticmethod
    async def delete_schools(school_id:str):
        _id=ObjectId(school_id)
        result=await school_collection.delete_one({"_id":_id})
        if result:
            return "school deleted sucessfully from database"
        else:
            return "Error while deleting"
        
    @staticmethod
    async def update_schools(school_id: str, schools: School):
        _id=ObjectId(school_id)
        result=await school_collection.update_one({"_id":_id},{"$set":schools.dict()})
        if result.modified_count>0:
            return "school updated sucessfully"
        else:
            return "error updating school"