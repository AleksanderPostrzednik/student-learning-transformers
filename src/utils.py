import re
from pathlib import Path
import pandas as pd
from typing import Iterable, Optional

try:
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
except Exception:
    WordCloud = None  # type: ignore
    plt = None  # type: ignore


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


def plot_wordcloud(text: str, stopwords: Optional[Iterable[str]] = None) -> None:
    """Plot a word cloud for given text."""
    if WordCloud is None or plt is None:
        raise ImportError("wordcloud or matplotlib is not installed")
    wc = WordCloud(width=800, height=400, stopwords=set(stopwords or []), background_color="white").generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
