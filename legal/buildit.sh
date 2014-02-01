#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk

pandoc \
	-V lang=spanish \
	-V title-meta='Contrato de servicios: GuifiBaix SCCL' \
	-V documentclass=article \
	-V mainfont='Ubuntu' \
	-V fontsize='12pt' \
	-V papersize=a4paper \
	-f markdown *.md \
	--template default.latex -o contrato-servicio.pdf
#	-N --toc \

#pdftk portada.pdf blank.pdf planempresa-content.pdf cat output planempresa.pdf
