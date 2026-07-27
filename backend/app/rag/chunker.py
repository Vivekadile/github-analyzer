from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text: str) -> list[str]:
    """
    Split source code into smaller chunks.

    Args:
        text: Source code as a string.

    Returns:
        List of text chunks.
    """
    if not text:
        return []
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)
    return chunks

