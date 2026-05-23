# 学生心理预警表 API 路由层
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schema.student_psych_alert import PsychAlertCreate, PsychAlertOut
from service.student_psych_alert_service import service_psych_alert_create

router = APIRouter()


@router.post(
    "/alerts",
    response_model=PsychAlertOut,
    summary="创建心理预警记录",
    description="创建新的学生心理预警记录（Dify调用）",
    operation_id="创建心理预警"
)
def create_psych_alert(alert: PsychAlertCreate, db: Session = Depends(get_db)):
    """创建心理预警记录"""
    return service_psych_alert_create(db, alert)
