from pydantic import BaseModel

class Event(BaseModel):
    school_id:str ##school_id
    event_date:int
    event_title:str
    event_description:str
    created_by:str ##mentor_id
    