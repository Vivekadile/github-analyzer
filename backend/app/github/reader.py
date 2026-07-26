from pathlib import Path


def read_file(file_path: Path) -> str:
    """
    Read a source code file.

    Args:
        file_path: Path to the source file.

    Returns:
        File content as a string.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    content = file_path.read_text(encoding="utf-8")

    return content