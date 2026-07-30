from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks: list[str]) -> list[list[float]]:
    """
    Generate vector embeddings for text chunks.
    """

    if not chunks:
        return []

    embeddings = EMBEDDING_MODEL.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=False,
    )

    return embeddings.tolist()