SLIDES := $(patsubst %.md,%.md.slides.pdf,$(wildcard *.md))
HANDOUTS := $(patsubst %.md,%.md.handout.pdf,$(wildcard *.md))
NOTES := $(patsubst %.md,%.md.notes.pdf,$(wildcard *.md))

DEPLOYDIR := ../../pdf

DATADIR   = ..
TEMPLATES = ${DATADIR}/templates

# pandoc aoc-aula-001-apresentacao-introducao.md --filter pandoc-citeproc --csl ../csl/apsa.csl --bibliography ref.bib 
# --filter ../filters/columns-filter.py --filter ../filters/terminal-filter.py --filter 
# ../filters/framebreaks-filter.py --verbose -f markdown --listings --variable=version:2020.01 
# --variable=lang:pt-br -t beamer --pdf-engine=pdflatex --template=../templates/beamer-rag.template --variable=theme:Madrid --variable=themeoptions:numbering=none --variable=themeoptions:progressbar=foot --standalone --slide-level=2 --include-in-header=../templates/header-beamer.tex 
# -V toc --highlight-style=pygments -o aoc-aula-001-apresentacao-introducao.md.slides.pdf

#Filters
FILTEROPTIONS = --filter pandoc-citeproc --csl=${DATADIR}/csl/apsa.csl --bibliography=ref.bib
FILTEROPTIONS += --filter ${DATADIR}/filters/columns-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/terminal-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/framebreaks-filter.py
# FILTEROPTIONS += --filter ${DATADIR}/filters/hide-on-beamer-with-space-filter.py
# FILTEROPTIONS += --filter ${DATADIR}/filters/hide-on-beamer-without-space-filter.py
# COMMOMOPTIONS += --filter ${DATADIR}/filters/change-listings-language-to-style.py

# Common Options.
COMMOMOPTIONS += --verbose
COMMOMOPTIONS += -f markdown
COMMOMOPTIONS += --listings
COMMOMOPTIONS += --pdf-engine=pdflatex --pdf-engine-opt=""
COMMOMOPTIONS += --variable=version:2020.01

# Slides Options.
# BEAMEROPTIONS = -V lang=pt-br -M lang=pt-br -V babel-lang=brazil
BEAMEROPTIONS = -t beamer 
BEAMEROPTIONS += --template=${TEMPLATES}/beamer-rag.template
BEAMEROPTIONS += --include-in-header=${TEMPLATES}/header-beamer.tex
#BEAMEROPTIONS += --default-image-extension=pdf
BEAMEROPTIONS += --variable=lang:pt-br --variable=babel-lang:brazil
BEAMEROPTIONS += --standalone --slide-level=2
BEAMEROPTIONS += -V theme:Madrid
BEAMEROPTIONS += --toc
# needs adapted beamer template (see https://github.com/jgm/pandoc-templates/pull/211)
BEAMEROPTIONS += -V themeoptions:numbering=none -V themeoptions:progressbar=foot
BEAMEROPTIONS += --highlight-style=pygments
# BEAMEROPTIONS += -V fontsize=smaller
# BEAMEROPTIONS += --filter=${PREFIX}/texnotes.py

# Handouts options.
HANDOUTOPTIONS = -V handout

# Notes options.
PDFOPTIONS = --template=${TEMPLATES}/latex-rag.template
PDFOPTIONS += --include-in-header=${TEMPLATES}/header-latex.tex
# PDFOPTIONS += -N --latex-engine=pdflatex
PDFOPTIONS += --variable=lang:brazil --variable=babel-lang:brazil
PDFOPTIONS += --standalone 
PDFOPTIONS += --toc --toc-depth=2
#PDFOPTIONS += --default-image-extension=pdf
# PDFOPTIONS += -V documentclass=scrartcl -V beamerarticle
PDFOPTIONS += --number-sections --toc --toc-depth=1
PDFOPTIONS += -V geometry:left=2.0cm -V geometry:right=2.0cm -V geometry:top=2.0cm -V geometry:bottom=2.0cm -V geometry:margin=2.0cm
PDFOPTIONS += -V fontsize=12pt -V papersize=a4 -V mainfont="Palatino" -V sansfont="Helvetica" -V monofont="Menlo"
PDFOPTIONS += --highlight-style=tango
PDFOPTIONS += -V colorlinks -V linkcolor=headcolor -V citecolor=headcolor -V urlcolor=headcolor

# PDFOPTIONS += --include-before-body=/dados/rogerio/UTFPR/extensao/projeto-escola-de-computacao-paralela/minicursos/minicurso-computacao-heterogenea-cuda/figuras/banner.tex


all : clean $(SLIDES) $(HANDOUTS) $(NOTES)

%.md.slides.pdf : %.md
	pandoc $^ ${COMMOMOPTIONS} ${BEAMEROPTIONS} ${FILTEROPTIONS} -o $@
	evince $@ &

%.md.handout.pdf : %.md
	pandoc $^ ${COMMOMOPTIONS} ${BEAMEROPTIONS} ${FILTEROPTIONS} ${HANDOUTOPTIONS} -o $@ 
	pdfnup $@ --nup 1x2 --no-landscape --keepinfo \
		--paper letterpaper --frame true --scale 0.9 \
		--suffix "nup"
	mv $*.md.handout-nup.pdf $@

%.md.notes.pdf : %.md
	pandoc $^ ${COMMOMOPTIONS} ${PDFOPTIONS} ${FILTEROPTIONS} -o $@

deploy:
	@echo "Deploying the PDF files in ../../pdf"
	$(shell cp $(SLIDES) $(HANDOUTS) $(NOTES) $(DEPLOYDIR))		

clean : 
	rm -f $(SLIDES)
	rm -f $(HANDOUTS)
	rm -f $(NOTES)
