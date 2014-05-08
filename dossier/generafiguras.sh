#!/bin/bash
# sudo apt-get install inkscape texlive-extra-utils

for a in \
	../../web/content/media/images/figura-xarxaciutadana-cami.svg \
	../../web/content/media/images/figura-telefoniaip.svg \
	../cartelleria/lamines/internet-sharing.svg \
	../logos/logo-guifibaix.svg \
	; do
	echo '**' Procesando $(basename $a .svg)...
	inkscape $a -A $(basename $a .svg).pdf
done

libreoffice --headless --convert-to pdf tabla-preciostelefoniaip.odg
pdfcrop tabla-preciostelefoniaip.pdf tabla-preciostelefoniaip.pdf

