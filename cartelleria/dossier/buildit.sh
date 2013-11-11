#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish texlive-fonts-recomended pdftk

pandoc \
	-V lang=spanish \
	-V title-meta='GuifiBaix SCCL: Dossier informatiu' \
	-V documentclass=article \
	-V mainfont='Ubuntu' \
	-V fontsize='11pt,twocolumn,oneside' \
	-V papersize=a4paper \
	-f markdown *.md \
	--template default.latex -o dossier.pdf

#pdftk portada.pdf blank.pdf planempresa-content.pdf cat output planempresa.pdf
