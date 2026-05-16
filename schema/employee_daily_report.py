# 员工日报表 Pydantic 模型
# 用于请求体验证和响应序列化

from pydantic import BaseModel
from typing import Optional
from datetime import date


class DailyReportCreate(BaseModel):
    """创建员工日报请求体"""
    employee_id: int
    report_date: date
    content: str

    class Config:
        extra = 'ignore'


class DailyReportUpdate(BaseModel):
    """更新员工日报请求体"""
    id: Optional[int] = None
    employee_id: Optional[int] = None
    report_date: Optional[date] = None
    content: Optional[str] = None

    class Config:
        extra = 'ignore'


class DailyReportOut(BaseModel):
    """员工日报响应体"""
    id: int
    employee_id: int
    report_date: date
    content: str

    class Config:
        from_attributes = True