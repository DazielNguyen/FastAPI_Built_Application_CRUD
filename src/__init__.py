from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting up...")
    await init_db()
    yield
    print(f"Server has been stopped...")


version = "v1"

app = FastAPI(
    title="Book CRUD API",
    description="API for managing books",
    version=version,
    lifespan=life_span
)
app.include_router(book_router, prefix=f"/api/{version}/books", tags =["Books"])