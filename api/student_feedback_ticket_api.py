# 投诉反馈工单表 API 路由层
# RESTful 风格接口定义

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schema.student_feedback_ticket import FeedbackCreate, FeedbackUpdate, FeedbackUpdateById, FeedbackOut
from service.student_feedback_ticket import service_feedback_create, service_feedback_update, service_feedback_delete

router = APIRouter()


@router.post(
    "/feedbacks",
    response_model=FeedbackOut,
    summary="创建投诉反馈",
    description="创建新的学生投诉反馈工单",
    operation_id="创建投诉反馈"
)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    """创建投诉反馈工单
    
    Args:
        feedback: 反馈创建请求
        db: 数据库依赖注入
    
    Returns:
        FeedbackOut: 创建成功的反馈工单记录
    """
    return service_feedback_create(db, feedback)


# @router.put("/feedbacks/{id}", response_model=FeedbackOut)
# def update_feedback(id: int, feedback: FeedbackUpdate, db: Session = Depends(get_db)):
#     """根据ID更新投诉反馈"""
#     feedback.id = id
#     return service_feedback_update(db, feedback)


# @router.delete("/feedbacks/{id}", response_model=FeedbackOut)
# def delete_feedback(id: int, db: Session = Depends(get_db)):
#     """根据ID删除投诉反馈"""
#     return service_feedback_delete(db, id)


@router.post(
    "/feedbacks/update",
    response_model=FeedbackOut,
    summary="更新投诉反馈（Dify专用）",
    description="通过请求体传id更新投诉反馈记录，方便Dify调用",
    operation_id="更新投诉反馈ById"
)
def update_feedback_by_id(feedback: FeedbackUpdateById, db: Session = Depends(get_db)):
    """通过请求体传id更新投诉反馈记录
    
    Args:
        feedback: 包含id的更新请求（方便Dify调用）
        db: 数据库依赖注入
    
    Returns:
        FeedbackOut: 更新后的反馈工单记录
    """
    return service_feedback_update(db, feedback)