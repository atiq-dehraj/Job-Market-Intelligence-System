"""
config.py
Central configuration for the Job Market Intelligence System (JMIS).
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Load .env
load_dotenv()

# 2. Paths
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR          = BASE_DIR / "data"
RAW_DATA_DIR      = DATA_DIR / "raw"
LOGS_DIR          = BASE_DIR / "logs"
REPORTS_DIR       = BASE_DIR / "reports"
UPLOADS_DIR       = BASE_DIR / "uploads"

DB_PATH              = DATA_DIR / "jmis.db"
SKILLS_DICT_PATH     = DATA_DIR / "skills_dictionary.csv"
COURSES_PATH         = DATA_DIR / "courses.csv"
DIVERSITY_TERMS_PATH = DATA_DIR / "diversity_terms.csv"
CITY_COORDS_PATH     = DATA_DIR / "city_coordinates.csv"

# 3. Live data collection
KEYWORDS         = ["data analyst", "python developer", "machine learning"]
COUNTRIES        = ["gb", "us"]
MAX_PAGES        = 3
RESULTS_PER_PAGE = 50

# 4. Languages
SUPPORTED_LANGUAGES = ["en", "ur", "ar", "fr", "de", "es"]

# 5. Scoring weights
SKILL_DEMAND_WEIGHTS = {
    "share":  0.5,
    "salary": 0.3,
    "growth": 0.2,
}

# 6. Alert thresholds
MATCH_SCORE_ALERT_THRESHOLD = 70
EMERGING_INDEX_THRESHOLD    = 0.25
ANOMALY_ZSCORE_THRESHOLD    = 2.5

# 7. Secrets
ADZUNA_APP_ID  = os.getenv("ADZUNA_APP_ID", "")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY", "")

SMTP_HOST     = os.getenv("SMTP_HOST", "")
SMTP_PORT     = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER     = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

API_ACCESS_KEY = os.getenv("API_ACCESS_KEY", "")