# tests/test_feature.py

"""Tests for src/pyda/processing/feature.py"""

import pandas as pd

from pyda.processing.feature import feature_engineer


def test_feature_engineer_adds_squared_columns():
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4], "z": ["a", "b"]})
    df_new = feature_engineer(df)
    assert "x_squared" in df_new.columns
    assert "y_squared" in df_new.columns
    assert df_new["x_squared"].tolist() == [1, 4]
    assert df_new["y_squared"].tolist() == [9, 16]
