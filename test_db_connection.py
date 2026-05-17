
from sqlalchemy import create_engine, text
from core.config import settings

print("Testing database connection...")
print("DATABASE_URL:", settings.DATABASE_URL)

try:
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT VERSION()"))
        version = result.scalar()
        print(f"✅ Database connected! MySQL version: {version}")
        
        result = conn.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result]
        print(f"Tables in database: {tables}")
        
except Exception as e:
    print(f"❌ Database connection failed: {type(e).__name__} - {e}")
    import traceback
    print("\nStack trace:")
    traceback.print_exc()
