SLIDES_MD=slides.md
SLIDES_QMD=slides.qmd
BUILD_DIR=build

all: html quarto

html:
    pandoc $(SLIDES_MD) -t revealjs -s -o $(BUILD_DIR)/slides.html \
        --slide-level=2 --mathjax --bibliography=../manuscript/refs.bib --csl=ieee.csl

quarto:
    quarto render $(SLIDES_QMD) --output-dir $(BUILD_DIR)

clean:
    rm -f $(BUILD_DIR)/*

.PHONY: all html quarto clean
