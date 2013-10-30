#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk

pandoc \
	-V lang=spanish \
	-V title="Plan de Empresa: GuifiBaix SCCL" \
	-V title-meta='Plan de Empresa: GuifiBaix SCCL' \
	-V documentclass=book \
	-V mainfont='Ubuntu' \
	-V fontsize='11pt' \
	-V papersize=a4paper \
	-N --toc -f markdown *.md \
	--template default.latex -o planempresa-content.pdf

pdftk portada.pdf blank.pdf planempresa-content.pdf cat output planempresa.pdf
