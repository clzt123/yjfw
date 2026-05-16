# student_admin_service 表 API 路由层
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.config import get_db
from schemas.student_admin_service import StudentServiceCreate, StudentServiceUpdate, StudentServiceUpdateById, StudentServiceOut
from service.student_admin_service_service import service_student_admin_service_create, service_student_admin_service_update

router = APIRouter()


@router.post("/api/student-services", response_model=StudentServiceOut)
def create_student_service(service: StudentServiceCreate, db: Session = Depends(get_db)):
    """创建学生服务记录"""
    return service_student_admin_service_create(db, service)


@router.put("/api/student-services/{id}", response_model=StudentServiceOut)
def update_student_service(id: int, service: StudentServiceUpdate, db: Session = Depends(get_db)):
    """根据ID更新学生服务记录"""
    service.id = id
    return service_student_admin_service_update(db, service)


@router.post("/api/student-services/update", response_model=StudentServiceOut)
def update_student_service_by_id(service: StudentServiceUpdateById, db: Session = Depends(get_db)):
    """通过请求体传id更新学生服务记录（方便Dify调用）"""
    return service_student_admin_service_update(db, service)