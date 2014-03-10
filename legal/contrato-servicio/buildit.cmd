@echo off

C:\Python27\python.exe omple.py *.md > temp.md

C:\Python27\pandoc.exe -V lang=spanish -V title-meta="Contrato de servicios: GuifiBaix SCCL" -V documentclass=article -V mainfont='Ubuntu' -V fontsize='12pt' -V papersize=a4paper -f markdown --template default.latex -o guifibaix-contrato-mantenimiento-y-servicio.tex temp.md

"C:\Program Files (x86)\MiKTeX 2.9\miktex\bin\pdflatex.exe" -interaction=nonstopmode guifibaix-contrato-mantenimiento-y-servicio.tex

del *.out
del *.log
del *.aux
del temp.md


