
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


@router.get(
    "/resolve",
    summary="根据用户ID获取用户信息",
    description="根据sys.user_id获取用户的数据库信息和类型，供Dify工作流自动绑定学生ID",
    operation_id="解析用户ID"
)
def resolve_user(user_id: int, db: Session = Depends(get_db)):
    """
    根据用户ID解析用户信息

    供 Dify 工作流在学生智能助手中自动获取登录用户的数据库 ID，
    避免每次对话都需要手动输入学生ID

    Args:
        user_id: 用户数据库ID（由前端从登录响应中获取并传递给Dify的sys.user_id）
        db: 数据库依赖注入

    Returns:
        dict: 包含用户基本信息

    Example:
        GET /api/v1/user/resolve?user_id=5
    """
    from dao.sys_user_dao import get_user_by_id
    user = get_user_by_id(db, user_id)
    if not user:
        return {"code": 404, "message": "用户不存在"}
    return {
        "code": 200,
        "data": {
            "id": user.id,
            "username": user.username,
            "user_type": user.user_type,
            "real_name": user.real_name
        }
    }


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
