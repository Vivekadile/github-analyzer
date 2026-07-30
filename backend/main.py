from app.github.clone import clone_repository
from app.github.reader import read_file
from app.github.scanner import scan_repository

from app.rag.chain import ask_question
from app.rag.chunker import chunk_text
from app.rag.embeddings import create_embeddings
from app.rag.vectorstore import (
    clear_collection,
    store_embeddings,
)


def index_repository(github_url: str) -> None:
    """
    Clone and index the GitHub repository.
    """

    repo_path = clone_repository(github_url)

    print(f"\nRepository Path: {repo_path}")

    files = scan_repository(repo_path)

    print(f"Total Source Files: {len(files)}")

    clear_collection()

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


def chat() -> None:
    """
    Interactive question-answering loop.
    """

    print("\nRepository is ready.")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask a question: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            continue

        answer = ask_question(question)

        print("\n" + "=" * 80)
        print("ANSWER")
        print("=" * 80)
        print(answer)
        print()


def main():

    github_url = "https://github.com/langchain-ai/langchain.git"

    index_repository(github_url)

    chat()


if __name__ == "__main__":
    main()