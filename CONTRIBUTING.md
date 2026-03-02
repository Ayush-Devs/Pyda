# Contributing to Pyda

First off, thank you for your interest in contributing! Your help makes Pyda better for everyone.

This guide will help you get started with contributing to the project smoothly.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Coding Guidelines](#coding-guidelines)
3. [Running Tests](#running-tests)
4. [Pre-Commit Hooks](#pre-commit-hooks)
5. [Submitting a Pull Request](#submitting-a-pull-request)
6. [Reporting Issues](#reporting-issues)

---

## Getting Started

1. **Fork the repository** and clone your fork:

2. **Install dependencies using Poetry**:

```bash
poetry install
```

3. **Activate the Poetry environment**:

```bash
poetry env info
poetry run python
```

Now you are ready to start coding!

---

## Coding Guidelines

- Follow **PEP 8** for Python style.
- Use **black** and **isort** to format code consistently.
- Write clear, concise **docstrings** for any new functions.
- Keep changes **small and focused** per PR.

---

## Running Tests

Pyda uses **pytest** for testing. Run tests locally before submitting a PR:

```bash
poetry run pytest
```

All tests should pass before opening a pull request.

---

## Pre-Commit Hooks

We use pre-commit hooks to keep the code clean and secure. Make sure they pass before committing:

```bash
poetry run pre-commit install
poetry run pre-commit run --all-files
```

The hooks include:
- `black` for code formatting
- `isort` for import sorting
- `flake8` for linting
- `bandit` for security checks
- `detect-private-key`, `check-yaml`, `check-json`, and `trailing-whitespace`

These hooks help keep contributions consistent and error-free.

---

## Submitting a Pull Request

1. Create a new branch for your feature/fix:

```bash
git checkout -b my-feature
```

2. Make your changes and run **tests and pre-commit hooks**.

3. Commit your changes:

```bash
git add .
git commit -m "Add feature X or fix Y"
```

4. Push your branch to your fork and open a PR against `main` in the Pyda repo.

5. Describe your changes clearly and link to any related issues if applicable.

---

## Reporting Issues

If you encounter a bug or have a feature request, please open an **issue** on the GitHub repository.

Include:
- A clear description of the problem or feature
- Steps to reproduce (if applicable)
- Expected vs. actual behavior
- Environment details (Python version, OS, etc.)

---

Thank you for helping make Pyda better!
We appreciate all contributions, no matter how small.
