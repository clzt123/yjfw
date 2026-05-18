# student_admin_service 表 DAO 数据访问层
from sqlalchemy.orm import Session
from model.student_models import StudentAdminService


def student_admin_service_create(db: Session, service) -> StudentAdminService:
    """
    创建学生服务记录
    :param db: 数据库会话
    :param service: 创建请求对象，必须包含 student_id 和 service_type
    :return: 创建后的记录
    """
    db_service = StudentAdminService(
        student_id=service.student_id,
        service_type=service.service_type,
        start_time=service.start_time,
        end_time=service.end_time,
        reason=service.reason,
        status=service.status or '待审批',
        approver_id=service.approver_id,
        related_academic_id=service.related_academic_id
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


def student_admin_service_update(db: Session, service) -> StudentAdminService:
    """
    更新学生服务记录
    :param db: 数据库会话
    :param service: 更新请求对象
    :return: 更新后的记录
    """
    db_service = db.query(StudentAdminService).filter(StudentAdminService.id == service.id).first()
    if not db_service:
        return None
    
    update_data = service.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_service, key, value)
    
    db.commit()
    db.refresh(db_service)
    return db_service