#!/usr/bin/env python
"""Download Yelp Review Full dataset from Hugging Face."""
# pyright: reportAttributeAccessIssue=false
import os
from datasets import load_dataset

DATA_DIR = os.environ.get("DATA_DIR", "data")
FILE = os.path.join(DATA_DIR, "yelp_reviews.csv")


def main() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Downloading dataset (this may take a while)...")
    ds = load_dataset("Yelp/yelp_review_full", split="train")
    ds.to_pandas().to_csv(FILE, index=False)
    print(f"Dataset saved to {FILE}")


if __name__ == "__main__":
    main()
