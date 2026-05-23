# student_psych_alert 表 Pydantic 模型
from pydantic import BaseModel
from typing import Optional


class PsychAlertCreate(BaseModel):
    """创建心理预警请求体"""
    student_id: int
    trigger_reason: str
    risk_level: str
    status: Optional[str] = '未处理'
    teacher_id: Optional[int] = None

    class Config:
        extra = 'ignore'


class PsychAlertOut(BaseModel):
    """心理预警响应体"""
    id: int
    student_id: int
    trigger_reason: str
    risk_level: str
    status: str
    teacher_id: Optional[int] = None

    class Config:
        from_attributes = True
