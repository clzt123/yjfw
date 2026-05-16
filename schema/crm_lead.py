# 意向客户表 Pydantic 模型
# 用于请求体验证和响应序列化

from pydantic import BaseModel
from typing import Optional


class LeadCreate(BaseModel):
    """创建意向客户请求体"""
    customer_name: str
    owner_employee_id: int
    contact_info: Optional[str] = None
    background_info: Optional[str] = None
    follow_up_history: Optional[str] = None
    status: Optional[str] = None

    class Config:
        extra = 'ignore'


class LeadUpdate(BaseModel):
    """更新意向客户请求体（通过URL传id）"""
    id: Optional[int] = None
    customer_name: Optional[str] = None
    contact_info: Optional[str] = None
    background_info: Optional[str] = None
    follow_up_history: Optional[str] = None
    status: Optional[str] = None
    owner_employee_id: Optional[int] = None

    class Config:
        extra = 'ignore'


class LeadUpdateById(BaseModel):
    """更新意向客户请求体（通过请求体传id，方便Dify调用）"""
    id: int
    customer_name: Optional[str] = None
    contact_info: Optional[str] = None
    background_info: Optional[str] = None
    follow_up_history: Optional[str] = None
    status: Optional[str] = None
    owner_employee_id: Optional[int] = None

    class Config:
        extra = 'ignore'


class LeadOut(BaseModel):
    """意向客户响应体"""
    id: int
    customer_name: str
    contact_info: Optional[str] = None
    background_info: Optional[str] = None
    follow_up_history: Optional[str] = None
    status: str
    owner_employee_id: int

    class Config:
        from_attributes = True