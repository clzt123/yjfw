# 投诉反馈工单表 Service 业务逻辑层
# 透传 DAO 调用，不做复杂业务逻辑

from sqlalchemy.orm import Session
from schema.student_feedback_ticket import FeedbackCreate, FeedbackUpdate, FeedbackOut
from dao.student_feedback_ticket import feedback_create, feedback_update, feedback_delete


def service_feedback_create(db: Session, feedback: FeedbackCreate):
    """创建投诉反馈"""
    return feedback_create(db, feedback)


def service_feedback_update(db: Session, feedback: FeedbackUpdate):
    """更新投诉反馈"""
    return feedback_update(db, feedback)


def service_feedback_delete(db: Session, feedback_id: int):
    """删除投诉反馈"""
    return feedback_delete(db, feedback_id)