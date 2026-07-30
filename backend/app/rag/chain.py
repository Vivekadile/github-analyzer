from app.rag.llm import generate_answer
from app.rag.prompt import build_prompt
from app.rag.retriever import retrieve_chunks


def ask_question(question: str) -> str:
    """
    Answer a user question using the indexed repository.
    """

    if not question:
        return ""

    chunks = retrieve_chunks(question)

    if not chunks:
        return "I could not find that information in the repository."

    prompt = build_prompt(
        question=question,
        chunks=chunks,
    )

    return generate_answer(prompt)