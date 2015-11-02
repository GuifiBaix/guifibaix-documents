@echo off

C:\Python34\python.exe generaContrato.py --md b2b/input-neutro.yaml -d 2015-10-20 > temp.md

"C:\Program Files (x86)\GnuWin32\bin\iconv.exe" -f CP1252 -t UTF-8 temp.md > temp2.md

pandoc.exe -V lang=spanish -V title-meta="Contrato de servicios: GuifiBaix SCCL" -V documentclass=article -V mainfont='Ubuntu' -V fontsize='12pt' -V papersize=a4paper -f markdown --template default.latex -o guifibaix-contrato-mantenimiento-y-servicio.tex temp2.md

"C:\Program Files\MiKTeX 2.9\miktex\bin\x64\pdflatex.exe" -interaction=nonstopmode guifibaix-contrato-mantenimiento-y-servicio.tex

del *.out
del *.log
del *.aux
del temp.md
del temp2.md
del guifibaix-contrato-mantenimiento-y-servicio.tex



pause

