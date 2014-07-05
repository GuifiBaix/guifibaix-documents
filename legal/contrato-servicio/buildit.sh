#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk


python3 omple.py $1 < *.md | 
pandoc \
	--template default.latex \
	-o guifibaix-contrato-mantenimiento-y-servicio.pdf


