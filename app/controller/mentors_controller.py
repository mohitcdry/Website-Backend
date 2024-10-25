from fastapi import APIRouter
from app.model.mentors_model import Mentors
from app.service.mentors_service import MentorService
from app.model.mentors_model import Mentors


mentors_route = APIRouter()

# mentors_route.get("/mentors")
# async def list_mentorss(mentors:Mentors):
#     response = await MentorService.list_mentors(mentors)
#     return response

@mentors_route.get("/mentors")
async def read_mentors():
    response =await MentorService.read_mentors()  
    return response
    
@mentors_route.post("/mentors")
async def post_mentors(mentors:Mentors):
    response =await MentorService.create_mentors(mentors)
    return response
    
@mentors_route.delete("/mentors/{mentor_id}")
async def del_mentors(mentor_id:str):
    response = await MentorService.delete_mentors(mentor_id)
    return response

@mentors_route.put("/mentors/{mentor_id}")
async def put_mentors(mentor_id:str, mentors:Mentors):
    response = await MentorService.update_mentors(mentor_id, mentors)
    return response