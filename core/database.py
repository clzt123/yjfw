from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings
from typing import Generator


engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"auth_plugin_map": settings.AUTH_PLUGIN_MAP},
    pool_pre_ping=True,
    pool_recycle=300,
    echo=settings.DEBUG
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    数据库会话依赖注入函数

    用于 FastAPI 的 Depends(get_db)，确保每个请求都能获得独立的数据库会话，
    请求结束后自动关闭会话

    Yields:
        Session: SQLAlchemy 数据库会话对象

    Example:
        @app.get("/items")
        def get_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
