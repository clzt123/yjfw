# 意向客户表 API 路由层
# RESTful 风格接口定义

from fastapi import APIRouter, Depends, HTTPException
import json
from sqlalchemy.orm import Session
from core.config import get_db
from schemas.crm_lead import LeadCreate, LeadUpdate, LeadUpdateById, LeadOut
from service.crm_lead import service_lead_create, service_lead_update, service_lead_delete

router = APIRouter()


@router.post("/api/leads", response_model=LeadOut)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    """创建意向客户"""
    return service_lead_create(db, lead)


# @router.put("/api/leads/{id}", response_model=LeadOut)
# def update_lead(id: int, lead: LeadUpdate, db: Session = Depends(get_db)):
#     """根据ID更新意向客户"""
#     lead.id = id
#     return service_lead_update(db, lead)


# @router.delete("/api/leads/{id}", response_model=LeadOut)
# def delete_lead(id: int, db: Session = Depends(get_db)):
#     """根据ID删除意向客户"""
#     return service_lead_delete(db, id)


@router.post("/api/leads/update", response_model=LeadOut)
def update_lead_by_id(lead: LeadUpdateById, db: Session = Depends(get_db)):
    """通过请求体传id更新意向客户（方便Dify调用）"""
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