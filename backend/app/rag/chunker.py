from langchain_text_splitters import RecursiveCharacterTextSplitter

TEXT_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)


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

    return TEXT_SPLITTER.split_text(text)