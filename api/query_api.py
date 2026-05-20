# SQL 查询 API 路由
# 接收 SQL 语句并执行，返回查询结果

from fastapi import APIRouter
from pydantic import BaseModel
from service.query_service import execute_query

router = APIRouter()


class QueryRequest(BaseModel):
    sql: str


class QueryResponse(BaseModel):
    code: int
    data: list = None
    message: str = None


@router.post(
    "/execute",
    response_model=QueryResponse,
    summary="执行SQL查询",
    description="执行动态SQL查询语句，返回JSON格式的查询结果",
    operation_id="执行SQL查询"
)
def query_sql(request: QueryRequest):
    """执行SQL查询语句
    
    Args:
        request: SQL查询请求，包含sql字段
    
    Returns:
        QueryResponse: 查询结果，包含code、data和message字段
    """
    try:
        result = execute_query(request.sql)
        return QueryResponse(code=200, data=result)
    except Exception as e:
        return QueryResponse(code=500, message=str(e))