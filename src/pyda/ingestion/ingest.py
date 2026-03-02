# src/pyda/ingestion/ingest.py

"""
Ingestion module for pyda.

Contains functions to read and process input data for the ETL pipeline.
"""

from pathlib import Path
from typing import Callable, Dict

import pandas as pd

# Registry for all ingestion functions
INGEST_REGISTRY: Dict[str, Callable[..., pd.DataFrame]] = {}


def register_source(name: str):
    """
    Decorator to register a new ingestion function in the INGEST_REGISTRY.

    Args:
        name (str): The key name for the source type.
    """

    def decorator(fn: Callable[..., pd.DataFrame]):
        INGEST_REGISTRY[name] = fn
        return fn

    return decorator


def load_source(source_type: str, file_path: str, **kwargs) -> pd.DataFrame:
    """
    Dynamically load data from a registered source type.

    Args:
        source_type (str): Type of source, must be registered in INGEST_REGISTRY.
        file_path (str): Path to the input file.
        **kwargs: Additional arguments to pass to the ingestion function.

    Returns:
        pd.DataFrame: Loaded DataFrame.

    Raises:
        ValueError: If the source_type is not registered.
    """
    if source_type not in INGEST_REGISTRY:
        raise ValueError(
            f"Source type '{source_type}' is not registered. "
            f"Available sources: {list(INGEST_REGISTRY.keys())}"
        )
    return INGEST_REGISTRY[source_type](file_path, **kwargs)


@register_source("csv")
def read_csv(file_path: str, **kwargs) -> pd.DataFrame:
    """Read a CSV file into a pandas DataFrame with basic checks."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    df = pd.read_csv(path, **kwargs)

    if df.empty:
        print(f"Warning: {file_path} is empty.")

    print(
        f"Loaded {file_path} with shape {df.shape} and columns: {df.columns.tolist()}"
    )
    return df


@register_source("json")
def read_json(file_path: str, **kwargs) -> pd.DataFrame:
    """Read a JSON file into a pandas DataFrame with basic checks."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    df = pd.read_json(path, **kwargs)

    if df.empty:
        print(f"Warning: {file_path} is empty.")

    print(
        f"Loaded {file_path} with shape {df.shape} and columns: {df.columns.tolist()}"
    )
    return df
