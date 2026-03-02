# examples/titanic/example_ingest.py

from pyda.ingestion.ingest import load_source


def main():
    csv_file = "examples/titanic/Titanic-Dataset.xls"

    df = load_source("csv", csv_file)

    print("\nFirst 5 rows of the dataset:")
    print(df.head())


if __name__ == "__main__":
    main()
