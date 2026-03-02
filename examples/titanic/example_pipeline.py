# examples/titanic/example_pipeline.py

import logging
from pathlib import Path

from pipeline import load_pipeline

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    csv_file = Path("examples/titanic/Titanic-Dataset.xls")

    df = load_pipeline("csv", csv_file)

    print("\nProcessed dataset preview:")
    print(df.head())
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())


if __name__ == "__main__":
    main()
