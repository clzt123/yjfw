# student_psych_profile 表 业务逻辑层
from sqlalchemy.orm import Session
from dao.student_psych_profile import psych_profile_upsert


def service_psych_profile_upsert(db: Session, profile):
    """服务层：创建或更新心理画像记录"""
    return psych_profile_upsert(db, profile)
