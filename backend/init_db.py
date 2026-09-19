from __future__ import annotations

import os
import time

from database import create_database
from app import ensure_demo_history


def initialize() -> None:
    attempts = max(1, int(os.getenv("MEDSUPPLYAI_DB_INIT_ATTEMPTS", "12")))
    delay = max(1, int(os.getenv("MEDSUPPLYAI_DB_INIT_DELAY", "3")))

    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            print(f"[MedSupplyAI] Database initialization attempt {attempt}/{attempts}")
            create_database()
            if os.getenv("MEDSUPPLYAI_SEED_DEMO", "1").strip().lower() in {"1", "true", "yes", "on"}:
                ensure_demo_history()
            print("[MedSupplyAI] Database initialization successful")
            return
        except Exception as exc:  # noqa: BLE001 - startup retry needs the concrete error
            last_error = exc
            print(f"[MedSupplyAI] Database initialization failed: {exc}")
            if attempt < attempts:
                time.sleep(delay)

    raise RuntimeError(f"Database initialization failed after {attempts} attempts: {last_error}") from last_error


if __name__ == "__main__":
    initialize()
