from pydantic import BaseModel

class Course(BaseModel):
    course_name:str
    course_content:str
    study_material:str
    course_duration:int