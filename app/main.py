from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.v1.endpoints import posts, users, portfolio, contact, about
from app.core.config import settings
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog Backend",
    debug=settings.DEBUG
)

# Setup CORS origins
ORIGINS = settings.CORS_ORIGINS if settings.CORS_ORIGINS else [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000"
]

@app.get("/", include_in_schema=False)
async def index():
    return {
        "message": "Welcome to the Blog Portfolio API."
    }
    
# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(posts.router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(portfolio.router, prefix="/api/v1/portfolio", tags=["portfolio"])
app.include_router(contact.router, prefix="/api/v1/contact", tags=["contact"])
app.include_router(about.router, prefix="/api/v1/about", tags=["about"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
