from app.repositories.event_repo import EventRepo
from app.model.events_model import Event

class EventService:

    @staticmethod
    async def create_event(event: Event):
        result = await EventRepo.create_event(event)
        return result
    
    @staticmethod
    async def read_event():
        result = await EventRepo.get_all_event()
        return result
    
    @staticmethod
    async def delete_event(mentor_id:str):
        result= await EventRepo.delete_event(mentor_id)
        return result

    @staticmethod
    async def update_event(mentor_id: str, event: Event):
        result= await EventRepo.update_event(mentor_id, event)
        return result
    
