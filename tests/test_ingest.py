# tests/test_ingest.py

"""Tests for src/pyda/ingestion/ingest.py"""

from pathlib import Path

import pandas as pd
import pytest

from pyda.ingestion.ingest import read_csv, read_json

CSV_FILE = Path("tests/data/test_data.csv")
JSON_FILE = Path("tests/data/test_data.json")


def test_read_csv_returns_dataframe():
    """Reads csv"""
    df = read_csv(CSV_FILE)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "id" in df.columns


def test_read_csv_file_not_found():
    """If csv not found"""
    with pytest.raises(FileNotFoundError):
        read_csv("tests/data/non_existent.csv")


def test_read_json_returns_dataframe():
    """Reads json"""
    df = read_json(JSON_FILE)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "name" in df.columns
