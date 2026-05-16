# 员工日报表 ORM 模型
# 对应数据库表: employee_daily_report

from sqlalchemy import Column, Integer, String, Text, Date, DateTime
from sqlalchemy.sql import func
from core.config import Base


class EmployeeDailyReport(Base):
    __tablename__ = "employee_daily_report"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, nullable=False)
    report_date = Column(Date, nullable=False)
    content = Column(Text, nullable=False)
    create_time = Column(DateTime, server_default=func.now())