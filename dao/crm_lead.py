# 意向客户表 DAO 数据访问层
# 实现数据库的增删改操作

from sqlalchemy.orm import Session
from model.crm_lead import CrmLead
from schemas.crm_lead import LeadCreate, LeadUpdate


def lead_create(db: Session, lead: LeadCreate):
    """创建新的意向客户记录"""
    db_lead = CrmLead(
        customer_name=lead.customer_name,
        contact_info=lead.contact_info,
        background_info=lead.background_info,
        follow_up_history=lead.follow_up_history,
        status=lead.status,
        owner_employee_id=lead.owner_employee_id
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead


def lead_update(db: Session, lead: LeadUpdate):
    """根据ID更新意向客户记录"""
    db_lead = db.query(CrmLead).filter(CrmLead.id == lead.id).first()
    if db_lead:
        if lead.customer_name is not None:
            db_lead.customer_name = lead.customer_name
        if lead.contact_info is not None:
            db_lead.contact_info = lead.contact_info
        if lead.background_info is not None:
            db_lead.background_info = lead.background_info
        if lead.follow_up_history is not None:
            db_lead.follow_up_history = lead.follow_up_history
        if lead.status is not None:
            db_lead.status = lead.status
        if lead.owner_employee_id is not None:
            db_lead.owner_employee_id = lead.owner_employee_id
        db.commit()
        db.refresh(db_lead)
    return db_lead


def lead_delete(db: Session, lead_id: int):
    """根据ID删除意向客户记录"""
    db_lead = db.query(CrmLead).filter(CrmLead.id == lead_id).first()
    if db_lead:
        db.delete(db_lead)
        db.commit()
    return db_lead