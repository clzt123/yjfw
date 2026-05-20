# 员工日报表 ORM 模型
# 对应数据库表: employee_daily_report

from sqlalchemy import Column, Integer, String, Text, Date, DateTime
from sqlalchemy.sql import func
from core.database import Base


class EmployeeDailyReport(Base):
    __tablename__ = "employee_daily_report"

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    employee_id = Column(Integer, nullable=False, comment='员工ID')
    report_date = Column(Date, nullable=False, comment='汇报日期')
    content = Column(Text, nullable=False, comment='日报内容')
    create_time = Column(DateTime, server_default=func.now(), comment='创建时间')