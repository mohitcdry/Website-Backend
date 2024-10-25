from datetime import datetime
from pydantic import BaseModel

class Feedback(BaseModel):
    feedback_by:str
    feedback_to:str
    feedback_discription:str
    date:datetime
    media:str
