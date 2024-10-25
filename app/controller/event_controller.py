from fastapi import APIRouter
from app.model.events_model import Event
from app.service.event_service import EventService
from app.model.events_model import Event


event_route = APIRouter()

@event_route.get("/event")
async def read_event():
    response =await EventService.read_event()  
    return response
    
@event_route.post("/event")
async def post_event(event:Event):
    response =await EventService.create_event(event)
    return response
    
@event_route.delete("/event/{mentor_id}")
async def del_event(mentor_id:str):
    response = await EventService.delete_event(mentor_id)
    return response

@event_route.put("/event/{mentor_id}")
async def put_event(mentor_id:str, event:Event):
    response = await EventService.update_event(mentor_id, event)
    return response