from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.student_routes import router as student_router
from api.course import router as course_router
from api.event import router as event_router
from core.config import settings
from typing import Dict


app = FastAPI(
    title="Dify HTTP Request Service",
    description="用于对接 Dify 的后端服务，提供数据库 CRUD 和动态 SQL 查询功能，同时提供课程项目和活动讲座服务",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(student_router, prefix="/api/v1/osa")
app.include_router(course_router, prefix="/api/course", tags=["课程项目"])
app.include_router(event_router, prefix="/api/event", tags=["活动讲座"])


@app.get("/", summary="健康检查", description="验证服务是否正常运行")
def health_check() -> Dict[str, str]:
    """
    健康检查接口

    用于验证服务是否正常运行，返回服务的基本状态信息

    Returns:
        Dict: 包含服务状态和名称的字典

    Example:
        GET / 返回 {"status": "ok", "service": "Dify HTTP Request Service"}
    """
    return {"status": "ok", "service": "Dify HTTP Request Service"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG
    )
