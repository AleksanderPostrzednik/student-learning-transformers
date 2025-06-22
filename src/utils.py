import re
from pathlib import Path
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load CSV dataset."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    return pd.read_csv(path)


def clean_text(text: str) -> str:
    """Basic text cleaning used across notebooks."""
    if text is None:
        return ""
    text = str(text).lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
