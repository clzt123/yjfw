# 员工日报表 Service 业务逻辑层
# 透传 DAO 调用，不做复杂业务逻辑

from sqlalchemy.orm import Session
from schema.employee_daily_report import DailyReportCreate, DailyReportUpdate, DailyReportOut
from dao.employee_daily_report import daily_report_create, daily_report_update, daily_report_delete


def service_daily_report_create(db: Session, report: DailyReportCreate):
    """创建员工日报"""
    return daily_report_create(db, report)


def service_daily_report_update(db: Session, report: DailyReportUpdate):
    """更新员工日报"""
    return daily_report_update(db, report)


def service_daily_report_delete(db: Session, report_id: int):
    """删除员工日报"""
    return daily_report_delete(db, report_id)