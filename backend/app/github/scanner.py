from pathlib import Path

# ---------------------------------------------------------
# Directories that should not be scanned
# ---------------------------------------------------------

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
    "tests",
    "test",
    "docs",
    "examples",
    ".github",
}

# ---------------------------------------------------------
# Supported source code extensions
# ---------------------------------------------------------

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

# ---------------------------------------------------------
# Scan Repository
# ---------------------------------------------------------

def scan_repository(repo_path: Path) -> list[Path]:
    """
    Scan a repository and return all supported source code files.

    Args:
        repo_path: Path to the cloned repository.

    Returns:
        List of source code files.
    """

    source_files = []

    for file in repo_path.rglob("*"):

        # Skip directories
        if not file.is_file():
            continue

        # Skip ignored directories
        if any(part in IGNORE_DIRECTORIES for part in file.parts):
            continue

        # Skip unsupported file types
        if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        source_files.append(file)

    return source_files