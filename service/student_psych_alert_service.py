# student_psych_alert 表 业务逻辑层
from sqlalchemy.orm import Session
from dao.student_psych_alert import psych_alert_create


def service_psych_alert_create(db: Session, alert):
    """服务层：创建心理预警记录"""
    return psych_alert_create(db, alert)
