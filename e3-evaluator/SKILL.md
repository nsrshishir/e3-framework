---
name: e3-evaluator
description: Evaluate software quality using the E3 Framework (Effective, Efficient, Elegant). Use when performing code reviews, architectural audits, or verifying compliance with E3 standards for both human and agentic software development.
---

# E3 Evaluator

## Overview
The E3 Evaluator skill provides a standardized protocol for assessing software quality based on the three pillars of the E3 framework: Effectiveness ($E_1$), Efficiency ($E_2$), and Elegance ($E_3$).

## Core Workflow

### 1. Perform E3 Scan
Scan the codebase to identify existing E3 protocols and metrics.
- Run `python3 scripts/e3_scorecard.py <dir>` to get a baseline utility score ($U_{E3}$).
- Look for comments or documentation tagged with `E1 Check`, `E2 Check`, or `E3 Check`.

### 2. Pillar-Specific Assessment
Evaluate each pillar against the [metrics](references/metrics.md):

- **Effectiveness ($E_1$)**: Check mission alignment, hallucination rates, and ethical compliance.
- **Efficiency ($E_2$)**: Audit token usage, latency, and carbon intensity.
- **Elegance ($E_3$)**: Review usability, explainability coverage, and format compliance.

### 3. Generate E3 Report
Synthesize findings into an E3 Report.
- **Score**: From the scorecard script.
- **Strengths**: Pillars meeting or exceeding target thresholds.
- **Action Items**: Concrete steps (e.g., "Add E1 Check for Mission Alignment") to improve the score.

## Guidelines
- **Be Quantitative**: Whenever possible, use the formulas defined in the metrics reference.
- **Focus on Actionability**: Every finding should lead to a specific "E3 Check" or refactoring task.
- **2026 Readiness**: Prioritize agentic concerns (A2A communication, MCP protocol, prompt optimization).

## Resources

### scripts/
- `e3_scorecard.py`: Analyzes directory and outputs JSON report of E3 compliance and complexity.

### references/
- `metrics.md`: Comprehensive list of $E_1, E_2, E_3$ metrics, targets, and definitions.
