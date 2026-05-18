from pydantic import BaseModel
from typing import Optional


class CourseProjectResponse(BaseModel):
    """
    课程项目响应模型

    用于返回课程项目的完整信息

    Attributes:
        id: 项目ID
        project_name: 项目/课程名称
        category: 类别（如：语言培训、背景提升、硕博连读）
        target_education: 适合学历
        duration: 学制时长
        tuition_fee: 学费
        project_advantage: 项目优势
        application_condition: 申请条件
        target_country: 目标国家
        target_major: 意向专业
        status: 招生状态
    """
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
