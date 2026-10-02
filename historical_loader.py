import pandas as pd
from config import ARCHIVE_DIR, DATA_DIR
from logger import get_logger

log = get_logger("phase2.loader")


# Columns that carry no useful information for JMIS:
# - skills_desc is 98% null (2439 / 123849 non-null)
DROP_COLUMNS = ["skills_desc"]


def load_postings() -> pd.DataFrame:
    """Load the main postings CSV and drop useless columns."""
    path = ARCHIVE_DIR / "postings.csv"
    log.info("Loading postings from %s", path)
    df = pd.read_csv(path, low_memory=False)
    log.info("Loaded postings: %d rows x %d columns", *df.shape)

    to_drop = [c for c in DROP_COLUMNS if c in df.columns]
    if to_drop:
        df = df.drop(columns=to_drop)
        log.info("Dropped columns: %s", to_drop)
        log.info("After drop: %d rows x %d columns", *df.shape)

    return df


def load_skill_map() -> pd.DataFrame:
    """
    Load job_skills + skills, merge them into a mapping table
    of (job_id, skill_abr, skill_name). This stays small — no text.
    """
    js_path = ARCHIVE_DIR / "jobs" / "job_skills.csv"
    sk_path = ARCHIVE_DIR / "mappings" / "skills.csv"

    log.info("Loading job_skills from %s", js_path)
    job_skills = pd.read_csv(js_path)
    log.info("Loaded job_skills: %d rows", len(job_skills))

    log.info("Loading skills from %s", sk_path)
    skills = pd.read_csv(sk_path)
    log.info("Loaded skill categories: %d rows", len(skills))

    merged = job_skills.merge(skills, on="skill_abr", how="left")
    log.info("Merged job_id -> skill_name mapping: %d rows", len(merged))
    return merged


def save_parquet(df: pd.DataFrame, filename: str) -> None:
    """
    Save a DataFrame as Parquet with zstd compression.
    zstd compresses long text 3-5x better than snappy at similar speed.
    """
    out_dir = DATA_DIR / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename

    log.info("Saving %s ...", out_path)
    df.to_parquet(out_path, index=False, compression="zstd")
    size_mb = out_path.stat().st_size / (1024 * 1024)
    log.info("Saved %s (%.1f MB, %d rows)", filename, size_mb, len(df))


def main() -> None:
    log.info("historical_loader starting...")

    postings = load_postings()
    skill_map = load_skill_map()

    save_parquet(postings, "postings.parquet")
    save_parquet(skill_map, "job_skills.parquet")

    log.info("historical_loader done.")


if __name__ == "__main__":
    main()