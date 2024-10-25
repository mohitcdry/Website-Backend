from app.repositories.feedback_repo import feedbackRepo
from app.model.feedback_model import Feedback

class feedbackservice:
    @staticmethod
    async def create_feedback(feedback: Feedback):
        result = await feedbackRepo.create_feedback(feedback)
        return result
    
    @staticmethod
    async def read_feedback():
        result = await feedbackRepo.get_all_feedback()
        return result
    
    @staticmethod
    async def delete_feedback(feedback_id:str):
        result= await feedbackRepo.delete_feedback(feedback_id)
        return result

    @staticmethod
    async def update_feedback(feedback_id: str, feedback: Feedback):
        result= await feedbackRepo.update_feedback(feedback_id, feedback)
        return result
    