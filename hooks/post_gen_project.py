"""This module is called after project is created."""
import os
from pathlib import Path
from shutil import rmtree

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name }}"

# Values to generate correct
ORGANIZATION = "{{ cookiecutter.organization }}"

# Values to generate github repository
GIT_HOST = "{{ cookiecutter.git_host }}"
USER_NAME = "{{ cookiecutter.user_name }}"


def remove_unused_files(directory: Path) -> None:
    """Remove unused files.

    Args:
        directory: path to the project directory
        module_name: project module name
        need_to_remove_cli: flag for removing CLI related files
    """
    files_to_delete: list[Path] = []

    if GIT_HOST == "GitHub":
        files_to_delete.append(os.path.join(directory, ".gitlab-ci.yml"))
    if GIT_HOST == "GitLab":
        files_to_delete.append(os.path.join(directory, ".github"))

    for path in files_to_delete:
        if os.path.isdir(path):
            rmtree(path)
        else:
            os.remove(path)


def main() -> None:
    remove_unused_files(directory=PROJECT_DIRECTORY)


if __name__ == "__main__":
    main()
