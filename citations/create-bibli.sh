#!/bin/bash
pandoc \
    --bibliography wetmsm.bib \
    --bibliography mdtraj.bib \
    --bibliography mdtraj.nmeth.ris \
    --csl style.csl \
    -o ../research/citations.html \
    cite.in.md
