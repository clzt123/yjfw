
from sqlalchemy.orm import Session
from dao.sys_user_dao import get_user_by_username
from schema.user_schema import LoginResponse
import bcrypt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证密码是否匹配
    
    Args:
        plain_password: 用户输入的明文密码
        hashed_password: 数据库中存储的加密密码
        
    Returns:
        bool: 密码是否匹配
    """
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception:
        return False


def login_service(db: Session, username: str, password: str) -> LoginResponse:
    """
    用户登录服务
    """
    # 根据用户名查询用户
    user = get_user_by_username(db, username)
    
    if not user:
        return LoginResponse(
            success=False,
            message="用户名或密码错误"
        )
    
    # 检查账号状态
    if user.status != '正常':
        return LoginResponse(
            success=False,
            message="账号状态异常，请联系管理员"
        )
    
    # 验证密码（使用 bcrypt 进行加密验证）
    if not verify_password(password, user.password):
        return LoginResponse(
            success=False,
            message="用户名或密码错误"
        )
    
    # 登录成功，返回用户信息
    return LoginResponse(
        success=True,
        message="登录成功",
        id=user.id,
        username=user.username,
        real_name=user.real_name,
        user_type=user.user_type,
        employee_role=user.employee_role,
        department=user.department
    )
