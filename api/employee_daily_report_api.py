# 员工日报表 API 路由层
# RESTful 风格接口定义

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schema.employee_daily_report import DailyReportCreate, DailyReportUpdate, DailyReportOut
from service.employee_daily_report import service_daily_report_create, service_daily_report_update, service_daily_report_delete

router = APIRouter()


@router.post(
    "/daily-reports",
    response_model=DailyReportOut,
    summary="创建员工日报",
    description="创建新的员工日报记录",
    operation_id="创建员工日报"
)
def create_daily_report(report: DailyReportCreate, db: Session = Depends(get_db)):
    """创建员工日报记录
    
    Args:
        report: 日报创建请求
        db: 数据库依赖注入
    
    Returns:
        DailyReportOut: 创建成功的员工日报记录
    """
    return service_daily_report_create(db, report)


# @router.put("/daily-reports/{id}", response_model=DailyReportOut)
# def update_daily_report(id: int, report: DailyReportUpdate, db: Session = Depends(get_db)):
#     """根据ID更新员工日报"""
#     report.id = id
#     return service_daily_report_update(db, report)


# @router.delete("/daily-reports/{id}", response_model=DailyReportOut)
# def delete_daily_report(id: int, db: Session = Depends(get_db)):
#     """根据ID删除员工日报"""
#     return service_daily_report_delete(db, id)