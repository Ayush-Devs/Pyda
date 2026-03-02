# src/pyda/ingestion/ingest.py

"""
Ingestion module for pyda.

Contains functions to read and process input data for the ETL pipeline.
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

    print(
        f"Loaded {file_path} with shape {df.shape} and columns: {df.columns.tolist()}"
    )
    return df


def read_json(file_path: str) -> pd.DataFrame:
    """Read a JSON file into a pandas DataFrame with basic checks."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    df = pd.read_json(path)

    if df.empty:
        print(f"Warning: {file_path} is empty.")

    print(
        f"Loaded {file_path} with shape {df.shape} and columns: {df.columns.tolist()}"
    )
    return df
