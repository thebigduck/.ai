# .ai

AI Directory Standard (/.ai) – Specification v0.1‑draft
Status: Draft – open for public feedback. Submit issues or pull requests to the ADS working group repository.

## Table of Contents

- [Purpose & Scope](#purpose--scope)
- [Design Goals & Principles](#design-goals--principles)
- [Directory Structure Overview](#directory-structure-overview)
- [File Specifications](#file-specifications)
  - [0-ai-config/](#0-ai-config)
  - [1-context/](#1-context)
  - [2-technical-design/](#2-technical-design)
  - [3-development/](#3-development)
  - [4-acceptance/](#4-acceptance)
- [JSON Schemas](#json-schemas)
- [Lifecycle Workflows](#lifecycle-workflows)
- [Interoperability & Compatibility](#interoperability--compatibility)
- [Adoption & Migration Guide](#adoption--migration-guide)
- [Best Practices & Anti-Patterns](#best-practices--anti-patterns)
- [Appendices](#appendices)
  - [Appendix A: ai-config.json Schema](#appendix-a-ai-configjson-schema)
  - [Appendix B: Glossary](#appendix-b-glossary)
  - [Appendix C: CLI Command Reference](#appendix-c-cli-command-reference)

## Purpose & Scope {#purpose--scope}

The AI Directory Standard (ADS) defines a language-agnostic folder—/.ai/—that acts as the canonical, machine- and human-readable source of truth for all artificial-intelligence assistants interacting with a software repository.

The specification covers:

- Structure: Required sub-directories & files.

- Content: Minimal & recommended metadata for effective AI operation.

- Workflows: How humans and AI agents collaborate to populate, validate, and evolve the directory.

- Interoperability: Alignment with existing configuration files (e.g., Copilot, Cursor) and emerging standards (Model Context Protocol — MCP).


## Design Goals & Principles {#design-goals--principles}

- Comprehensive Context — Aggregate why, what, and how in one place.

- Machine-Readable First — Key metadata expressed as JSON or YAML; narrative docs in Markdown.

- Assistant-Prompted Completeness — AI agents must prompt users to fill missing info or apply defaults.

- Language & Tool Agnostic — No binding to specific stacks; adapters generate tool-specific configs.

- Self-Validation & Auditability — Acceptance criteria and compliance logs reside in-repo for automated checks.

- Non-Redundant — Leverage, not duplicate, existing standards; .ai is a unifying wrapper.


## Directory Structure Overview {#directory-structure-overview}

.ai/
  ├── 0-ai-config/
  │   ├── ai-config.json
  │   ├── workflow.md
  │   └── (tool-specific rule files)
  ├── 1-context/
  │   ├── project_context.md
  │   ├── project_conventions.md
  │   ├── target-personas/
  │   └── standards/
  ├── 2-technical-design/
  │   ├── architecture.md
  │   ├── requirements/
  │   └── features/
  ├── 3-development/
  │   ├── folder-locks.md
  │   └── tasklog/
  └── 4-acceptance/
      ├── acceptance_criteria.md
      └── compliance_reports/

Mandatory vs. Optional

Path

Status

Description

.ai/0-ai-config/ai-config.json

Required

Core project + AI settings.

.ai/1-context/project_context.md

Required

High-level scope & goals.

.ai/4-acceptance/acceptance_criteria.md

Required

Definition of Done checklist.

All others

Recommended

Populate as relevant to project complexity.


## File Specifications {#file-specifications}
### 0-ai-config/ {#0-ai-config}

File

Format

Purpose

ai-config.json

JSON

Machine-readable project metadata & global AI behaviour flags.

workflow.md

Markdown

Human-readable description of AI↔human collaboration workflow.

Tool rule files (e.g. .cursorrules)

Text/MD

Generated or symlinked configs for specific assistants.

ai-config.json – Required Keys
```json
{
  "projectName": "string",
  "description": "string",
  "primaryLanguage": "string",          // e.g. "TypeScript"
  "frameworks": ["string"],             // e.g. ["Next.js", "Prisma"]
  "license": "string",                 // SPDX identifier
  "aiPreferences": {
    "styleGuide": "string",            // e.g. "Google TS Style"
    "testingFramework": "string",      // e.g. "Jest"
    "promptOnMissing": true             // Enforce prompts for missing context
  }
}
```


### 1-context/ {#1-context}

Narrative documentation to orient AI agents.

project_context.md — Problem domain, goals, value proposition, target users.


project_conventions.md — Coding style, branch strategy, commit message guidelines and linting recommendations.


target-personas/ — One Markdown file per persona (persona-alpha.md, persona-beta.md).

standards/ — Links or embedded content for external policies (PCI-DSS, OWASP, etc.).


### 2-technical-design/ {#2-technical-design}

Design-centric artifacts.

Item

Purpose

architecture.md

Diagrams / Mermaid markup of high-level system.

requirements/

Sub-folders for domain requirements (e.g. security/ssl.md).

features/

Each feature gets its own spec folder with specification.md, acceptance tests, etc.



### 3-development/ {#3-development}

File

Purpose

folder-locks.md

Declare areas AI must not auto-modify without human approval.

tasklog/

Timestamped records of AI ↔ human chats; helps continuity.



### 4-acceptance/ {#4-acceptance}

File

Purpose

acceptance_criteria.md

Global Definition of Done checklist.

compliance_reports/

Auto-generated audit & test outcome artifacts.


## JSON Schemas {#json-schemas}
A full JSON Schema for ai-config.json is provided in Appendix A for validation tooling.


## Lifecycle Workflows {#lifecycle-workflows}

For a detailed reference on the commands mentioned below, see Appendix C.

Initialization – Run ai-init CLI: scaffolds .ai, stubs templates.

Population – AI prompts user to fill blanks → writes values to JSON/Markdown.



Development – AI references .ai for code generation, doc sync, and linting rules (see `1-context/project_conventions.md`).


Validation – CI and/or AI agents verify code against 4-acceptance/ using ai-validate.

Maintenance – On repo changes, AI proposes updates to context & design docs.


## Interoperability & Compatibility {#interoperability--compatibility}

Assistant Config Sync – Scripts convert core context → Copilot / Cursor / Windsurf rules.

Model Context Protocol – Expose .ai via GitMCP endpoint; prioritise .ai over README.

Repo-Sync Tools – Knowhub can sync org-wide .ai templates into new repos.


## Adoption & Migration Guide {#adoption--migration-guide}

For a detailed reference on the commands mentioned below, see Appendix C.

Bootstrap existing repos with ai-migrate, auto-extracting info from README, package manifests.

Iterative Filling – Triage missing keys → prompt owners.

CI Integration – Add ai-validate step to pipeline to ensure .ai completeness.


## Best Practices & Anti-Patterns {#best-practices--anti-patterns}

Keep single source: don’t scatter AI rules outside .ai unless required by external tool paths (use symlinks).

Avoid empty stubs lingering—configure prompts to surface missing context ASAP.

Don’t store sensitive secrets in .ai; reference secure secret stores instead.



## Appendices {#appendices}
### Appendix A — ai-config.json Schema (Draft) {#appendix-a-ai-configjson-schema}

{
  "$schema": "http://json-schema.org/draft/2020-12/schema",
  "title": "AI Config",
  "type": "object",
  "required": ["projectName", "description", "primaryLanguage", "aiPreferences"],
  "properties": {
    "projectName": { "type": "string", "minLength": 1 },
    "description":  { "type": "string" },
    "primaryLanguage": { "type": "string" },
    "frameworks": {
      "type": "array",
      "items": { "type": "string" }
    },
    "license": { "type": "string" },
    "aiPreferences": {
      "type": "object",
      "required": ["styleGuide", "testingFramework", "promptOnMissing"],
      "properties": {
        "styleGuide": { "type": "string" },
        "testingFramework": { "type": "string" },
        "promptOnMissing": { "type": "boolean" }
      }
    }
  }
}


### Appendix B — Glossary {#appendix-b-glossary}

Term

Definition

MCP

Model Context Protocol – specification for real-time retrieval of external context by AI models.

Knowhub

OSS tool for propagating shared config & rules across multiple repos.

ADS

AI Directory Standard (this document).


### Appendix C — CLI Command Reference {#appendix-c-cli-command-reference}

This section details the command-line interface (CLI) tools designed to support the AI Directory Standard.

### ai-init
Purpose: Scaffolds a new /.ai/ directory in a project.

Usage:
```bash
ai-init [options]
```

Behavior: Creates the standard ADS directory structure and populates files with default templates and placeholder content. It can run interactively to ask for key project details.

Options:
| Flag               | Description                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------- |
| --template <name>| Initializes the directory using a predefined template (e.g., web-app, cli, data-science).                  |
| -y, --yes      | Skips all interactive prompts and uses default values. Good for automated scripts.                            |

### ai-migrate
Purpose: Bootstraps a /.ai/ directory in an existing project by inferring context from source files.

Usage:
```bash
ai-migrate --from <sources> [options]
```

Behavior: Scans specified source files (e.g., package.json, README.md) to intelligently populate ai-config.json and project_context.md.

Options:
| Flag            | Description                                                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| --from <list> | Required. A comma-separated list of sources to scan. E.g., readme,package.json,license. Supported sources: readme, license, package.json, pom.xml, pyproject.toml, go.mod. |
| --interactive | Prompts the user to confirm each inferred value before writing it to the target file, allowing for corrections.                              |

### ai-validate
Purpose: Checks the /.ai/ directory for completeness, correctness, and adherence to the standard. Designed for use in CI/CD pipelines.

Usage:
```bash
ai-validate [options]
```

ai-validate looks for `ai-config.schema.json` at the repository root and uses it to verify `.ai/0-ai-config/ai-config.json`. Other JSON Schema tools can load the same file for standalone checks.

Behavior: Runs a series of checks and exits with a non-zero status code if errors are found.

Checks Performed:

Schema Validation: Ensures ai-config.json conforms to `ai-config.schema.json` (also shown in Appendix A).

File Existence: Verifies that all Required files from the standard are present.

Content Completeness: (Optional) Scans files for common placeholder text (e.g., "[TODO]", "[FILL IN]", "...") to identify incomplete sections.

Link Validation: (Optional) Checks that HTTP(S) links in Markdown files are not broken.

Options:
| Flag            | Description                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| --level <level> | Sets the reporting level. error (default): fails on any validation issue. warn: prints issues but always exits successfully. |
| --check-links | Enables the optional (and potentially slow) validation of external links in Markdown files.                  |

### gitmcp
Purpose: Serves the `.ai` directory over HTTP via a simple MCP endpoint.

Usage:
```bash
gitmcp --port 8000
```

The server returns a JSON payload of the `.ai` directory when requesting
`http://localhost:8000/context`. Tools can fetch this endpoint to retrieve
structured project context following the Model Context Protocol.


CLI Installation
The CLI tools can be installed from source using `pip`:

```
pip install .
```

This exposes four commands: `ai-init`, `ai-migrate`, `ai-validate`, and `gitmcp`.

Example Usage
```
# Initialize a new .ai directory
ai-init -y

# Migrate existing project metadata
ai-migrate --from readme,license --interactive

# Validate the directory
ai-validate --level warn

# Serve .ai over MCP
gitmcp --port 8000
```

Run `python -m ai_cli -h` to see all options.
Run `pytest` to execute the unit tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

