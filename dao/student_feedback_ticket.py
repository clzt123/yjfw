# 投诉反馈工单表 DAO 数据访问层
# 实现数据库的增删改操作

from sqlalchemy.orm import Session
from model.student_models import StudentFeedbackTicket
from schema.student_feedback_ticket import FeedbackCreate, FeedbackUpdate


def feedback_create(db: Session, feedback: FeedbackCreate):
    """创建新的投诉反馈记录"""
    db_feedback = StudentFeedbackTicket(
        student_id=feedback.student_id,
        content=feedback.content,
        detail=feedback.detail
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


def feedback_update(db: Session, feedback: FeedbackUpdate):
    """根据ID更新投诉反馈记录"""
    db_feedback = db.query(StudentFeedbackTicket).filter(StudentFeedbackTicket.id == feedback.id).first()
    if db_feedback:
        if feedback.student_id is not None:
            db_feedback.student_id = feedback.student_id
        if feedback.content is not None:
            db_feedback.content = feedback.content
        if feedback.detail is not None:
            db_feedback.detail = feedback.detail
        if feedback.status is not None:
            db_feedback.status = feedback.status
        if feedback.solution is not None:
            db_feedback.solution = feedback.solution
        if feedback.is_notified is not None:
            db_feedback.is_notified = feedback.is_notified
        db.commit()
        db.refresh(db_feedback)
    return db_feedback


def feedback_delete(db: Session, feedback_id: int):
    """根据ID删除投诉反馈记录"""
    db_feedback = db.query(StudentFeedbackTicket).filter(StudentFeedbackTicket.id == feedback_id).first()
    if db_feedback:
        db.delete(db_feedback)
        db.commit()
    return db_feedback