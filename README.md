
# Pyda

**Pyda** — Python Data Analysis & ETL library, lightweight, beginner-friendly, and extensible.

Pyda is designed to simplify data workflows for both beginners and experienced developers who need a **quick, working ETL setup**. Its lightweight design makes it ideal not only for production-ready pipelines but also for **prototyping** and experimentation, where speed of setup and clarity of code are more important than full optimization. Whether you’re quickly exploring a dataset, building reproducible analysis, or developing modular pipelines for your team, Pyda provides a **structured yet flexible framework** to ingest, transform, and analyze your data efficiently.

It emphasizes **clarity, modularity, and step-based processing**, enabling users to selectively run specific parts of their pipeline while keeping the codebase maintainable and extensible. Pyda’s design makes it easy to add new steps, integrate additional data sources, and adjust processing logic without rewriting existing code. It also logs each step’s progress, providing immediate feedback on the dataset shape, columns, and potential issues, which is invaluable during both prototyping and development phases.



## Table of Contents

1. [Introduction](#introduction)
2. [Motivation & Goals](#motivation--goals)
3. [Key Features](#key-features)
4. [Installation](#installation)
5. [Basic Usage](#basic-usage)
6. [Pipeline Example](#pipeline-example)
7. [Extensibility](#extensibility)
8. [Development & Contribution](#development--contribution)
9. [Code Quality](#code-quality)



## Introduction

**Pyda** is a lightweight Python library designed to simplify **data ingestion, cleaning, transformation, and analysis** workflows. It provides a structured, modular approach to building ETL pipelines while maintaining a low barrier of entry for beginners in Python and data engineering.

Unlike heavy frameworks, Pyda focuses on **clarity, flexibility, and extensibility**, making it ideal for:

* Students learning data analysis
* Junior engineers building ETL pipelines
* Teams wanting a **standardized workflow** without complex dependencies
* Quick prototyping and non-optimal setups where setup speed is prioritized



## Motivation & Goals

Data processing pipelines in Python often require a combination of libraries like `pandas`, `numpy`, or custom code. Beginners frequently struggle with:

* Structuring ingestion, transformation, and analysis steps
* Writing reusable and maintainable code
* Handling errors consistently
* Choosing which steps to apply to their data

Pyda was created to **solve these problems** by:

1. Providing **simple, reusable functions** for ingestion (CSV, JSON)
2. Allowing **pipeline step selection**, so users can choose which steps to run
3. Following **best practices** for code structure and documentation
4. Making the code **extensible**, so new steps can be added easily
5. Maintaining **strict code quality** with Flake8, autoflake, and black



## Key Features

* **Flexible Ingestion**: Read CSV or JSON files safely with file checks and warnings.
* **Extensible Pipeline**: Add and run custom processing steps with a simple decorator.
* **Step Selection**: Users can choose which steps to run, enabling partial processing.
* **Automatic Logging**: Every step prints status, shapes, and columns for quick insights.
* **Professional Code Quality**: Ready for production, with strict static analysis tools.



## Installation

You can install Pyda locally using `Poetry`:

```bash
git clone https://github.com/yourusername/pyda.git
cd pyda
poetry install
```

Or using `pip` (after building locally):

```bash
pip install .
```

**Development dependencies**:

* Python 3.12+
* pandas >=3.0.1, <4.0.0
* pre-commit (for code quality)



## Basic Usage

### Reading CSV Files

```python
from pyda.ingestion.ingest import read_csv

df = read_csv("examples/titanic/Titanic-Dataset.csv")
print(df.head())
```

### Reading JSON Files

```python
from pyda.ingestion.ingest import read_json

df = read_json("examples/titanic/Titanic-Dataset.json")
print(df.head())
```

All ingestion functions perform **basic checks**:

* Verify file exists
* Warn if the file is empty
* Print dataset shape and column names



## Pipeline Example

Pyda supports **modular, step-based pipelines**. Each step is **registered and executed dynamically**, enabling users to **selectively run any subset of steps**.

```python
from pyda.pipeline import PIPELINE_STEPS, run_pipeline

# Run only selected steps
df = run_pipeline(selected_steps=["ingest", "transform"])
```

### How the Pipeline Works

1. **Step Registration**: Steps are created as decorated functions using `@step("step_name")`.
2. **Dynamic Execution**: `run_pipeline()` iterates through all registered steps and executes only the ones selected by the user.
3. **Logging**: Each step logs its execution status, dataset shape, and columns for transparency.
4. **Extensibility**: Developers can add new steps without modifying existing pipeline logic.
5. **Partial Pipelines**: Users can run only a subset of steps depending on their workflow needs, e.g., ingest only or ingest + transform.

This design makes Pyda ideal for **prototyping, iterative development, and flexible ETL workflows**. It keeps code modular, readable, and maintainable while providing immediate feedback for each processing stage.



## Extensibility

Pyda encourages **modular, extensible workflows**:

* Add new ingestion, cleaning, or transformation functions
* Register them using the `@step` decorator
* Users can select steps dynamically without touching old code

This ensures **long-term maintainability** while remaining beginner-friendly.



## Development & Contribution

For details on contributing, please refer to the [CONTRIBUTION.md](CONTRIBUTION.md) file.

Basic setup for development:

```bash
poetry install
pre-commit install
pre-commit run --all-files
pytest
```



## Code Quality

Pyda uses **modern Python tooling** for maintainability:

* **Black**: code formatting
* **Isort**: import sorting
* **Autoflake**: remove unused imports and variables
* **Flake8 + Flake8-docstrings**: enforce coding style and documentation
* **Pre-commit hooks**: ensure code quality before committing


Wrapping Up

Pyda is more than just a library — it’s a framework for clarity, learning, and rapid experimentation. By providing modular, step-based pipelines, transparent logging, and beginner-friendly functions, it empowers developers to focus on solving data problems rather than wrestling with boilerplate code.

Whether you’re prototyping a new idea, building a production-ready ETL pipeline, or teaching data workflows to others, Pyda offers a clean, extensible, and maintainable foundation. Its combination of simplicity, flexibility, and robust code quality tools ensures that your projects remain reliable, readable, and reproducible — no matter the size of the dataset or the complexity of the pipeline.

Start small, experiment fast, and scale confidently — that’s the Pyda way.