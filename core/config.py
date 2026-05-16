# 数据库连接配置模块
# 提供 SQLAlchemy 引擎、会话管理器和基类

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL 数据库连接字符串
DATABASE_URL = "mysql+pymysql://root:123456@localhost/osatable"

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建会话工厂，用于获取数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类，所有 ORM 模型继承此基类
Base = declarative_base()


def get_db():
    """
    依赖注入函数，获取数据库会话
    用法: 在 FastAPI 路由函数参数中使用 db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()