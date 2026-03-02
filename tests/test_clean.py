# tests/test_clean.py

"""Tests for src/pyda/cleaning/clean.py"""

import pandas as pd

from pyda.cleaning.clean import clean_missing, normalize_columns


def test_clean_missing_drop():
    df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, None]})
    cleaned = clean_missing(df, strategy="drop")
    assert cleaned.isna().sum().sum() == 0
    assert cleaned.shape[0] == 1  # only row 0 remains


def test_clean_missing_fill():
    df = pd.DataFrame({"a": [1, None], "b": [None, 2]})
    filled = clean_missing(df, strategy="fill")
    assert filled.isna().sum().sum() == 0
    assert filled.iloc[0]["b"] == 0
    assert filled.iloc[1]["a"] == 0


def test_normalize_columns_lower():
    df = pd.DataFrame(columns=["A ", "bC", " D "])
    normalized = normalize_columns(df, case="lower")
    assert normalized.columns.tolist() == ["a", "bc", "d"]


def test_normalize_columns_upper():
    df = pd.DataFrame(columns=["a", "b", "c"])
    normalized = normalize_columns(df, case="upper")
    assert normalized.columns.tolist() == ["A", "B", "C"]
