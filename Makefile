# Build the book.
#   make            figures (if any script changed) + PDF
#   make pdf        PDF only
#   make figures    regenerate every figure from scripts/
#   make clean      remove LaTeX build files (keeps the PDF and figures)

PDF     = main.pdf
SCRIPTS = $(wildcard scripts/fig_*.py)

all: figures pdf

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

figures: figures/.stamp

figures/.stamp: $(SCRIPTS) scripts/_style.py
	python3 scripts/make_figures.py
	touch figures/.stamp

clean:
	latexmk -c main.tex
	rm -f chapters/*.aux

.PHONY: all pdf figures clean
