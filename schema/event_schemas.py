from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class EventLectureResponse(BaseModel):
    """
    活动讲座响应模型

    用于返回活动讲座的完整信息

    Attributes:
        id: 活动ID
        event_name: 活动名称
        event_type: 活动类型（线上/线下）
        start_time: 开始时间
        location: 地点或会议链接
        max_participants: 最大报名人数
        current_participants: 当前已报名人数
    """
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
    """
    活动报名创建模型

    用于接收用户提交的报名信息

    Attributes:
        event_id: 活动ID（必填）
        customer_name: 客户姓名（必填）
        phone: 联系电话（必填）
        email: 邮箱（可选）
        remark: 备注信息（可选）
    """
    event_id: int
    customer_name: str
    phone: str
    email: Optional[EmailStr] = None
    remark: Optional[str] = None


class EventRegistrationResponse(BaseModel):
    """
    活动报名响应模型

    用于返回报名成功后的完整报名记录

    Attributes:
        id: 报名记录ID
        event_id: 活动ID
        customer_name: 客户姓名
        phone: 联系电话
        email: 邮箱（可选）
        status: 报名状态
        create_time: 报名时间
    """
    id: int
    event_id: int
    customer_name: str
    phone: str
    email: Optional[str] = None
    status: str
    create_time: datetime

    class Config:
        from_attributes = True
