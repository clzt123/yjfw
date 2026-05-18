from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db
from service import course_service
from schema.course_schemas import CourseProjectResponse
from typing import List, Optional


router = APIRouter()


@router.get(
    "/recommend",
    response_model=List[CourseProjectResponse],
    summary="智能推荐课程项目",
    description="根据目标学历、国家和专业进行模糊匹配查询，返回符合条件的课程项目列表"
)
def recommend_courses(
    target_education: Optional[str] = Query(
        None,
        description="适合学历",
        example="本科"
    ),
    target_country: Optional[str] = Query(
        None,
        description="目标国家",
        example="美国"
    ),
    target_major: Optional[str] = Query(
        None,
        description="意向专业",
        example="计算机"
    ),
    db: Session = Depends(get_db)
) -> List[CourseProjectResponse]:
    """
    智能推荐课程项目接口

    支持根据学历、国家和专业进行多条件模糊匹配查询。
    所有参数均为可选，不传则返回全部课程项目。

    Args:
        target_education: 适合学历（如：本科、硕士、博士）
        target_country: 目标国家/地区
        target_major: 意向专业方向
        db: 数据库依赖注入

    Returns:
        符合条件的课程项目列表

    Example:
        GET /api/course/recommend?target_education=本科&target_country=美国
    """
    return course_service.recommend_courses(
        db, target_education, target_country, target_major
    )
