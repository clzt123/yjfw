
from pydantic import BaseModel, Field
from typing import Optional


class LoginRequest(BaseModel):
    """
    登录请求模型
    """
    username: str = Field(..., description="用户名/登录账号")
    password: str = Field(..., description="密码")


class LoginResponse(BaseModel):
    """
    登录响应模型
    """
    success: bool
    message: str
    id: Optional[int] = None
    username: Optional[str] = None
    real_name: Optional[str] = None
    user_type: Optional[str] = None
    employee_role: Optional[str] = None
    department: Optional[str] = None
