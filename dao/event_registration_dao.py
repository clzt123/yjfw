from sqlalchemy.orm import Session
from model.models import EventRegistration
from schema.event_schemas import EventRegistrationCreate
from typing import Optional


def create_registration(
    db: Session,
    registration: EventRegistrationCreate
) -> EventRegistration:
    """
    创建活动报名记录

    Args:
        db: 数据库会话
        registration: 报名信息（包含event_id, customer_name, phone等）

    Returns:
        创建的报名记录对象
    """
    db_registration = EventRegistration(**registration.model_dump())
    db.add(db_registration)
    return db_registration


def get_registration_by_id(
    db: Session,
    registration_id: int
) -> Optional[EventRegistration]:
    """
    根据报名ID获取报名记录

    Args:
        db: 数据库会话
        registration_id: 报名记录ID

    Returns:
        报名记录对象，如果不存在则返回None
    """
    return db.query(EventRegistration).filter(EventRegistration.id == registration_id).first()


def get_registrations_by_event_id(
    db: Session,
    event_id: int
) -> list:
    """
    根据活动ID获取该活动的所有报名记录

    Args:
        db: 数据库会话
        event_id: 活动ID

    Returns:
        该活动的所有报名记录列表
    """
    return db.query(EventRegistration).filter(EventRegistration.event_id == event_id).all()
