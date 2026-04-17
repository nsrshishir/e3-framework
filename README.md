# The E3 Framework: Effective, Efficient, Elegant

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.19634683-blue)](https://doi.org/10.5281/zenodo.19634683)
[![License: Hybrid](https://img.shields.io/badge/License-Apache--2.0%20%7C%20CC--BY--4.0-blue)](LICENSE)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-e3--evaluator-green)](https://skills.sh/nsrshishir/e3-framework)

> **"Stop manually tweaking hyperparameters. Start programming the researcher."**

The **E3 Framework** is a standardized quality governance protocol for the age of Agentic AI. It provides a mathematically rigorous system for balancing **Effectiveness** (Software Usefulness), **Efficiency** (Logic & Performance), and **Elegance** (Interface & Experience).

This repository is **Agent-Native**: designed for autonomous multi-agent systems (e.g., Gemini CLI, Cursor, Claude Code) to read, implement, and iterate upon software quality with minimal human intervention.

## 🚀 Quick Start (For Agents)

To perform an autonomous E3 evaluation, use the **Skill.sh** registry:

```bash
# 1. Install the E3-Evaluator skill
npx skills add nsrshishir/e3-framework

# 2. Run the scorecard (Python 3.8+)
python3 skills/e3-evaluator/scripts/e3_scorecard.py <your_project_dir>
```

## 📚 Repository Structure

- [**framework/**](framework/): Refined E3 definitions and "E3 Checks" for the 2026 SDLC.
- [**skills/e3-evaluator/**](skills/e3-evaluator/): The agentic skill package, including the Python-based quality scorecard.
- [**paper/**](paper/): Foundational research paper LaTeX sources (Academic Review, Formal Definitions).

## 📊 The "Karpathy Loop" Integration

This framework was developed using the **Autoresearch** (Karpathy Loop) methodology. Every iteration was validated against the **E3 Utility Score ({E3}$)**:

2835U_{E3} = 0.4 \cdot \text{Actionability} + 0.4 \cdot \text{Alignment} + 0.2 \cdot \text{Completeness}2835

### **Latest E3 Evaluation (v1.0.1)**
- **Total E3 Score**: **0.60**
- **Actionability**: **1.00** (Full coverage of agentic E3 checks)
- **Completeness**: **0.00** (Foundational LaTeX docs contain 18 TODOs – *Under construction*)

## 🛡 Intellectual Property & Citation

This framework is the result of formal academic research. If you use it in your research or software, please cite it using the information in [CITATION.cff](CITATION.cff).

**Zenodo Archive**: [10.5281/zenodo.19634683](https://doi.org/10.5281/zenodo.19634683)  
**Academic Preprint**: [Link to arXiv Pending]

---

**Built for the future of software engineering, where humans architect and agents execute.**
