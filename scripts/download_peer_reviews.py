#!/usr/bin/env python
"""Download argumentative student peer reviews dataset from Hugging Face."""
# pyright: reportAttributeAccessIssue=false
import os
from datasets import load_dataset

DATA_DIR = os.environ.get("DATA_DIR", "data")
FILE = os.path.join(DATA_DIR, "peer_reviews.csv")


def main() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Downloading dataset...")
    ds = load_dataset("samirmsallem/argumentative_student_peer_reviews", split="train")
    ds.to_pandas().to_csv(FILE, index=False)
    print(f"Dataset saved to {FILE}")


if __name__ == "__main__":
    main()
