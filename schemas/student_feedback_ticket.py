# 投诉反馈工单表 Pydantic 模型
# 用于请求体验证和响应序列化

from pydantic import BaseModel
from typing import Optional


class FeedbackCreate(BaseModel):
    """创建投诉反馈请求体"""
    student_id: int
    content: str
    detail: Optional[str] = None

    class Config:
        extra = 'ignore'


class FeedbackUpdate(BaseModel):
    """更新投诉反馈请求体（通过URL传id）"""
    id: Optional[int] = None
    student_id: Optional[int] = None
    content: Optional[str] = None
    detail: Optional[str] = None
    status: Optional[str] = None
    solution: Optional[str] = None
    is_notified: Optional[int] = None

    class Config:
        extra = 'ignore'


class FeedbackUpdateById(BaseModel):
    """更新投诉反馈请求体（通过请求体传id，方便Dify调用）"""
    id: int
    student_id: Optional[int] = None
    content: Optional[str] = None
    detail: Optional[str] = None
    status: Optional[str] = None
    solution: Optional[str] = None
    is_notified: Optional[int] = None

    class Config:
        extra = 'ignore'


class FeedbackOut(BaseModel):
    """投诉反馈响应体"""
    id: int
    student_id: int
    content: str
    detail: Optional[str] = None
    status: str
    solution: Optional[str] = None
    is_notified: int

    class Config:
        from_attributes = True