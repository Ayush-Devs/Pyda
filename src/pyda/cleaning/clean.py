# src/pyda/cleaning/clean.py

"""Basic cleaning module for pyda."""

import pandas as pd


def clean_missing(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """Handle missing values in the DataFrame. strategy: drop or fill"""
    if strategy == "drop":
        df = df.dropna()
    elif strategy == "fill":
        df = df.fillna(0)
    else:
        raise ValueError("Strategy must be 'drop' or 'fill'.")

    print(f"After clean_missing: shape={df.shape}")
    return df


def normalize_columns(df: pd.DataFrame, case: str = "lower") -> pd.DataFrame:
    """Normalize column names: lowercase, strip spaces."""
    if case == "lower":
        df.columns = [c.lower().strip() for c in df.columns]
    elif case == "upper":
        df.columns = [c.upper().strip() for c in df.columns]
    else:
        raise ValueError("case must be 'lower' or 'upper'.")

    print(f"After normalize_columns: columns={df.columns.tolist()}")
    return df
