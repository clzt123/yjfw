# 意向客户表 API 路由层
# RESTful 风格接口定义

from fastapi import APIRouter, Depends, HTTPException
import json
from sqlalchemy.orm import Session
from core.database import get_db
from schema.crm_lead import LeadCreate, LeadUpdate, LeadUpdateById, LeadOut
from service.crm_lead import service_lead_create, service_lead_update, service_lead_delete

router = APIRouter()


@router.post(
    "/leads",
    response_model=LeadOut,
    summary="创建意向客户",
    description="创建新的意向客户记录",
    operation_id="创建意向客户"
)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    """创建意向客户记录
    
    Args:
        lead: 意向客户创建请求
        db: 数据库依赖注入
    
    Returns:
        LeadOut: 创建成功的意向客户记录
    """
    return service_lead_create(db, lead)


# @router.put("/leads/{id}", response_model=LeadOut)
# def update_lead(id: int, lead: LeadUpdate, db: Session = Depends(get_db)):
#     """根据ID更新意向客户"""
#     lead.id = id
#     return service_lead_update(db, lead)


# @router.delete("/leads/{id}", response_model=LeadOut)
# def delete_lead(id: int, db: Session = Depends(get_db)):
#     """根据ID删除意向客户"""
#     return service_lead_delete(db, id)


@router.post(
    "/leads/update",
    response_model=LeadOut,
    summary="更新意向客户（Dify专用）",
    description="通过请求体传id更新意向客户记录，方便Dify调用",
    operation_id="更新意向客户ById"
)
def update_lead_by_id(lead: LeadUpdateById, db: Session = Depends(get_db)):
    """通过请求体传id更新意向客户记录
    
    Args:
        lead: 包含id的更新请求（方便Dify调用）
        db: 数据库依赖注入
    
    Returns:
        LeadOut: 更新后的意向客户记录
    """
    return service_lead_update(db, lead)


# @router.post("/api/leads/update/dify", response_model=LeadOut)
# def update_lead_for_dify(payload: dict, db: Session = Depends(get_db)):
#     """Dify专用：payload 格式 {"sql": "{\"id\":14,...}"}"""
#     try:
#         data = json.loads(payload["sql"])
#         lead = LeadUpdateById(**data)
#         return service_lead_update(db, lead)
#     except Exception as e:
#         raise HTTPException(status_code=422, detail=f"解析失败：{str(e)}")