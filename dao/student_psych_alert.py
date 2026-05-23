# student_psych_alert 表 DAO 数据访问层
from sqlalchemy.orm import Session
from model.student_models import StudentPsychAlert


def psych_alert_create(db: Session, alert) -> StudentPsychAlert:
    """创建心理预警记录"""
    db_alert = StudentPsychAlert(
        student_id=alert.student_id,
        trigger_reason=alert.trigger_reason,
        risk_level=alert.risk_level,
        status=alert.status or '未处理',
        teacher_id=alert.teacher_id
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert
