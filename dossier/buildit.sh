#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish texlive-fonts-recomended pdftk

pandoc \
	-V lang=spanish \
	-V title-meta='GuifiBaix SCCL: Dossier informatiu' \
	-V documentclass=article \
	-V mainfont='Ubuntu' \
	-V fontsize='11pt,twocolumn,oneside' \
	-V papersize=a4paper \
	-f markdown \
	00-resumen.md \
	dossier-0.md \
	--template default.latex -o dossier.pdf

pdftk dossier.pdf background ../membrete-a4.pdf output dossier-final.pdf && mv dossier-final.pdf dossier.pdf

