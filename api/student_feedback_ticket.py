# 投诉反馈工单表 API 路由层
# RESTful 风格接口定义

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.config import get_db
from schemas.student_feedback_ticket import FeedbackCreate, FeedbackUpdate, FeedbackUpdateById, FeedbackOut
from service.student_feedback_ticket import service_feedback_create, service_feedback_update, service_feedback_delete

router = APIRouter()


@router.post("/api/feedbacks", response_model=FeedbackOut)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    """创建投诉反馈"""
    return service_feedback_create(db, feedback)


# @router.put("/api/feedbacks/{id}", response_model=FeedbackOut)
# def update_feedback(id: int, feedback: FeedbackUpdate, db: Session = Depends(get_db)):
#     """根据ID更新投诉反馈"""
#     feedback.id = id
#     return service_feedback_update(db, feedback)


# @router.delete("/api/feedbacks/{id}", response_model=FeedbackOut)
# def delete_feedback(id: int, db: Session = Depends(get_db)):
#     """根据ID删除投诉反馈"""
#     return service_feedback_delete(db, id)


@router.post("/api/feedbacks/update", response_model=FeedbackOut)
def update_feedback_by_id(feedback: FeedbackUpdateById, db: Session = Depends(get_db)):
    """通过请求体传id更新投诉反馈（方便Dify调用）"""
    return service_feedback_update(db, feedback)