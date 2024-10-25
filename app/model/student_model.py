from pydantic import BaseModel

class Student(BaseModel):
    user_name:str
    pass_hass:str

