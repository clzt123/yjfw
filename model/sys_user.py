
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from core.database import Base


class SysUser(Base):
    __tablename__ = 'sys_user'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    username = Column(String(64), nullable=False, unique=True, comment='用户名/登录账号')
    password = Column(String(255), nullable=False, comment='密码')
    real_name = Column(String(64), nullable=False, comment='真实姓名')
    user_type = Column(String(32), nullable=False, comment='用户大类（STUDENT/EMPLOYEE）')
    employee_role = Column(String(64), nullable=True, comment='员工角色')
    department = Column(String(128), nullable=True, comment='所属部门/院系')
    contact_info = Column(String(64), nullable=True, comment='联系方式')
    status = Column(String(16), default='正常', comment='账号状态')
    create_time = Column(DateTime, server_default=func.now(), comment='创建时间')
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')
