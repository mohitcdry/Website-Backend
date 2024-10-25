from pydantic import BaseModel

class Mentors(BaseModel):
    user_name:str
    pass_hass:str