from sqlalchemy import Column, Integer, String, DateTime, Text, Index
from datetime import datetime
from core.database import Base


class StudentAdminService(Base):
    __tablename__ = "student_admin_service"
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    student_id = Column(Integer, nullable=False, comment='学生ID')
    service_type = Column(String(100), nullable=False, comment='服务类型（如：休学申请、复学申请）')
    start_time = Column(DateTime, comment='开始时间')
    end_time = Column(DateTime, comment='结束时间')
    reason = Column(String(100), comment='申请原因')
    status = Column(String(100), default='待审批', comment='审批状态')
    approver_id = Column(Integer, comment='审批人ID')
    related_academic_id = Column(Integer, comment='相关学籍ID')
    create_time = Column(DateTime, default=datetime.now, comment='创建时间')
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')


class StudentPsychProfile(Base):
    __tablename__ = "student_psych_profile"
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    student_id = Column(Integer, nullable=False, unique=True, comment='学生ID')
    latest_emotion_tag = Column(String(100), comment='最新情绪标签')
    emotion_score = Column(Integer, comment='情绪评分')
    last_interaction_time = Column(DateTime, comment='最后互动时间')
    emotion_history = Column(String(100), comment='情绪历史记录')
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')


class StudentPsychAlert(Base):
    __tablename__ = "student_psych_alert"
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    student_id = Column(Integer, nullable=False, comment='学生ID')
    trigger_reason = Column(String(100), nullable=False, comment='触发原因')
    risk_level = Column(String(100), nullable=False, comment='风险等级（高/中/低）')
    status = Column(String(100), default='未处理', comment='处理状态')
    teacher_id = Column(Integer, comment='负责老师ID')
    create_time = Column(DateTime, default=datetime.now, comment='创建时间')


class StudentFeedbackTicket(Base):
    __tablename__ = "student_feedback_ticket"
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    student_id = Column(Integer, nullable=False, comment='学生ID')
    content = Column(String(100), nullable=False, comment='反馈内容')
    detail = Column(String(100), comment='详细描述')
    status = Column(String(100), default='待处理', comment='处理状态')
    solution = Column(String(100), comment='解决方案')
    is_notified = Column(Integer, default=0, comment='是否已通知（0未通知/1已通知）')
    create_time = Column(DateTime, default=datetime.now, comment='创建时间')
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')


class StudyAbroadProgress(Base):
    __tablename__ = "study_abroad_progress"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, nullable=False, comment='学生ID')
    service_stage = Column(String(50), nullable=False, comment='服务阶段（文书/申请/签证）')
    current_status = Column(String(100), nullable=False, comment='当前具体状态（如：初稿撰写中）')
    detail_info = Column(Text, comment='详细备注（如：文案老师正在润色PS第二段）')
    last_update_time = Column(DateTime, default=datetime.now, comment='最后更新时间')
    update_by = Column(Integer, comment='最后更新人（顾问ID）')


