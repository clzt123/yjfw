# student_admin_service 表 业务逻辑层
from sqlalchemy.orm import Session
from dao.student_admin_service_dao import student_admin_service_create, student_admin_service_update


def service_student_admin_service_create(db: Session, service) -> dict:
    """
    服务层：创建学生服务记录
    :param db: 数据库会话
    :param service: 创建请求对象
    :return: 创建后的记录
    """
    return student_admin_service_create(db, service)


def service_student_admin_service_update(db: Session, service) -> dict:
    """
    服务层：更新学生服务记录
    :param db: 数据库会话
    :param service: 更新请求对象
    :return: 更新后的记录
    """
    return student_admin_service_update(db, service)