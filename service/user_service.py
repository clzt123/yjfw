
from sqlalchemy.orm import Session
from dao.sys_user_dao import get_user_by_username
from schema.user_schema import LoginResponse


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
    
    # 验证密码（明文验证，实际项目中应使用加密密码）
    if user.password != password:
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
