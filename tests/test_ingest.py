# tests/test_ingest.py

"""Tests for src/pyda/ingestion/ingest.py"""

from pathlib import Path

import pandas as pd
import pytest

from pyda.ingestion.ingest import load_source, read_csv, read_json

# Test files
CSV_FILE = Path("tests/data/test_data.csv")
JSON_FILE = Path("tests/data/test_data.json")


# ------------------------
# read_csv tests
# ------------------------
def test_read_csv_returns_dataframe():
    """Happy path CSV"""
    df = read_csv(CSV_FILE)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "id" in df.columns


def test_read_csv_file_not_found():
    """Raise FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        read_csv("tests/data/non_existent.csv")


def test_read_csv_empty_file(tmp_path, capsys):
    """CSV file exists but empty"""
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("id,name\n")  # only header, no data

    df = read_csv(empty_csv)
    assert isinstance(df, pd.DataFrame)
    assert df.empty

    captured = capsys.readouterr()
    assert "Warning" in captured.out
    assert f"{empty_csv}" in captured.out


# ------------------------
# read_json tests
# ------------------------
def test_read_json_returns_dataframe():
    """Happy path JSON"""
    df = read_json(JSON_FILE)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "name" in df.columns


def test_read_json_file_not_found():
    """Raise FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        read_json("tests/data/non_existent.json")


def test_read_json_empty_file(tmp_path, capsys):
    """JSON file exists but empty"""
    empty_json = tmp_path / "empty.json"
    empty_json.write_text("[]")  # empty JSON array

    df = read_json(empty_json)
    assert isinstance(df, pd.DataFrame)
    assert df.empty

    captured = capsys.readouterr()
    assert "Warning" in captured.out
    assert f"{empty_json}" in captured.out


# ------------------------
# load_source tests
# ------------------------
@pytest.mark.parametrize(
    "source_type,expected_columns", [("csv", ["id", "name"]), ("json", ["id", "name"])]
)
def test_load_source_valid_types(source_type, expected_columns):
    """load_source loads CSV and JSON correctly"""
    file_path = CSV_FILE if source_type == "csv" else JSON_FILE
    df = load_source(source_type, file_path)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    for col in expected_columns:
        assert col in df.columns


def test_load_source_unsupported_type():
    """load_source raises ValueError for unsupported type"""
    with pytest.raises(ValueError):
        load_source("xlsx", CSV_FILE)


def test_load_source_file_path_as_Path():
    """load_source works with Path object"""
    df = load_source("csv", Path(CSV_FILE))
    assert isinstance(df, pd.DataFrame)
