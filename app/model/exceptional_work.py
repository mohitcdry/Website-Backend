from pydantic import BaseModel
from datetime import datetime

class ExceptionalWork(BaseModel):
    student_id:str #student_id
    title:str
    description:str
    submission_date:datetime
    