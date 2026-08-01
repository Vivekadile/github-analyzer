from app.github.clone import clone_repository
from app.github.scanner import scan_repository
from app.github.reader import read_file

from app.rag.chunker import chunk_text
from app.rag.embeddings import create_embeddings
from app.rag.vectorstore import (
    clear_collection,
    store_embeddings,
)


def analyze_repository(
    github_url: str,
) -> None:
    """
    Clone, process, and index a GitHub repository.
    """

    # ---------------------------------------------------------
    # Clone Repository
    # ---------------------------------------------------------
    repo_path = clone_repository(github_url)

    print(f"\nRepository Path: {repo_path}")

    # ---------------------------------------------------------
    # Scan Repository
    # ---------------------------------------------------------
    files = scan_repository(repo_path)

    print(f"Total Source Files: {len(files)}")

    # ---------------------------------------------------------
    # Clear Previous Embeddings
    # ---------------------------------------------------------
    clear_collection()

    # ---------------------------------------------------------
    # Index Repository
    # ---------------------------------------------------------
    indexed_files = 0

    for file in files:

        content = read_file(file)

        if not content.strip():
            continue

        chunks = chunk_text(content)

        if not chunks:
            continue

        embeddings = create_embeddings(chunks)

        store_embeddings(
            chunks=chunks,
            embeddings=embeddings,
            file_path=file,
        )

        indexed_files += 1

        print(f"Indexed {indexed_files}: {file}")

    print("\nRepository indexing completed.")