# Scientific Paper Template

[![Build
Paper](https://github.com/AgentschapPlantentuinMeise/manuscripts/actions/workflows/build-paper.yml/badge.svg?branch=main)](https://github.com/AgentschapPlantentuinMeise/manuscripts/actions/workflows/build-paper.yml)

A modular, Git-tracked scientific writing workflow using Markdown, Pandoc, and automated Makefile compilation.

## 🛠️ Features

- Write the manuscript in lightweight Markdown (`paper.md`)
- Use a modular `AUTHORS.md` for author contributions
- Format control via `metadata.yaml`
- Output to multiple formats: PDF, DOCX, and LaTeX
- Automatic injection of author metadata using a preprocessing script
- Easy build automation with Makefile

## 🗂️ Project Structure

```text
your-paper/
├── manuscript/
│   ├── paper.md            # Main manuscript in Markdown
│   ├── AUTHORS.md          # Author list and contributions
│   ├── refs.bib            # BibTeX bibliography
├── presentation/
│   ├── slides.md           # Markdown-based presentation
│   ├── slides.qmd          # Quarto format (optional)
│   ├── Makefile            # Build slides into HTML/PDF
│   └── build/              # Compiled outputs
├── shared/
│   ├── figures/            # Reusable diagrams and plots
│   └── data/               # Reusable data (raw/processed)
├── metadata.yaml           # Document styling and layout
├── inject-authors.py       # Preprocessor script
├── Makefile                # Build automation
├── build/                  # Compiled outputs (ignored by Git)
├── scripts/                # Code used for analysis or figure generation
│   ├── generate_figures.py
│   ├── stats.R
├── .gitignore              # Clean up your repo
├── LICENSE                 # Usage rights
├── CITATION.cff            # Citation metadata
└── README.md               # Project overview and instructions
```

## 🔧 Requirements

- [Pandoc](https://pandoc.org)
- [pandoc-include](https://github.com/DCsunset/pandoc-include)

    pip install pandoc-include

## 🚀 Build Instructions

Run the following from the repository root:

```bash
make            # Compiles PDF, DOCX, and LaTeX
make pdf        # Compiles PDF only
make docx       # Compiles DOCX only
make tex        # Generates LaTeX file only
make clean      # Cleans build artifacts
```

🧑‍🤝‍🧑 Contributions
See manuscript/AUTHORS.md for author roles and ORCID IDs.

📜 Citation
Please cite this work using the details in CITATION.cff.

🔓 License
Licensed under Creative Commons Attribution 4.0.

