from fastapi import APIRouter
from app.model.feedback_model import Feedback
from app.service.feedback_service import feedbackservice



feedback_route = APIRouter()


@feedback_route.get("/feedback")
async def read_feedback():
    response =await feedbackservice.read_feedback()  
    return response
    
@feedback_route.post("/feedback")
async def post_feedback(feedback:Feedback):
    response =await feedbackservice.create_feedback(feedback)
    return response
    
@feedback_route.delete("/feedback/{feedback_id}")
async def del_feedback(feedback_id:str):
    response = await feedbackservice.delete_feedback(feedback_id)
    return response

@feedback_route.put("/feedback/{feedback_id}")
async def put_feedback(feedback_id:str, feedback:Feedback):
    response = await feedbackservice.update_feedback(feedback_id, feedback)
    return response