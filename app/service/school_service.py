from app.repositories.school_repo import SchoolsRepo
from app.model.school_model import School

class SchoolService:
    @staticmethod
    async def create_school(school: School):
        result = await SchoolsRepo.create_schools(school)
        return result
    
    @staticmethod
    async def read_school():
        result = await SchoolsRepo.get_all_school()
        return result
    
    @staticmethod
    async def delete_school(school_id:str):
        result= await SchoolsRepo.delete_schools(school_id)
        return result

    @staticmethod
    async def update_school(school_id: str, school: School):
        result= await SchoolsRepo.update_schools(school_id, school)
        return result
    
