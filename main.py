from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.student_routes_api import router as student_router
from api.course_api import router as course_router
from api.event_api import router as event_router
from api.student_score_api import router as student_score_router
from api.student_services_api import router as student_services_router
from api.crm_lead_api import router as crm_lead_router
from api.employee_daily_report_api import router as employee_daily_report_router
from api.student_feedback_ticket_api import router as student_feedback_ticket_router
from api.student_psych_alert_api import router as student_psych_alert_router
from api.student_psych_profile_api import router as student_psych_profile_router
from api.query_api import router as query_router
from api.user_api import router as user_router
from core.config import settings
from core.database_init import init_database
from typing import Dict


app = FastAPI(
    title="Dify HTTP Request Service",
    description="用于对接 Dify 的后端服务，提供数据库 CRUD 和动态 SQL 查询功能，同时提供用户登录验证",
    version="1.0.0"
)

# 初始化数据库（删除现有表 -> 创建新表 -> 插入测试数据）
init_database()

# 配置CORS（允许跨域调用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(user_router, prefix="/api/v1/user", tags=["用户管理"])
app.include_router(student_router, prefix="/api/v1/student", tags=["学生管理"])
app.include_router(course_router, prefix="/api/v1/course", tags=["课程项目"])
app.include_router(event_router, prefix="/api/v1/event", tags=["活动讲座"])
app.include_router(student_score_router, prefix="/api/v1/score", tags=["学生成绩"])
app.include_router(student_services_router, prefix="/api/v1/service", tags=["学生服务"])
app.include_router(crm_lead_router, prefix="/api/v1/lead", tags=["意向客户"])
app.include_router(employee_daily_report_router, prefix="/api/v1/report", tags=["员工日报"])
app.include_router(student_feedback_ticket_router, prefix="/api/v1/feedback", tags=["投诉反馈"])
app.include_router(student_psych_alert_router, prefix="/api/v1/psych-alert", tags=["心理预警"])
app.include_router(student_psych_profile_router, prefix="/api/v1/psych-profile", tags=["心理画像"])
app.include_router(query_router, prefix="/api/v1/query", tags=["SQL查询"])

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/", summary="首页", description="返回前端首页")
def index():
    return FileResponse("frontend/index.html")


@app.get("/health", summary="健康检查", description="验证服务是否正常运行")
def health_check() -> Dict[str, str]:
    """
    健康检查接口

    用于验证服务是否正常运行，返回服务的基本状态信息

    Returns:
        Dict: 包含服务状态和名称的字典

    Example:
        GET /health 返回 {"status": "ok", "service": "Dify HTTP Request Service"}
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
