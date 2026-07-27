from sentence_transformers import SentenceTransformer
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
def create_embeddings(chunks: list[str]) -> list[list[float]]:
    """
    Generate vector embeddings for text chunks.

    Args:
        chunks: List of text chunks.

    Returns:
        List of embedding vectors.
    """

    if not chunks:
        return []

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings.tolist()