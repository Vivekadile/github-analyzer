from pathlib import Path
from urllib.parse import urlparse

from git import Repo
from pathlib import Path

# backend directory
BASE_DIR = Path(__file__).resolve().parents[2]

# backend/repositories
REPOSITORIES_DIR = BASE_DIR / "repositories"

REPOSITORIES_DIR.mkdir(exist_ok=True)



def get_repository_name(repo_url: str) -> str:
    """
    Extract the repository name from a GitHub repository URL.

    Args:
        repo_url: The GitHub repository URL.

    Returns:
        Repository name without the '.git' suffix.
    """

    parsed_url = urlparse(repo_url)
    path = parsed_url.path.strip("/")
    parts = path.split("/")

    repo_name = parts[-1]

    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    return repo_name


def validate_github_url(repo_url: str) -> bool:
    """
    Validate whether the given URL is a valid GitHub repository URL.

    Args:
        repo_url: GitHub repository URL.

    Returns:
        True if the URL is valid, otherwise False.
    """

    if not repo_url:
        return False

    parsed_url = urlparse(repo_url)

    if parsed_url.scheme not in ("http", "https"):
        return False

    if parsed_url.netloc != "github.com":
        return False

    path = parsed_url.path.strip("/")
    parts = path.split("/")

    if len(parts) < 2:
        return False

    return True


def clone_repository(repo_url: str) -> Path:
    """
    Clone a GitHub repository.

    Args:
        repo_url: Public GitHub repository URL.

    Returns:
        Path to the cloned repository.

    Raises:
        ValueError: If the GitHub URL is invalid.
    """

    if not validate_github_url(repo_url):
        raise ValueError("Invalid GitHub repository URL.")

    repo_name = get_repository_name(repo_url)

    destination = REPOSITORIES_DIR / repo_name

    # Already cloned
    if destination.exists():
        print("Repository already exists.")
        return destination

    print("Cloning repository...")

    Repo.clone_from(repo_url, destination)

    print("Repository cloned successfully.")

    return destination

