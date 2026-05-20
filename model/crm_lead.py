# 意向客户表 ORM 模型
# 对应数据库表: crm_lead

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from core.database import Base


class CrmLead(Base):
    __tablename__ = "crm_lead"

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    customer_name = Column(String(255), nullable=False, comment='客户姓名')
    contact_info = Column(Text, comment='联系方式')
    background_info = Column(Text, comment='背景信息')
    follow_up_history = Column(Text, comment='跟进历史')
    status = Column(String(50), server_default="新增意向", comment='状态（新增意向/跟进中/已成交/已流失）')
    owner_employee_id = Column(Integer, nullable=False, comment='负责人ID')
    create_time = Column(DateTime, server_default=func.now(), comment='创建时间')
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')