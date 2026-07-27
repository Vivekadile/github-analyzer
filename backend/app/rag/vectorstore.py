import chromadb


# Create (or load) the persistent database
client = chromadb.PersistentClient(path="chroma_db")

# Create (or load) the collection
collection = client.get_or_create_collection(
    name="github_repository"
)


def store_embeddings(
    chunks: list[str],
    embeddings: list[list[float]]
) -> None:
    """
    Store text chunks and their embeddings in ChromaDB.

    Args:
        chunks: List of text chunks.
        embeddings: List of embedding vectors.
    """

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings must have the same length.")

    ids = []
    metadatas = []

    for index in range(len(chunks)):
        ids.append(f"chunk_{index}")
        metadatas.append(
            {
                "chunk_id": index
            }
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks successfully.")