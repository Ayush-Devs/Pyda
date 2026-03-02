# src/pipeline.py

"""
Unified pipeline interface for pyda.

This module provides a simple high-level API to run ingestion,
cleaning, and feature engineering as a single pipeline.
"""

import logging
from pathlib import Path
from typing import Literal

import pandas as pd

from pyda.cleaning.clean import clean_missing, normalize_columns
from pyda.ingestion.ingest import load_source
from pyda.processing.feature import feature_engineer

logger = logging.getLogger(__name__)

SourceType = Literal["csv", "json"]


def load_pipeline(source_type: SourceType, file_path: str | Path) -> pd.DataFrame:
    """Run the full pyda pipeline on a data source."""
    logger.info("Starting pyda pipeline")
    logger.info("Source type: %s", source_type)
    logger.info("File path: %s", file_path)

    # Step 1: Ingest
    df = load_source(source_type, file_path)
    logger.info("Ingestion complete | Shape: %s", df.shape)

    # Step 2: Clean
    df = clean_missing(df)
    logger.info("Missing values cleaned")

    df = normalize_columns(df)
    logger.info("Columns normalized")

    # Step 3: Feature Engineering
    df = feature_engineer(df)
    logger.info("Feature engineering complete")

    logger.info("Pipeline complete | Final shape: %s", df.shape)

    return df
