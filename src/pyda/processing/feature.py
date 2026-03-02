# src/pyda/processing/feature.py

"""Feature engineering module for pyda."""

import pandas as pd


def feature_engineer(df: pd.DataFrame) -> pd.DataFrame:
    """Add placeholder engineered features. For now, returns the same DataFrame."""
    # Example: add a new column if numeric columns exist
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        df[f"{col}_squared"] = df[col] ** 2

    print(
        f"After feature_engineer: added squared columns: {[f'{c}_squared' for c in numeric_cols]}"
    )
    return df
