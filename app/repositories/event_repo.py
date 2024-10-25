from app.config.db_config import event_collection
from bson import ObjectId
from app.model.events_model import Event

class EventRepo:
    @staticmethod
    async def create_event(event: Event):
        result = await event_collection.insert_one(event.dict())
        return {"inserted_id": str(result.inserted_id)}
    
    @staticmethod
    async def read_event(event_id: str):
        _id = ObjectId(event_id)
        event = await event_collection.find_one({"_id": _id})
        if event:
            event["_id"] = str(event["_id"])
            return event
        return {"error": "Event ID not found"}

    @staticmethod
    async def get_all_event():
        cursor = event_collection.find({})
        event = []
        async for admin in cursor:
            admin["_id"] = str(admin["_id"])
            event.append(admin)
        return event

    # @staticmethod
    # async def read_event( mentor_id: str):
    #     _id=ObjectId(mentor_id)
    #     result = await event_collection.find_one({"_id":_id})
    #     if result:
    #         return result
    #     else:
    #         return "ID not found"
        
    @staticmethod
    async def delete_event(mentor_id:str):
        _id=ObjectId(mentor_id)
        result=await event_collection.delete_one({"_id":_id})
        if result:
            return "mentor deleted sucessfully from database"
        else:
            return "Error while deleting"
        
    @staticmethod
    async def update_event(mentor_id: str, event: Event):
        _id=ObjectId(mentor_id)
        result=await event_collection.update_one({"_id":_id},{"$set":event.dict()})
        if result.modified_count>0:
            return "mentor updated sucessfully"
        else:
            return "error updating mentor"
        
