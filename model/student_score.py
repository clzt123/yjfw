# 学生成绩表 ORM 模型
# 对应数据库表: student_score

from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.sql import func
from core.database import Base


class StudentScore(Base):
    __tablename__ = "student_score"

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    student_id = Column(Integer, nullable=False, comment='学生ID')
    course_name = Column(String(255), nullable=False, comment='课程名称')
    score = Column(DECIMAL(5, 2), nullable=False, comment='成绩')
    semester = Column(String(100), comment='学期')
    create_time = Column(DateTime, server_default=func.now(), comment='创建时间')