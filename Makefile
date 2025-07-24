# Makefile for compiling scientific paper in multiple formats

PAPER_SRC=manuscript/paper.md
PAPER_INJECTED=manuscript/paper.injected.md
AUTHORS=manuscript/AUTHORS.md
METADATA=metadata.yaml

PDF_OUT=build/paper.pdf
DOCX_OUT=build/paper.docx
LATEX_OUT=build/paper.tex

# Default target
all: inject pdf docx tex

# Step 1: Inject authors into metadata block
inject:
    python inject-authors.py

# Step 2: Build PDF
pdf:
    pandoc $(PAPER_INJECTED) -d $(METADATA) -o $(PDF_OUT)

# Step 3: Build DOCX
docx:
    pandoc $(PAPER_INJECTED) -d $(METADATA) -o $(DOCX_OUT)

# Step 4: Generate raw LaTeX
tex:
    pandoc $(PAPER_INJECTED) -d $(METADATA) -o $(LATEX_OUT)

# Clean build artifacts
clean:
    rm -f $(PDF_OUT) $(DOCX_OUT) $(LATEX_OUT) $(PAPER_INJECTED)

.PHONY: all inject pdf docx tex clean
