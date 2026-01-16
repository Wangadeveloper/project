import os
from dotenv import load_dotenv

# Load .env only in local development (Render ignores it)
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Application configuration.

    This app uses a custom JSON-backed RDBMS,
    so filesystem paths MUST be writable.
    """

    # -------------------------------------------------
    # Core Flask
    # -------------------------------------------------
    SECRET_KEY = os.environ.get("SECRET_KEY")

    if not SECRET_KEY:
        raise RuntimeError("❌ SECRET_KEY is not set")

    # -------------------------------------------------
    # Custom RDBMS (JSON storage)
    # -------------------------------------------------
    # Writable both locally and on Render
    DATA_DIR = os.environ.get(
        "DATA_DIR",
        os.path.join(BASE_DIR, "instance", "data")
    )

    # -------------------------------------------------
    # Generated reports (PDFs)
    # -------------------------------------------------
    REPORTS_DIR = os.environ.get(
        "REPORTS_DIR",
        os.path.join(BASE_DIR, "loan", "static", "reports")
    )

    # -------------------------------------------------
    # Google Gemini AI
    # -------------------------------------------------
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

    if not GOOGLE_API_KEY:
        raise RuntimeError("❌ GOOGLE_API_KEY is not set")
