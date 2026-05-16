# 学生成绩表 Pydantic 模型
# 用于请求体验证和响应序列化

from pydantic import BaseModel
from typing import Optional


class ScoreCreate(BaseModel):
    """创建学生成绩请求体"""
    student_id: int
    course_name: str
    score: float
    semester: Optional[str] = None

    class Config:
        extra = 'ignore'


class ScoreUpdate(BaseModel):
    """更新学生成绩请求体"""
    id: Optional[int] = None
    student_id: Optional[int] = None
    course_name: Optional[str] = None
    score: Optional[float] = None
    semester: Optional[str] = None

    class Config:
        extra = 'ignore'


class ScoreOut(BaseModel):
    """学生成绩响应体"""
    id: int
    student_id: int
    course_name: str
    score: float
    semester: Optional[str] = None

    class Config:
        from_attributes = True