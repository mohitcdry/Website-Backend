from fastapi import APIRouter
from app.model.school_model import School
from app.service.school_service import SchoolService

school_route = APIRouter()

# @school_route.get("/schools")
# async def list_schools():
#     response = await Schoolservice.list_school()
#     return response

@school_route.get("/school")
async def get_school():
    response =await SchoolService.read_school() 
    return response
    
@school_route.post("/school")
async def post_school(school:School):
    response =await SchoolService.create_school(school)
    return response
    
@school_route.delete("/School/{school_id}")
async def del_school(school_id:str):
    response = await SchoolService.delete_school(school_id)
    return response

@school_route.put("/school/{school_id}")
async def put_school(school_id:str, school:School):
    response = await SchoolService.update_school(school_id, school)
    return response
