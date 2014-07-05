#!/bin/bash
# sudo apt-get install pandoc texlive-lang-spanish pdftk

fail()
{
	echo TEST FAILED: $* && exit -1
}

for input in b2b/omple-input*yaml; do
	output=$(echo $input | sed s/input/output/ | sed 's/\.yaml$/.tex/' )
	echo Generating $input '->' $output
	cat *md | python3 omple.py $input > $output || fail Command returned an error
done && git diff --exit-code b2b && echo TEST OK || echo FAILED!!!!!!!!


