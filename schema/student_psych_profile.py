# student_psych_profile 表 Pydantic 模型
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PsychProfileUpdate(BaseModel):
    """更新心理画像请求体（Dify专用，通过student_id定位）"""
    student_id: int
    latest_emotion_tag: Optional[str] = None
    emotion_score: Optional[int] = None
    last_interaction_time: Optional[datetime] = None
    emotion_history: Optional[str] = None

    class Config:
        extra = 'ignore'


class PsychProfileOut(BaseModel):
    """心理画像响应体"""
    id: int
    student_id: int
    latest_emotion_tag: Optional[str] = None
    emotion_score: Optional[int] = None
    last_interaction_time: Optional[datetime] = None
    emotion_history: Optional[str] = None

    class Config:
        from_attributes = True
