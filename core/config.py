from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Settings(BaseSettings):
    """
    应用配置类

    从环境变量或 .env 文件中读取配置参数

    Attributes:
        DATABASE_URL: MySQL 数据库连接 URL
        APP_HOST: 应用服务监听地址
        APP_PORT: 应用服务监听端口
        DEBUG: 是否开启调试模式
    """
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:123456@localhost:3306/osatable"
    )
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8080"))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    class Config:
        env_file = ".env"


settings = Settings()
