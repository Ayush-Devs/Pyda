# tests/test_ingest.py

"""Tests for src/pyda/ingestion/ingest.py"""

import pandas as pd

from pyda.ingestion.ingest import read_csv, read_json


def test_read_csv(tmp_path):
    """Tests csv"""
    file = tmp_path / "test.csv"
    file.write_text("a,b\n1,2\n3,4")
    df = read_csv(file)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)


def test_read_json(tmp_path):
    """Tests json"""
    file = tmp_path / "test.json"
    file.write_text('[{"a":1,"b":2},{"a":3,"b":4}]')
    df = read_json(file)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
