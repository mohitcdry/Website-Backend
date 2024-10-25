from app.repositories.mentors_repo import MentorsRepo
from app.model.mentors_model import Mentors

class MentorService:

    @staticmethod
    async def create_mentors(mentors: Mentors):
        result = await MentorsRepo.create_mentors(mentors)
        return result
    
    @staticmethod
    async def read_mentors():
        result = await MentorsRepo.get_all_mentors()
        return result
    
    @staticmethod
    async def delete_mentors(mentor_id:str):
        result= await MentorsRepo.delete_mentors(mentor_id)
        return result

    @staticmethod
    async def update_mentors(mentor_id: str, mentors: Mentors):
        result= await MentorsRepo.update_mentors(mentor_id, mentors)
        return result
    
