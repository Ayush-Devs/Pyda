# tests/test_clean.py

"""Tests for src/pyda/cleaning/clean.py"""

import pandas as pd
import pytest

from pyda.cleaning.clean import clean_missing, normalize_columns


# ------------------------
# clean_missing tests
# ------------------------
def test_clean_missing_drop(capsys):
    df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, None]})
    cleaned = clean_missing(df, strategy="drop")
    assert cleaned.isna().sum().sum() == 0
    assert cleaned.shape[0] == 1  # only row 0 remains

    captured = capsys.readouterr()
    assert "After clean_missing" in captured.out


def test_clean_missing_fill(capsys):
    df = pd.DataFrame({"a": [1, None], "b": [None, 2]})
    filled = clean_missing(df, strategy="fill")
    assert filled.isna().sum().sum() == 0
    assert filled.iloc[0]["b"] == 0
    assert filled.iloc[1]["a"] == 0

    captured = capsys.readouterr()
    assert "After clean_missing" in captured.out


def test_clean_missing_invalid_strategy():
    df = pd.DataFrame({"a": [1, None]})
    with pytest.raises(ValueError, match="Strategy must be 'drop' or 'fill'"):
        clean_missing(df, strategy="invalid")


# ------------------------
# normalize_columns tests
# ------------------------
def test_normalize_columns_lower(capsys):
    df = pd.DataFrame(columns=["A ", "bC", " D "])
    normalized = normalize_columns(df, case="lower")
    assert normalized.columns.tolist() == ["a", "bc", "d"]

    captured = capsys.readouterr()
    assert "After normalize_columns" in captured.out


def test_normalize_columns_upper(capsys):
    df = pd.DataFrame(columns=["a", "b", "c"])
    normalized = normalize_columns(df, case="upper")
    assert normalized.columns.tolist() == ["A", "B", "C"]

    captured = capsys.readouterr()
    assert "After normalize_columns" in captured.out


def test_normalize_columns_invalid_case():
    df = pd.DataFrame(columns=["a", "b"])
    with pytest.raises(ValueError, match="case must be 'lower' or 'upper'"):
        normalize_columns(df, case="invalid")
