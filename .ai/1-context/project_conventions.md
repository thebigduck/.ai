# Project Conventions


This document captures how development happens in this repository.

## Coding Style

- Follow **PEP 8** as the baseline style guide.
- Format code using `black` with the default 88 character line length.
- Use `snake_case` for variables and functions and `CamelCase` for classes.

## Branch Strategy

- Work happens in short-lived feature branches created from `main`.
- Branch names use the pattern `type/short-description` (e.g. `feat/add-cli`).
- All changes go through pull requests before merging back into `main`.

## Commit Message Format

- Commit messages follow the **Conventional Commits** standard:
  - `type(scope?): summary`
  - Example: `docs(readme): clarify installation instructions`
- Use the imperative mood in the summary line and keep it under 72 characters.

## Linting

- The recommended linter is **flake8**.
- Configuration is stored in the repository root at `.flake8`.
- Run `flake8` locally or in CI to enforce the style rules.

This document defines coding standards and workflow conventions for this repository.

## Coding Style
Describe the preferred code formatting rules and style conventions.

## Branch Strategy
Outline how feature branches are named and merged.

## Commit Messages
Explain the expected commit message format, including prefixes or references.

## Linting
Use `flake8` for Python linting. The configuration is located in `setup.cfg`.

