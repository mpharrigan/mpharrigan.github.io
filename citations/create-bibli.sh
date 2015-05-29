#!/bin/bash
pandoc --bibliography wetmsm.bib --csl style.csl \
    -o ../research/citations.html \
    cite.in.md
