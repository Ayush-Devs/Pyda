# examples/titanic/example_ingest.py
from pyda.ingestion.ingest import read_csv


def main():
    csv_file = "examples/titanic/Titanic-Dataset.xls"

    df = read_csv(csv_file)

    print("\nFirst 5 rows of the dataset:")
    print(df.head())


if __name__ == "__main__":
    main()
