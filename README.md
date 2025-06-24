# PRAX - PDF Rendering and Assembly for Exams

> 📄 Fast exam generation from YAML to LaTeX/PDF

---

## Overview

**Exam Generator** is a cross-platform Python tool that quickly converts a simple YAML file describing an exam into a beautifully formatted LaTeX (`.tex`) file or a ready-to-print PDF.  
With a user-friendly graphical interface (GUI), you can select your YAML file, choose output format, and instantly get a professional-looking exam and answer sheet — with your institution's logo and custom metadata.

---

## ✨ Features

- **🖱️ Easy-to-use GUI** — No command-line required. Select files, choose output, done!
- **🔐 Secure Output** — PDF files are generated locally. SHA-256 hash is displayed for integrity.
- **📄 LaTeX & PDF Support** — Output directly to `.tex` for custom edits, or straight to `.pdf`.
- **🎨 Modern Exam Design** — Includes custom logo, clear formatting, and answer sheet.
- **🔄 Fast and Deterministic** — Exam layout is always the same for a given YAML.
- **🛡️ Tested & Reliable** — Includes Pytest test suite and CI workflow.

---

## 🚀 Getting Started

### 1. Requirements

- Python 3.8+
- [PyYAML](https://pyyaml.org/)
- [Tkinter](https://wiki.python.org/moin/TkInter) (usually included with Python)
- LaTeX installation for PDF output (`pdflatex`, e.g. via TeX Live or MikTeX)

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-org/exam-generator.git
cd exam-generator
pip install -r requirements.txt
```

---

## 📥 YAML Exam Format

Here's a sample `exam.yaml`:

```yaml
creator: Jane Doe
id: EXAM-001
title: Physics Exam
subtitle: Mechanics and Thermodynamics
questions:
  - id: 1
    statement: What is the acceleration due to gravity on Earth?
    alternatives:
      A: 9.8 m/s^2
      B: 10 m/s^2
      C: 8.9 m/s^2
      D: 7.8 m/s^2
  - id: 2
    statement: Which law explains the relationship between volume and pressure of a gas at constant temperature?
    alternatives:
      A: Boyle's law
      B: Charles's law
      C: Avogadro's law
      D: Gay-Lussac's law
```

- **Creator**: Author of the exam.
- **ID**: Unique identifier.
- **title**/**subtitle**: Shown at the top of the exam.
- **questions**: List of questions, each with:
  - **id**: Question number.
  - **statement**: The statement of the question.
  - **alternatives**: Dict of answer choices (A, B, C, ...).

---

## 🖥️ Usage

Just run:

```bash
python app.py
```

- **Step 1:** Select your YAML file when prompted.
- **Step 2:** Choose output format: `tex` or `pdf`.
- **Step 3:** Choose an output directory.
- **Step 4:** Collect your `.tex` or `.pdf` file — and, for PDF, see the SHA-256 hash for verification.

> **Note:** For PDF output, make sure `pdflatex` is installed and available in your system PATH.

---

## 🧪 Running Tests

To run all tests:

```bash
pytest
```

All core modules are fully unit-tested.

---

## 🏗️ GitHub Actions CI

This project includes a GitHub Actions workflow (`.github/workflows/test.yml`) that:

- Installs Python and LaTeX (TeX Live)
- Installs dependencies
- Runs the full test suite on every push or pull request

---

## 📝 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
