from fastapi import APIRouter

from app.api.schemas import (
    AnalyzeRequest,
    QuestionRequest,
    AnswerResponse,
)

from app.services.repository_service import analyze_repository
from app.rag.chain import ask_question


router = APIRouter()


@router.get("/")
def home():
    """
    Health check endpoint.
    """

    return {
        "message": "GitHub Analyzer API is running."
    }


@router.post("/analyze")
def analyze_repository_route(request: AnalyzeRequest):
    """
    Analyze and index a GitHub repository.
    """

    analyze_repository(request.github_url)

    return {
        "message": "Repository indexed successfully."
    }


@router.post(
    "/ask",
    response_model=AnswerResponse,
)
def ask_repository(request: QuestionRequest):
    """
    Answer questions about the indexed repository.
    """

    answer = ask_question(request.question)

    return AnswerResponse(
        answer=answer
    )