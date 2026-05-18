from sqlalchemy.orm import Session
from dao import course_project_dao
from schema.course_schemas import CourseProjectResponse
from typing import List, Optional


def recommend_courses(
    db: Session,
    target_education: Optional[str] = None,
    target_country: Optional[str] = None,
    target_major: Optional[str] = None
) -> List[CourseProjectResponse]:
    """
    智能推荐课程项目服务

    根据用户提供的条件（学历、国家、专业）进行模糊匹配查询，返回符合条件的课程项目列表

    Args:
        db: 数据库会话
        target_education: 适合学历
        target_country: 目标国家
        target_major: 意向专业

    Returns:
        符合条件的课程项目响应列表
    """
    courses = course_project_dao.get_course_by_filter(
        db, target_education, target_country, target_major
    )
    return [CourseProjectResponse.model_validate(course) for course in courses]
