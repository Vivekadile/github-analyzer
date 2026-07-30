from pathlib import Path


def read_file(file_path: Path) -> str:
    """
    Safely read a source file.

    Args:
        file_path: Path of the source file.

    Returns:
        File contents or an empty string if unreadable.
    """

    try:
        return file_path.read_text(
            encoding="utf-8"
        )

    except (UnicodeDecodeError, OSError):
        print(f"Skipped unreadable file: {file_path}")
        return ""