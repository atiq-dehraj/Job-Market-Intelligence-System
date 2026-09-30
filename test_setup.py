"""
test_setup.py
Phase 1 smoke test.
Confirms that folders exist, config values load, and logging works.
"""

from config import (
    DATA_DIR, LOGS_DIR, REPORTS_DIR, UPLOADS_DIR,
    KEYWORDS, COUNTRIES, SKILL_DEMAND_WEIGHTS,
    ADZUNA_APP_ID,
)
from logger import get_logger

log = get_logger("phase1.test")


def main() -> None:
    log.info("Phase 1 smoke test starting...")

    for folder in (DATA_DIR, LOGS_DIR, REPORTS_DIR, UPLOADS_DIR):
        assert folder.exists(), f"Missing folder: {folder}"
        log.info("Folder OK: %s", folder)

    log.info("Keywords loaded: %s", KEYWORDS)
    log.info("Countries loaded: %s", COUNTRIES)
    log.info("Scoring weights: %s", SKILL_DEMAND_WEIGHTS)

    if ADZUNA_APP_ID:
        log.info("Adzuna APP_ID found in .env")
    else:
        log.warning("Adzuna APP_ID not set yet (expected in Phase 1)")

    log.info("Phase 1 smoke test PASSED.")


if __name__ == "__main__":
    main()