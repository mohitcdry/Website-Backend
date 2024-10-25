from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Attendance(BaseModel):
    student_id: Optional[str]
    date: datetime
    status: bool
    