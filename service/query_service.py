# 查询服务层
# 执行原始 SQL 查询并返回结果

from sqlalchemy.orm import Session
from sqlalchemy import text
from core.database import SessionLocal


def execute_query(sql: str) -> list[dict]:
    """
    执行 SQL 查询语句并返回结果列表
    :param sql: SQL 查询语句
    :return: 查询结果列表，每条记录为一个字典
    """
    with SessionLocal() as session:
        result = session.execute(text(sql))
        return [dict(row) for row in result.mappings()]