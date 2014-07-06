#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk

fail()
{
	echo TEST FAILED: $* && exit -1
}

for input in b2b/omple-input*yaml; do
	output=$(echo $input | sed s/input/output/ | sed 's/\.yaml$/.md/' )
	echo Generating $input '->' $output
	python3 generaContracte.py --md $input -d 2014-02-20 > $output || fail Command returned an error
done

echo Generating b2b/omple-output-eva.tex '->' b2b/pandoc-output.tex
	python3 generaContracte.py \
		b2b/omple-input-eva.yaml \
		-d 2014-02-20 \
		-o b2b/pandoc-output.tex ||
		fail Command returned an error

git diff --exit-code b2b && echo TEST OK || echo FAILED!!!!!!!!

