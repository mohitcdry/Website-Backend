from app.config.db_config import feedback_collection
from bson import ObjectId
from app.model.feedback_model import Feedback

class feedbackRepo:
    @staticmethod
    async def create_feedback(feedback: Feedback):
        result = await feedback_collection.insert_one(feedback.dict())
        return {"inserted_id": str(result.inserted_id)}
    

    @staticmethod
    async def get_all_feedback():
        cursor = feedback_collection.find({})
        feedback = []
        async for admin in cursor:
            admin["_id"] = str(admin["_id"])
            feedback.append(admin)
        return feedback
    
    @staticmethod
    async def read_feedback(feedback_id: str):
        _id = ObjectId(feedback_id)
        feedback = await feedback_collection.find_one({"_id": _id})
        if feedback:
            feedback["_id"] = str(feedback["_id"])
            return feedback
        return {"error": "Feedback ID not found"}

    # @staticmethod
    # async def read_feedback( feedback_id: str):
    #     _id=ObjectId(feedback_id)
    #     result = await feedback_collection.find_one({"_id":_id})
    #     if result:
    #         return result
    #     else:
    #         return "ID not found"
        
    @staticmethod
    async def delete_feedback(feedback_id:str):
        _id=ObjectId(feedback_id)
        result=await feedback_collection.delete_one({"_id":_id})
        if result:
            return "feedback deleted sucessfully from database"
        else:
            return "Error while deleting"
        
    @staticmethod
    async def update_feedback(feedback_id: str, feedback: Feedback):
        _id=ObjectId(feedback_id)
        result=await feedback_collection.update_one({"_id":_id},{"$set":feedback.dict()})
        if result.modified_count>0:
            return "feedback updated sucessfully"
        else:
            return "error updating feedback"

