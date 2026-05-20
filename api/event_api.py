
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from service import event_service
from schema.event_schemas import (
    EventLectureResponse,
    EventRegistrationCreate,
    EventRegistrationResponse
)
from typing import List


router = APIRouter()


@router.get(
    "/available",
    response_model=List[EventLectureResponse],
    summary="获取可报名的活动列表",
    description="返回所有活动的详细信息，包括已报名人数和最大报名人数",
    operation_id="获取可报名的活动列表"
)
def get_available_events(
    db: Session = Depends(get_db)
) -> List[EventLectureResponse]:
    """
    获取可报名的活动列表接口

    返回系统中所有活动的列表，包含活动名称、类型、时间、地点、
    最大报名人数和当前已报名人数等信息。

    Args:
        db: 数据库依赖注入

    Returns:
        所有活动讲座的列表

    Example:
        GET /api/event/available
    """
    return event_service.get_available_events(db)


@router.post(
    "/register",
    response_model=EventRegistrationResponse,
    summary="活动报名",
    description="用户报名参加指定活动，系统自动检查名额并更新已报名人数",
    operation_id="活动报名"
)
def register_event(
    registration: EventRegistrationCreate,
    db: Session = Depends(get_db)
) -> EventRegistrationResponse:
    """
    活动报名接口

    1. 检查活动是否存在
    2. 检查活动是否还有剩余名额
    3. 自动增加活动的已报名人数
    4. 创建报名记录

    Args:
        registration: 报名信息，包含：
            - event_id: 活动ID
            - customer_name: 客户姓名
            - phone: 联系电话
            - email: 邮箱（可选）
            - remark: 备注（可选）
        db: 数据库依赖注入

    Returns:
        报名成功后的报名记录响应

    Raises:
        HTTPException 404: 活动不存在
        HTTPException 400: 名额已满
        HTTPException 500: 报名失败（服务器内部错误）

    Example:
        POST /api/event/register
        {
            "event_id": 1,
            "customer_name": "张三",
            "phone": "13800138000",
            "email": "zhangsan@example.com"
        }
    """
    try:
        return event_service.register_event(db, registration)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"报名失败：{str(e)}")
