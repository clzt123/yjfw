# 员工日报表 DAO 数据访问层
# 实现数据库的增删改操作

from sqlalchemy.orm import Session
from model.employee_daily_report import EmployeeDailyReport
from schema.employee_daily_report import DailyReportCreate, DailyReportUpdate


def daily_report_create(db: Session, report: DailyReportCreate):
    """创建新的员工日报记录"""
    db_report = EmployeeDailyReport(
        employee_id=report.employee_id,
        report_date=report.report_date,
        content=report.content
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


def daily_report_update(db: Session, report: DailyReportUpdate):
    """根据ID更新员工日报记录"""
    db_report = db.query(EmployeeDailyReport).filter(EmployeeDailyReport.id == report.id).first()
    if db_report:
        if report.employee_id is not None:
            db_report.employee_id = report.employee_id
        if report.report_date is not None:
            db_report.report_date = report.report_date
        if report.content is not None:
            db_report.content = report.content
        db.commit()
        db.refresh(db_report)
    return db_report


def daily_report_delete(db: Session, report_id: int):
    """根据ID删除员工日报记录"""
    db_report = db.query(EmployeeDailyReport).filter(EmployeeDailyReport.id == report_id).first()
    if db_report:
        db.delete(db_report)
        db.commit()
    return db_report