from typing import Optional
from pydantic import BaseModel

class Admin(BaseModel):
    id:Optional[int] = None
    user_name:str   
    pass_hass:str

#Hello