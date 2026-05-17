
from sqlalchemy.orm import Session
from model.sys_user import SysUser


def get_user_by_username(db: Session, username: str):
    """
    根据用户名查询用户
    """
    return db.query(SysUser).filter(SysUser.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    """
    根据用户ID查询用户
    """
    return db.query(SysUser).filter(SysUser.id == user_id).first()


def create_user(db: Session, user_data: dict):
    """
    创建新用户
    """
    user = SysUser(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
