# student_admin_service 表 Pydantic 模型
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class StudentServiceCreate(BaseModel):
    """创建学生服务请求体"""
    student_id: int
    service_type: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    reason: Optional[str] = None
    status: Optional[str] = '待审批'
    approver_id: Optional[int] = None
    related_academic_id: Optional[int] = None

    class Config:
        extra = 'ignore'


class StudentServiceUpdate(BaseModel):
    """更新学生服务请求体（通过URL传id）"""
    id: Optional[int] = None
    student_id: Optional[int] = None
    service_type: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    reason: Optional[str] = None
    status: Optional[str] = None
    approver_id: Optional[int] = None
    related_academic_id: Optional[int] = None

    class Config:
        extra = 'ignore'


class StudentServiceUpdateById(BaseModel):
    """更新学生服务请求体（通过请求体传id，方便Dify调用）"""
    id: int
    student_id: Optional[int] = None
    service_type: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    reason: Optional[str] = None
    status: Optional[str] = None
    approver_id: Optional[int] = None
    related_academic_id: Optional[int] = None

    class Config:
        extra = 'ignore'


class StudentServiceOut(BaseModel):
    """学生服务响应体"""
    id: int
    student_id: int
    service_type: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    reason: Optional[str] = None
    status: str
    approver_id: Optional[int] = None
    related_academic_id: Optional[int] = None

    class Config:
        from_attributes = True