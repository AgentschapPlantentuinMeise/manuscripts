SLIDES_MD=slides.md
SLIDES_QMD=slides.qmd
BUILD_DIR=build

all: html quarto

html: $(BUILD_DIR)
	@if [ -f $(SLIDES_MD) ]; then \
	  echo "Building slides from $(SLIDES_MD)..."; \
	  pandoc $(SLIDES_MD) -t revealjs -s -o $(BUILD_DIR)/slides.html \
	    --slide-level=2 --mathjax --bibliography=../manuscript/refs.bib --csl=ieee.csl; \
	else \
	  echo "Skipping HTML build: $(SLIDES_MD) not found."; \
	fi

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

quarto:
	@if [ -f $(SLIDES_QMD) ]; then \
	  echo "Building slides from $(SLIDES_QMD)..."; \
	  quarto render $(SLIDES_QMD) --output-dir $(BUILD_DIR); \
	else \
	  echo "Skipping quarto build: $(SLIDES_QMD) not found."; \
	fi

clean:
	rm -rf $(BUILD_DIR)/*

.PHONY: all html quarto clean
