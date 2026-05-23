# 学生心理画像表 API 路由层
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schema.student_psych_profile import PsychProfileUpdate, PsychProfileOut
from service.student_psych_profile_service import service_psych_profile_upsert

router = APIRouter()


@router.post(
    "/profile/update",
    response_model=PsychProfileOut,
    summary="创建或更新心理画像",
    description="按student_id创建或更新学生心理画像记录（Dify调用）",
    operation_id="更新心理画像"
)
def upsert_psych_profile(profile: PsychProfileUpdate, db: Session = Depends(get_db)):
    """创建或更新心理画像记录"""
    return service_psych_profile_upsert(db, profile)
