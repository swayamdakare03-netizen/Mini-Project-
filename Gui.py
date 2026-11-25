import os
import sys
import shutil
from pathlib import Path


APP_NAME = "DEIVS"


def get_app_data_dir():
    """Return the permanent user data directory for DEIVS."""

    if sys.platform == "win32":
        base_dir = os.environ.get("LOCALAPPDATA")

        if not base_dir:
            base_dir = Path.home() / "AppData" / "Local"

        app_dir = Path(base_dir) / APP_NAME

    elif sys.platform == "darwin":
        app_dir = (
            Path.home()
            / "Library"
            / "Application Support"
            / APP_NAME
        )

    else:
        base_dir = os.environ.get(
            "XDG_DATA_HOME",
            Path.home() / ".local" / "share"
        )
        app_dir = Path(base_dir) / APP_NAME

    app_dir.mkdir(parents=True, exist_ok=True)

    return app_dir


def get_database_path():
    """Return the database path and preserve an existing project database."""

    app_dir = get_app_data_dir()
    database_path = app_dir / "evidence.db"

    # One-time copy of an existing project database.
    if not database_path.exists():

        if getattr(sys, "frozen", False):
            project_dir = Path(sys.executable).resolve().parent
        else:
            project_dir = Path(__file__).resolve().parent

        old_database = project_dir / "evidence.db"

        if old_database.exists():
            shutil.copy2(old_database, database_path)

    return database_path


def get_reports_dir():
    """Return the permanent reports directory."""

    reports_dir = get_app_data_dir() / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    return reports_dir
