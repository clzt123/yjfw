# 学生成绩表 Service 业务逻辑层
# 透传 DAO 调用，不做复杂业务逻辑

from sqlalchemy.orm import Session
from schemas.student_score import ScoreCreate, ScoreUpdate, ScoreOut
from dao.student_score import score_create, score_update, score_delete


def service_score_create(db: Session, score: ScoreCreate):
    """创建学生成绩"""
    return score_create(db, score)


def service_score_update(db: Session, score: ScoreUpdate):
    """更新学生成绩"""
    return score_update(db, score)


def service_score_delete(db: Session, score_id: int):
    """删除学生成绩"""
    return score_delete(db, score_id)