from sqlalchemy.orm import Session
from model.models import CourseProject
from typing import List, Optional


def get_course_by_filter(
    db: Session,
    target_education: Optional[str] = None,
    target_country: Optional[str] = None,
    target_major: Optional[str] = None
) -> List[CourseProject]:
    """
    根据条件模糊查询课程项目

    Args:
        db: 数据库会话
        target_education: 适合学历（模糊匹配）
        target_country: 目标国家（模糊匹配）
        target_major: 意向专业（模糊匹配）

    Returns:
        符合条件的课程项目列表
    """
    query = db.query(CourseProject)
    if target_education:
        query = query.filter(CourseProject.target_education.like(f"%{target_education}%"))
    if target_country:
        query = query.filter(CourseProject.target_country.like(f"%{target_country}%"))
    if target_major:
        query = query.filter(CourseProject.target_major.like(f"%{target_major}%"))
    return query.all()
