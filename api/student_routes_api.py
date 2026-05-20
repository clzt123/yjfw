
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from service.student_service import BaseService
from schema.student_schemas import RawSQLRequest
from utils.sql_validator import validate_sql
from typing import Dict, Any, Optional

router = APIRouter()


@router.post(
    "/{table_name}/create",
    summary="创建记录",
    description="根据表名创建新记录",
    operation_id="创建记录"
)
def create_record(
    table_name: str,
    data: Dict[str, Any],
    db: Session = Depends(get_db)
):
    """
    创建记录接口

    Args:
        table_name: 表名
        data: 记录数据
        db: 数据库依赖注入

    Returns:
        dict: 创建结果

    Raises:
        HTTPException 400: 表不存在

    Example:
        POST /api/v1/student/{table_name}/create
    """
    service = BaseService(db)
    result = service.create(table_name, data)
    if result is None:
        raise HTTPException(status_code=400, detail=f"表 {table_name} 不存在")
    return {"status": "success", "data": result}


@router.put(
    "/{table_name}/update",
    summary="更新记录",
    description="根据 student_id 更新指定表的记录",
    operation_id="更新记录"
)
def update_record(
    table_name: str,
    data: Dict[str, Any],
    db: Session = Depends(get_db)
):
    """
    更新记录接口

    Args:
        table_name: 表名
        data: 更新数据（必须包含 student_id）
        db: 数据库依赖注入

    Returns:
        dict: 更新结果

    Raises:
        HTTPException 400: 必须提供 student_id
        HTTPException 404: 记录不存在

    Example:
        PUT /api/v1/student/{table_name}/update
    """
    student_id = data.get("student_id")
    if student_id is None:
        raise HTTPException(status_code=400, detail="必须提供 student_id")
    
    service = BaseService(db)
    result = service.update_by_student_id(table_name, student_id, data)
    if result is None:
        raise HTTPException(status_code=404, detail="记录不存在")
    return {"status": "success", "data": result}


@router.delete(
    "/{table_name}/{id}",
    summary="删除记录",
    description="根据 ID 删除指定表的记录",
    operation_id="删除记录"
)
def delete_record(
    table_name: str,
    id: int,
    db: Session = Depends(get_db)
):
    """
    删除记录接口

    Args:
        table_name: 表名
        id: 记录 ID
        db: 数据库依赖注入

    Returns:
        dict: 删除结果

    Raises:
        HTTPException 404: 记录不存在

    Example:
        DELETE /api/v1/student/{table_name}/{id}
    """
    service = BaseService(db)
    success = service.delete(table_name, id)
    if not success:
        raise HTTPException(status_code=404, detail="记录不存在")
    return {"status": "success", "message": "删除成功"}


@router.get(
    "/{table_name}/{id}",
    summary="查询记录",
    description="根据 ID 查询指定表的记录",
    operation_id="查询记录"
)
def get_record(
    table_name: str,
    id: int,
    db: Session = Depends(get_db)
):
    """
    查询记录接口

    Args:
        table_name: 表名
        id: 记录 ID
        db: 数据库依赖注入

    Returns:
        dict: 查询结果

    Raises:
        HTTPException 404: 记录不存在

    Example:
        GET /api/v1/student/{table_name}/{id}
    """
    service = BaseService(db)
    result = service.get_by_id(table_name, id)
    if result is None:
        raise HTTPException(status_code=404, detail="记录不存在")
    return {"status": "success", "data": result}


@router.post(
    "/query",
    summary="执行 SQL 查询",
    description="执行动态 SQL 查询，需通过 SQL 注入校验",
    operation_id="执行SQL查询"
)
def execute_sql(
    request: RawSQLRequest,
    db: Session = Depends(get_db)
):
    """
    执行 SQL 查询接口

    Args:
        request: SQL 请求，包含 sql 字段
        db: 数据库依赖注入

    Returns:
        dict: 查询结果

    Raises:
        HTTPException 400: SQL 验证失败或执行错误

    Example:
        POST /api/v1/student/query
        {
            "sql": "SELECT * FROM student LIMIT 10"
        }
    """
    sql = request.sql
    
    valid, error = validate_sql(sql)
    if not valid:
        raise HTTPException(status_code=400, detail=error)
    
    try:
        service = BaseService(db)
        result = service.execute_raw_sql(sql)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"SQL 执行错误: {str(e)}")