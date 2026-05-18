
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI(title="统一智能体入口系统", version="1.0.0")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据库连接
conn = sqlite3.connect('example_db.sqlite')
cursor = conn.cursor()

# 创建用户表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sys_user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        real_name TEXT NOT NULL,
        user_type TEXT NOT NULL,
        employee_role TEXT,
        department TEXT,
        contact_info TEXT,
        status TEXT DEFAULT '正常',
        create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# 插入测试数据
try:
    cursor.execute('''
        INSERT INTO sys_user (username, password, real_name, user_type, employee_role, department, contact_info)
        VALUES 
        ('admin', '123456', '管理员', 'EMPLOYEE', '管理员', '信息中心', '13800138000'),
        ('teacher001', '123456', '张老师', 'EMPLOYEE', '教师', '计算机学院', '13800138001'),
        ('20230001', '123456', '李明', 'STUDENT', NULL, '计算机学院', '13800138002'),
        ('20230002', '123456', '王芳', 'STUDENT', NULL, '电子工程学院', '13800138003')
    ''')
    conn.commit()
except sqlite3.IntegrityError:
    pass  # 数据已存在

conn.close()

# 数据模型
class LoginRequest(BaseModel):
    username: str = Field(..., description="用户名")
    password: str = Field(..., description="密码")

class LoginResponse(BaseModel):
    success: bool
    message: str
    id: Optional[int] = None
    username: Optional[str] = None
    real_name: Optional[str] = None
    user_type: Optional[str] = None
    employee_role: Optional[str] = None
    department: Optional[str] = None

@app.post("/api/user/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """用户登录接口"""
    conn = sqlite3.connect('example_db.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sys_user WHERE username = ?', (request.username,))
    user = cursor.fetchone()
    conn.close()
    
    if not user:
        return LoginResponse(success=False, message="用户名或密码错误")
    
    # 检查状态
    if user[8] != '正常':
        return LoginResponse(success=False, message="账号状态异常，请联系管理员")
    
    # 验证密码
    if user[2] != request.password:
        return LoginResponse(success=False, message="用户名或密码错误")
    
    # 返回用户信息
    return LoginResponse(
        success=True,
        message="登录成功",
        id=user[0],
        username=user[1],
        real_name=user[3],
        user_type=user[4],
        employee_role=user[5],
        department=user[6]
    )

@app.get("/api/user/health")
def health():
    """健康检查"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
