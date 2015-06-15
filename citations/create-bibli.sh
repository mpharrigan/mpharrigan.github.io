#!/bin/bash
pandoc \
    --bibliography wetmsm.bib \
    --bibliography mdtraj.bib \
    --csl style.csl \
    -o ../research/citations.html \
    cite.in.md
