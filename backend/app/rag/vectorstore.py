from pathlib import Path

import chromadb
from chromadb.api.models.Collection import Collection

# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

CHROMA_DB_DIR = BASE_DIR / "chroma_db"
CHROMA_DB_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------
# Chroma Client
# ---------------------------------------------------------

CLIENT = chromadb.PersistentClient(
    path=str(CHROMA_DB_DIR)
)

COLLECTION_NAME = "github_repository"


# ---------------------------------------------------------
# Collection Accessor
# ---------------------------------------------------------

def get_collection() -> Collection:
    """
    Always return the current collection.
    """
    return CLIENT.get_or_create_collection(
        name=COLLECTION_NAME
    )


# ---------------------------------------------------------
# Clear Collection
# ---------------------------------------------------------

def clear_collection() -> None:
    """
    Delete the existing collection and recreate an empty one.
    """
    try:
        CLIENT.delete_collection(COLLECTION_NAME)
    except Exception:
        # Collection doesn't exist yet.
        pass

    # Recreate it
    get_collection()


# ---------------------------------------------------------
# Helper
# ---------------------------------------------------------

def _create_chunk_ids(
    file_path: Path | str,
    count: int,
) -> list[str]:
    """
    Generate unique IDs for all chunks of a file.
    """

    # Convert Path -> string safely
    file_path = Path(file_path).as_posix()

    safe_path = (
        file_path
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
    )

    return [
        f"{safe_path}_chunk_{i}"
        for i in range(count)
    ]


# ---------------------------------------------------------
# Store Embeddings
# ---------------------------------------------------------

def store_embeddings(
    chunks: list[str],
    embeddings: list[list[float]],
    file_path: Path | str,
) -> None:
    """
    Store document chunks and embeddings in ChromaDB.
    """

    if len(chunks) != len(embeddings):
        raise ValueError(
            "Chunks and embeddings must have the same length."
        )

    collection = get_collection()

    ids = _create_chunk_ids(
        file_path=file_path,
        count=len(chunks)
    )

    file_path_str = Path(file_path).as_posix()

    metadatas = [
        {
            "chunk_id": index,
            "file_path": file_path_str,
        }
        for index in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )