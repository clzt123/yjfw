
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.user_schema import LoginRequest, LoginResponse
from service.user_service import login_service
from core.database import get_db

router = APIRouter()


@router.post(
    "/login",
    response_model=LoginResponse,
    summary="用户登录",
    description="用户登录接口，验证用户名和密码",
    operation_id="用户登录"
)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    用户登录接口

    Args:
        request: 登录请求，包含用户名和密码
        db: 数据库依赖注入

    Returns:
        LoginResponse: 登录结果响应

    Example:
        POST /api/v1/user/login
        {
            "username": "admin",
            "password": "password"
        }
    """
    return login_service(db, request.username, request.password)


@router.get("/health", summary="健康检查", description="验证服务是否正常运行", operation_id="健康检查")
def health():
    """
    健康检查接口

    Returns:
        dict: 服务状态信息

    Example:
        GET /api/v1/user/health
    """
    return {"status": "ok"}
