#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk

pandoc \
	-V lang=spanish \
	-V title="Plan de Empresa: GuifiBaix SCCL" \
	-V documentclass=book \
	-V papersize=a4paper \
	-N --toc -f markdown *.md \
	--template default.latex -o planempresa-content.pdf

pdftk portada.pdf planempresa-content.pdf cat output planempresa.pdf
