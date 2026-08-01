from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="GitHub Repository Analyzer API",
    description="Ask questions about any GitHub repository using RAG.",
    version="1.0.0",
)

app.include_router(router)