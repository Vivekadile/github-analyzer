from app.github.clone import clone_repository
from app.github.scanner import scan_repository
from app.github.reader import read_file
from app.rag.chunker import chunk_text
from app.rag.embeddings import create_embeddings
from app.rag.vectorstore import store_embeddings


def main():

    github_url = "https://github.com/langchain-ai/langchain.git"

    # Step 1: Clone Repository
    repo_path = clone_repository(github_url)

    print(f"\nRepository Path: {repo_path}")

    # Step 2: Scan Repository
    files = scan_repository(repo_path)

    print(f"Total Source Files: {len(files)}")

    # Step 3: Find the first non-empty source file
    first_file = None
    content = ""

    for file in files:
        content = read_file(file)

        if content.strip():
            first_file = file
            break

    if first_file is None:
        print("No readable source files found.")
        return

    print(f"\nReading File:")
    print(first_file)

    print(f"\nCharacters: {len(content)}")

    # Step 4: Chunk the file
    chunks = chunk_text(content)

    print(f"\nTotal Chunks: {len(chunks)}")

    if chunks:
        print("\nFirst Chunk\n")
        print("=" * 70)
        print(chunks[0])
        print("=" * 70)

        print("\nChunk Statistics\n")

        for index, chunk in enumerate(chunks):
            print(f"Chunk {index + 1}: {len(chunk)} characters")

    else:
        print("No chunks were generated.")

    

    chunks = chunk_text(content)

    embeddings = create_embeddings(chunks)

    print(f"Total Chunks: {len(chunks)}")
    print(f"Total Embeddings: {len(embeddings)}")

    print(f"Embedding Dimension: {len(embeddings[0])}")

    print("\nFirst 10 values of first embedding:")
    print(embeddings[0][:10])
    print(len(embeddings))
    print(len(embeddings[0]))
    store_embeddings(chunks, embeddings)

    embeddings = create_embeddings(chunks)


if __name__ == "__main__":
    main()