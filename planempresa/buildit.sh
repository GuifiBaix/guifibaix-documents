#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish

pandoc -V lang=spanish -N --toc -f markdown *.md -o planempresa.pdf
