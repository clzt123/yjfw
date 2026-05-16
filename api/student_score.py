# 学生成绩表 API 路由层
# RESTful 风格接口定义

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.config import get_db
from schemas.student_score import ScoreCreate, ScoreUpdate, ScoreOut
from service.student_score import service_score_create, service_score_update, service_score_delete

router = APIRouter()


@router.post("/api/scores", response_model=ScoreOut)
def create_score(score: ScoreCreate, db: Session = Depends(get_db)):
    """创建学生成绩"""
    return service_score_create(db, score)


# @router.put("/api/scores/{id}", response_model=ScoreOut)
# def update_score(id: int, score: ScoreUpdate, db: Session = Depends(get_db)):
#     """根据ID更新学生成绩"""
#     score.id = id
#     return service_score_update(db, score)


# @router.delete("/api/scores/{id}", response_model=ScoreOut)
# def delete_score(id: int, db: Session = Depends(get_db)):
#     """根据ID删除学生成绩"""
#     return service_score_delete(db, id)