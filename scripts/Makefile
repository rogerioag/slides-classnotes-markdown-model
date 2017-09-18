SLIDES := $(patsubst %.md,%.md.slides.pdf,$(wildcard *.md))
HANDOUTS := $(patsubst %.md,%.md.handout.pdf,$(wildcard *.md))
NOTES := $(patsubst %.md,%.md.notes.pdf,$(wildcard *.md))

DEPLOYDIR := ../../pdf

DATADIR   = ..
TEMPLATES = ${DATADIR}/templates/


# Common Options.
COMMOMOPTIONS = --filter pandoc-citeproc --csl=${DATADIR}/csl/apsa.csl --bibliography=ref.bib
COMMOMOPTIONS += --filter ${DATADIR}/filters/columns-filter.py
COMMOMOPTIONS += --filter ${DATADIR}/filters/terminal-filter.py
COMMOMOPTIONS += --filter ${DATADIR}/filters/framebreaks-filter.py
# COMMOMOPTIONS += --filter ${DATADIR}/filters/change-listings-language-to-style.py
COMMOMOPTIONS += --verbose
COMMOMOPTIONS += -f markdown --listings
COMMOMOPTIONS += -V version=2017.01

# Slides Options.
BEAMEROPTIONS = -V lang=pt-br -M lang=pt-br -V babel-lang=brazil
BEAMEROPTIONS += -t beamer --latex-engine=pdflatex
BEAMEROPTIONS += --template=${TEMPLATES}/beamer-rag.template
#BEAMEROPTIONS += --default-image-extension=pdf
BEAMEROPTIONS += -V theme:Madrid
# needs adapted beamer template (see https://github.com/jgm/pandoc-templates/pull/211)
BEAMEROPTIONS += -V themeoptions:numbering=none -V themeoptions:progressbar=foot
# BEAMEROPTIONS += -V fontsize=smaller
BEAMEROPTIONS += --standalone --smart --slide-level=2
# BEAMEROPTIONS += --filter=${PREFIX}/texnotes.py
BEAMEROPTIONS += --include-in-header=${TEMPLATES}/header-beamer.tex
BEAMEROPTIONS += -V toc
BEAMEROPTIONS += --highlight-style=pygments

HANDOUTOPTIONS = -V handout

# Notes options.
PDFOPTIONS = -V lang=brazil -M lang=pt-br -V babel-lang=brazil
PDFOPTIONS += -N --latex-engine=pdflatex
PDFOPTIONS += --template=${TEMPLATES}/latex-rag.template
#PDFOPTIONS += --default-image-extension=pdf
# PDFOPTIONS += -V documentclass=scrartcl -V beamerarticle
PDFOPTIONS += -V fontsize=12pt -V papersize=a4 -V mainfont="Palatino" -V sansfont="Helvetica" -V monofont="Menlo"
PDFOPTIONS += -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:top=2.5cm -V geometry:bottom=2.5cm
PDFOPTIONS += --standalone --smart --number-sections --toc --toc-depth=1
PDFOPTIONS += --include-in-header=${TEMPLATES}/header-latex.tex
PDFOPTIONS += --highlight-style=tango
PDFOPTIONS += -V colorlinks -V linkcolor=headcolor -V citecolor=headcolor -V urlcolor=headcolor
PDFOPTIONS += --toc --toc-depth=2
# PDFOPTIONS += --include-before-body=/dados/rogerio/UTFPR/extensao/projeto-escola-de-computacao-paralela/minicursos/minicurso-computacao-heterogenea-cuda/figuras/banner.tex


all : clean $(SLIDES) $(HANDOUTS) $(NOTES)

%.md.slides.pdf : %.md
	pandoc $^ ${COMMOMOPTIONS} ${BEAMEROPTIONS} -o $@
	evince $@ &

%.md.handout.pdf : %.md
	pandoc $^ ${COMMOMOPTIONS} ${BEAMEROPTIONS} ${HANDOUTOPTIONS} -o $@ 
	pdfnup $@ --nup 1x2 --no-landscape --keepinfo \
		--paper letterpaper --frame true --scale 0.9 \
		--suffix "nup"
	mv $*.md.handout-nup.pdf $@

%.md.notes.pdf : %.md
	pandoc $^ ${COMMOMOPTIONS} ${PDFOPTIONS} -o $@

deploy:
	@echo "Deploying the PDF files in ../../pdf"
	$(shell cp $(SLIDES) $(HANDOUTS) $(NOTES) $(DEPLOYDIR))		

clean : 
	rm -f $(SLIDES)
	rm -f $(HANDOUTS)
	rm -f $(NOTES)
