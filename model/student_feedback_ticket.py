# 投诉反馈工单表 ORM 模型
# 对应数据库表: student_feedback_ticket

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from core.config import Base


class StudentFeedbackTicket(Base):
    __tablename__ = "student_feedback_ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, nullable=False)
    content = Column(String(100), nullable=False)
    detail = Column(String(100))
    status = Column(String(100), server_default="待处理")
    solution = Column(String(100))
    is_notified = Column(Integer, server_default="0")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now())