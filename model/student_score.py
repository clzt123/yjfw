# 学生成绩表 ORM 模型
# 对应数据库表: student_score

from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.sql import func
from core.config import Base


class StudentScore(Base):
    __tablename__ = "student_score"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, nullable=False)
    course_name = Column(String(255), nullable=False)
    score = Column(DECIMAL(5, 2), nullable=False)
    semester = Column(String(100))
    create_time = Column(DateTime, server_default=func.now())