from app.rag.embeddings import EMBEDDING_MODEL
from app.rag.vectorstore import get_collection


def retrieve_chunks(
    question: str,
    top_k: int = 5,
) -> list[str]:
    """
    Retrieve the most relevant chunks for a user question.
    """

    if not question:
        return []

    question_embedding = EMBEDDING_MODEL.encode(
        question,
        convert_to_numpy=True,
    ).tolist()

    collection = get_collection()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
    )

    documents = results.get("documents", [])

    if not documents:
        return []

    chunks = documents[0]

    if not chunks:
        return []

    return chunks