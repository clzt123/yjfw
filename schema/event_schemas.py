from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class EventLectureResponse(BaseModel):
    id: int
    event_name: str
    event_type: str
    start_time: datetime
    location: str
    max_participants: int
    current_participants: int

    class Config:
        from_attributes = True


class EventRegistrationCreate(BaseModel):
    event_id: int
    customer_name: str
    phone: str
    email: Optional[EmailStr] = None
    remark: Optional[str] = None


class EventRegistrationResponse(BaseModel):
    id: int
    event_id: int
    customer_name: str
    phone: str
    email: Optional[str]
    status: str
    create_time: datetime

    class Config:
        from_attributes = True
