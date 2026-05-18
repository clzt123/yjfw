# student_admin_service 表 ORM 模型
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from core.database import Base


class StudentAdminService(Base):
    __tablename__ = 'student_admin_service'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, nullable=False, comment='学生ID')
    service_type = Column(String(100), nullable=False, comment='服务类型')
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    reason = Column(String(100), nullable=True)
    status = Column(String(100), nullable=False, server_default='待审批', comment='处理进度')
    approver_id = Column(Integer, nullable=True)
    related_academic_id = Column(Integer, nullable=True)
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now())