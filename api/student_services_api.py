# student_admin_service 表 API 路由层
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schema.student_admin_service import StudentServiceCreate, StudentServiceUpdate, StudentServiceUpdateById, StudentServiceOut
from service.student_admin_service_service import service_student_admin_service_create, service_student_admin_service_update

router = APIRouter()


@router.post(
    "/student-services",
    response_model=StudentServiceOut,
    summary="创建学生服务记录",
    description="创建新的学生服务申请记录（如休学、复学等）",
    operation_id="创建学生服务记录"
)
def create_student_service(service: StudentServiceCreate, db: Session = Depends(get_db)):
    """创建学生服务记录
    
    Args:
        service: 学生服务创建请求
        db: 数据库依赖注入
    
    Returns:
        StudentServiceOut: 创建成功的学生服务记录
    """
    return service_student_admin_service_create(db, service)


@router.put(
    "/student-services/{id}",
    response_model=StudentServiceOut,
    summary="更新学生服务记录",
    description="根据ID更新学生服务记录",
    operation_id="更新学生服务记录"
)
def update_student_service(id: int, service: StudentServiceUpdate, db: Session = Depends(get_db)):
    """根据ID更新学生服务记录
    
    Args:
        id: 记录ID
        service: 更新数据
        db: 数据库依赖注入
    
    Returns:
        StudentServiceOut: 更新后的学生服务记录
    """
    service.id = id
    return service_student_admin_service_update(db, service)


@router.post(
    "/student-services/update",
    response_model=StudentServiceOut,
    summary="更新学生服务记录（Dify专用）",
    description="通过请求体传id更新学生服务记录，方便Dify调用",
    operation_id="更新学生服务记录ById"
)
def update_student_service_by_id(service: StudentServiceUpdateById, db: Session = Depends(get_db)):
    """通过请求体传id更新学生服务记录
    
    Args:
        service: 包含id的更新请求（方便Dify调用）
        db: 数据库依赖注入
    
    Returns:
        StudentServiceOut: 更新后的学生服务记录
    """
    return service_student_admin_service_update(db, service)