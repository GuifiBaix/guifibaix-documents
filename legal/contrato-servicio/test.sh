#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk

fail()
{
	echo TEST FAILED: $* && exit -1
}

for input in b2b/input*yaml; do
	output=$(echo $input | sed s/input/output/ | sed 's/\.yaml$/.md/' )
	echo Generating $input '->' $output
	gb_generacontratoservicio.py --md $input -d 2014-02-20 > $output || fail Command returned an error
done

false && (
echo Generating b2b/input-eva.yaml '->' b2b/output-eva.tex
	python3 generaContrato.py \
		b2b/input-eva.yaml \
		-d 2014-02-20 \
		-o b2b/output-eva.tex ||
		fail Command returned an error
	)
git diff --exit-code b2b && echo TEST OK || echo FAILED!!!!!!!!

