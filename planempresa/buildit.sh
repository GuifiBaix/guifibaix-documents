#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk

pandoc \
	-V lang=spanish \
	-V title-meta='Plan de Empresa: GuifiBaix SCCL' \
	-V documentclass=book \
	-V mainfont='Ubuntu' \
	-V fontsize='12pt' \
	-V papersize=a4paper \
	-N --toc \
	--include-before-body license.tex \
	-f markdown *.md \
	--template default.latex -o planempresa-content.pdf

pdftk portada.pdf blank.pdf planempresa-content.pdf cat output planempresa.pdf
