
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.user_schema import LoginRequest, LoginResponse
from service.user_service import login_service
from core.database import get_db

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    用户登录接口
    """
    return login_service(db, request.username, request.password)


@router.get("/health")
def health():
    """
    健康检查接口
    """
    return {"status": "ok"}
