# 意向客户表 ORM 模型
# 对应数据库表: crm_lead

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from core.database import Base


class CrmLead(Base):
    __tablename__ = "crm_lead"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(255), nullable=False)
    contact_info = Column(Text)
    background_info = Column(Text)
    follow_up_history = Column(Text)
    status = Column(String(50), server_default="新增意向")
    owner_employee_id = Column(Integer, nullable=False)
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now())