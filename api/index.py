"""Vercel entry point for the Flask application."""

import os

from backend.app import app


def _initialize_database_if_requested() -> None:
    if os.getenv("MEDSUPPLYAI_INIT_DB", "false").lower() not in {"1", "true", "yes"}:
        return

    from backend.app import ensure_demo_history
    from backend.database import create_database

    create_database()
    if os.getenv("MEDSUPPLYAI_SEED_DEMO", "false").lower() in {"1", "true", "yes"}:
        ensure_demo_history()


_initialize_database_if_requested()
