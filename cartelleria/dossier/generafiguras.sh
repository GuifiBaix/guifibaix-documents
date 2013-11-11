#!/bin/bash
# sudo apt-get install inkscape

for a in \
	../../../web/content/media/images/figura-xarxaciutadana-cami.svg \
	../../../web/content/media/images/figura-telefoniaip.svg \
	../../logos/logo-guifibaix.svg \
	; do
	echo '**' Procesando $(basename $a .svg)...
	inkscape $a -A $(basename $a .svg).pdf
done


