#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk


pandoc \
	-f markdown  \
	--template default.latex -o guifibaix-exemple-acord-previ-veins.pdf \
	*md
#	-N --toc \

#pdftk portada.pdf blank.pdf planempresa-content.pdf cat output planempresa.pdf
