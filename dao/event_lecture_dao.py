from sqlalchemy.orm import Session
from model.models import EventLecture
from typing import List, Optional


def get_available_events(db: Session) -> List[EventLecture]:
    """
    获取所有可报名的活动讲座

    Args:
        db: 数据库会话

    Returns:
        所有活动讲座列表
    """
    return db.query(EventLecture).all()


def get_event_by_id(db: Session, event_id: int) -> Optional[EventLecture]:
    """
    根据活动ID获取活动详情

    Args:
        db: 数据库会话
        event_id: 活动ID

    Returns:
        活动对象，如果不存在则返回None
    """
    return db.query(EventLecture).filter(EventLecture.id == event_id).first()


def increase_participants(db: Session, event_id: int) -> bool:
    """
    增加活动的已报名人数

    Args:
        db: 数据库会话
        event_id: 活动ID

    Returns:
        是否成功增加（未满员时返回True，已满员或活动不存在时返回False）
    """
    event = get_event_by_id(db, event_id)
    if event and event.current_participants < event.max_participants:
        event.current_participants += 1
        return True
    return False
