#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish

pandoc \
	-V lang=spanish \
	-V title="Plan de Empresa: GuifiBaix SCCL" \
	-V documentclass=book \
	-N --toc -f markdown *.md --template default.latex -o planempresa.pdf
