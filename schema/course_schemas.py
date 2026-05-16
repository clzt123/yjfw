from pydantic import BaseModel
from typing import Optional, List


class CourseProjectResponse(BaseModel):
    id: int
    project_name: str
    category: str
    target_education: str
    duration: str
    tuition_fee: str
    project_advantage: str
    application_condition: str
    target_country: str
    target_major: str
    status: str

    class Config:
        from_attributes = True
