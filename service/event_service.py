from sqlalchemy.orm import Session
from dao import event_lecture_dao, event_registration_dao
from schema.event_schemas import (
    EventLectureResponse,
    EventRegistrationCreate,
    EventRegistrationResponse
)
from fastapi import HTTPException
from typing import List


def get_available_events(db: Session) -> List[EventLectureResponse]:
    """
    获取所有可报名的活动讲座服务

    从数据库获取所有活动讲座信息，并转换为响应格式返回

    Args:
        db: 数据库会话

    Returns:
        所有活动讲座的响应列表
    """
    events = event_lecture_dao.get_available_events(db)
    return [EventLectureResponse.model_validate(event) for event in events]


def register_event(
    db: Session,
    registration: EventRegistrationCreate
) -> EventRegistrationResponse:
    """
    活动报名服务

    1. 校验活动是否存在
    2. 校验活动是否还有名额
    3. 增加活动的已报名人数
    4. 创建报名记录
    5. 提交事务并返回报名结果

    Args:
        db: 数据库会话
        registration: 报名信息

    Returns:
        报名成功后的报名记录响应

    Raises:
        HTTPException: 活动不存在（404）或名额已满（400）
    """
    event = event_lecture_dao.get_event_by_id(db, registration.event_id)
    if not event:
        raise HTTPException(status_code=404, detail="活动不存在")
    if event.current_participants >= event.max_participants:
        raise HTTPException(status_code=400, detail="活动名额已满")

    event_lecture_dao.increase_participants(db, registration.event_id)
    db_registration = event_registration_dao.create_registration(db, registration)
    db.commit()
    db.refresh(db_registration)
    return EventRegistrationResponse.model_validate(db_registration)
