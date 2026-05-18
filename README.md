
# 统一智能体入口系统

一个用于对接多个Dify智能体的统一入口系统，包含后端（Java Spring Boot）和前端（HTML/JS）。

## 项目结构

```
├── backend/                    # 后端代码
│   ├── src/main/java/com/example/app/
│   │   ├── api/              # RESTful接口（Controller）
│   │   ├── dao/              # 数据访问层（Repository）
│   │   ├── model/            # 实体类（Entity）
│   │   ├── schema/           # DTO模型
│   │   ├── service/          # 业务逻辑层
│   │   └── DifyAgentGatewayApplication.java
│   ├── src/main/resources/
│   │   ├── application.yml   # 应用配置
│   │   └── schema.sql        # 数据库初始化脚本
│   └── pom.xml               # Maven依赖管理
├── frontend/                  # 前端代码
│   ├── index.html            # 主页面
│   ├── css/
│   │   └── style.css         # 样式文件
│   └── js/
│       ├── config.js         # 配置文件（Dify智能体参数）
│       └── app.js            # 应用逻辑
└── README.md                 # 项目说明
```

## 功能特性

- **客服入口**：无需登录，直接进入客服智能体聊天界面
- **员工入口**：登录验证后进入企业智能体聊天界面
- **学生入口**：登录验证后进入学生智能体聊天界面，自动传递学生ID

## 技术栈

### 后端
- Java 21
- Spring Boot 3.2.0
- Spring Data JPA
- MySQL 8.0+

### 前端
- HTML5
- CSS3
- JavaScript (ES6+)

## 快速开始

### 1. 环境要求

- JDK 21+
- Maven 3.8+
- MySQL 8.0+

### 2. 数据库配置

创建MySQL数据库并执行初始化脚本：

```sql
CREATE DATABASE example_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE example_db;
SOURCE backend/src/main/resources/schema.sql;
```

### 3. 修改配置

编辑 `backend/src/main/resources/application.yml`：

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/example_db?useSSL=false&serverTimezone=Asia/Shanghai
    username: your_username
    password: your_password
```

### 4. 启动后端服务

```bash
cd backend
mvn spring-boot:run
```

服务将在 http://localhost:8080 启动。

### 5. 启动前端

使用任意HTTP服务器（如Nginx、Python SimpleHTTPServer）或直接在浏览器中打开：

```bash
cd frontend
python -m http.server 8000
```

访问 http://localhost:8000 查看前端页面。

## API接口

### 用户登录

**POST** `/api/user/login`

请求体：
```json
{
    "username": "string",
    "password": "string"
}
```

响应体：
```json
{
    "success": true,
    "message": "登录成功",
    "id": 1,
    "username": "admin",
    "realName": "管理员",
    "userType": "EMPLOYEE",
    "employeeRole": "管理员",
    "department": "信息中心"
}
```

## Dify智能体配置

在 `frontend/js/config.js` 中配置：

| 智能体类型 | AppID | BaseURL | APIKey |
|-----------|-------|---------|--------|
| 客服智能体 | G3Tsuspuu40ayj52 | http://192.168.110.49:5001/v1 | app-3VKersja1rrvoUav5qupHw1s |
| 企业智能体 | 7looxs6HP9YBSnK8 | http://192.168.110.60:5001/v1 | app-088VszaN9vwAYpbFEMy1U0Hr |
| 学生智能体 | EE4fkzwDP1FPz5ux | http://192.168.110.48:5001/v1 | app-CXyS5dzufPsEFYFR7fADR7Kj |

## 测试账号

| 用户名 | 密码 | 用户类型 |
|--------|------|----------|
| admin | 123456 | 员工（管理员） |
| teacher001 | 123456 | 员工（教师） |
| student001 | 123456 | 学生 |
| student002 | 123456 | 学生 |

## 项目流程图

```
用户访问首页
    │
    ▼
┌───────────────────────────────────────┐
│         菜单页面                       │
│  [客服入口] [员工入口] [学生入口]      │
└───────────────────────────────────────┘
    │              │              │
    ▼              ▼              ▼
客服智能体    登录页面        登录页面
(无需登录)    ┌───────┐      ┌───────┐
    │         │输入   │      │输入   │
    │         │账号密码│      │账号密码│
    │         └──┬────┘      └──┬────┘
    │            │              │
    │            ▼              ▼
    │      验证员工身份      验证学生身份
    │            │              │
    │            ▼              ▼
    │      企业智能体      学生智能体
    │      (传递用户信息)   (传递student_id)
    │
    ▼
┌───────────────────────────────────────┐
│         聊天界面 (iframe嵌入)          │
└───────────────────────────────────────┘
```

## 注意事项

1. 前端使用iframe嵌入Dify WebApp，请确保Dify服务可访问
2. 学生智能体登录时会自动将username作为student_id传递
3. 生产环境请使用HTTPS和密码加密存储
4. 数据库连接信息应使用环境变量配置，避免硬编码

## License

MIT License
