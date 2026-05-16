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


@router.post("/api/query", response_model=QueryResponse)
def query_sql(request: QueryRequest):
    """
    执行 SQL 查询语句
    接收 SQL 字符串，执行后返回 JSON 格式的查询结果
    """
    try:
        result = execute_query(request.sql)
        return QueryResponse(code=200, data=result)
    except Exception as e:
        return QueryResponse(code=500, message=str(e))