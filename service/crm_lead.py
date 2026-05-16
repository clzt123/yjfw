# 意向客户表 Service 业务逻辑层
# 透传 DAO 调用，不做复杂业务逻辑

from sqlalchemy.orm import Session
from schemas.crm_lead import LeadCreate, LeadUpdate, LeadOut
from dao.crm_lead import lead_create, lead_update, lead_delete


def service_lead_create(db: Session, lead: LeadCreate):
    """创建意向客户"""
    return lead_create(db, lead)


def service_lead_update(db: Session, lead: LeadUpdate):
    """更新意向客户"""
    return lead_update(db, lead)


def service_lead_delete(db: Session, lead_id: int):
    """删除意向客户"""
    return lead_delete(db, lead_id)