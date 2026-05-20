# 学生成绩表 API 路由层
# RESTful 风格接口定义

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schema.student_score import ScoreCreate, ScoreUpdate, ScoreOut
from service.student_score import service_score_create, service_score_update, service_score_delete

router = APIRouter()


@router.post(
    "/scores",
    response_model=ScoreOut,
    summary="创建学生成绩",
    description="创建新的学生成绩记录",
    operation_id="创建学生成绩"
)
def create_score(score: ScoreCreate, db: Session = Depends(get_db)):
    """创建学生成绩记录
    
    Args:
        score: 成绩创建请求
        db: 数据库依赖注入
    
    Returns:
        ScoreOut: 创建成功的成绩记录
    """
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