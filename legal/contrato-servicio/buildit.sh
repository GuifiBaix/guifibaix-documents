#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk


python3 omple.py < *.md | 
pandoc \
	-V lang=spanish \
	-V mainfont='Ubuntu' \
	-V fontsize='11pt' \
	-V papersize=a4paper \
	-f markdown  \
	--template default.latex -o guifibaix-contrato-mantenimiento-y-servicio.pdf
#	-V documentclass=article \
#	-N --toc \
#	*md
#	-V title-meta='Contrato de servicios: GuifiBaix SCCL' \

#pdftk portada.pdf blank.pdf planempresa-content.pdf cat output planempresa.pdf
