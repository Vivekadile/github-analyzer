from pathlib import Path

# Directories that should not be scanned
IGNORE_DIRECTORIES = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".idea",
    ".vscode",
    "dist",
    "build",
    "tests"
    "test"
}

# Source code file extensions supported by the scanner
SUPPORTED_EXTENSIONS = {
    ".py",
    ".java",
    ".cpp",
    ".c",
    ".h",
    ".hpp",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".go",
    ".rs",
    ".cs",
    ".kt",
    ".swift",
}


def scan_repository(repo_path: Path) -> list[Path]:
    """
    Scan a repository and return all supported source code files.

    Args:
        repo_path: Path to the cloned repository.

    Returns:
        List of source code file paths.
    """

    source_files = []

    for file in repo_path.rglob("*"):

        # Skip directories
        if not file.is_file():
            continue

        # Skip ignored directories
        if any(part in IGNORE_DIRECTORIES for part in file.parts):
            continue

        # Keep only supported source files
        if file.suffix in SUPPORTED_EXTENSIONS:
            source_files.append(file)

    return source_files


