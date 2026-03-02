# src/pyda/ingestion/ingest.py

"""
Ingestion module for pyda.

Contains functions to read input data for the ETL pipeline.
"""

from pathlib import Path

import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """Read a CSV file into a pandas DataFrame with basic checks."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    df = pd.read_csv(path)

    if df.empty:
        print(f"Warning: {file_path} is empty.")

    print(f"Loaded {file_path} with shape {df.shape}")
    return df


def read_json(file_path: str) -> pd.DataFrame:
    """Read a JSON file into a pandas DataFrame with basic checks."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    df = pd.read_json(path)

    if df.empty:
        print(f"Warning: {file_path} is empty.")

    print(f"Loaded {file_path} with shape {df.shape}")
    return df


def load_source(source_type: str, file_path: str | Path) -> pd.DataFrame:
    """Load a dataset from a specified source type into a pandas DataFrame."""
    source_type = source_type.lower()

    if source_type == "csv":
        return read_csv(file_path)
    elif source_type == "json":
        return read_json(file_path)
    else:
        raise ValueError(
            f"Unsupported source type '{source_type}'. " f"Supported types: csv, json"
        )
