from sqlmodel import create_engine, SQLModel, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

db_url = Config.DATABASE_URL
if db_url is None:
    raise RuntimeError("Config.DATABASE_URL must be set")

engine = AsyncEngine(
    create_engine(
        url=db_url,
        echo=True,
    )
)

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)