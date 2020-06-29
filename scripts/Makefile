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
# FILTEROPTIONS += --biblatex
FILTEROPTIONS += --filter ${DATADIR}/filters/columns-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/terminal-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/framebreaks-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/appendix-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/exampleblock-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/hideonbeamer-with-space-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/background-filter.py
# FILTEROPTIONS += --filter ${DATADIR}/filters/hide-on-beamer-without-space-filter.py
# COMMOM_OPTIONS += --filter ${DATADIR}/filters/change-listings-language-to-style.py

# Common Options.
COMMOM_OPTIONS += --verbose
COMMOM_OPTIONS += -f markdown
COMMOM_OPTIONS += --listings
#COMMOM_OPTIONS += --pdf-engine=pdflatex --pdf-engine-opt=""
COMMOM_OPTIONS += --variable=version:2020.01

# Slides Options.
# SLIDES_OPTIONS = -V lang=pt-br -M lang=pt-br -V babel-lang=brazil
SLIDES_OPTIONS = -t beamer 
SLIDES_OPTIONS += --template=${TEMPLATES}/beamer-slides-template.tex
SLIDES_OPTIONS += --include-in-header=${TEMPLATES}/beamer-header.tex
#SLIDES_OPTIONS += --default-image-extension=pdf
SLIDES_OPTIONS += --variable=lang:pt-br --variable=babel-lang:brazil
SLIDES_OPTIONS += --standalone --slide-level=2
# SLIDES_OPTIONS += -V theme:Madrid
SLIDES_OPTIONS += --toc
# needs adapted beamer template (see https://github.com/jgm/pandoc-templates/pull/211)
SLIDES_OPTIONS += -V themeoptions:numbering=none -V themeoptions:progressbar=foot
SLIDES_OPTIONS += --highlight-style=pygments
# SLIDES_OPTIONS += -V fontsize=smaller
# SLIDES_OPTIONS += --filter=${PREFIX}/texnotes.py

# Handouts options.
HANDOUTOPTIONS = -V handout

# Notes options.
CLASSNOTES_OPTIONS = --template=${TEMPLATES}/latex-classnotes-template.tex
CLASSNOTES_OPTIONS += --include-in-header=${TEMPLATES}/latex-header.tex
# CLASSNOTES_OPTIONS += -N --latex-engine=pdflatex
CLASSNOTES_OPTIONS += --variable=lang:brazil --variable=babel-lang:brazil
CLASSNOTES_OPTIONS += --standalone 
CLASSNOTES_OPTIONS += --toc --toc-depth=2
#CLASSNOTES_OPTIONS += --default-image-extension=pdf
# CLASSNOTES_OPTIONS += -V documentclass=scrartcl -V beamerarticle
CLASSNOTES_OPTIONS += --number-sections --toc --toc-depth=1
CLASSNOTES_OPTIONS += -V geometry:left=2.0cm -V geometry:right=2.0cm -V geometry:top=2.0cm -V geometry:bottom=2.0cm -V geometry:margin=2.0cm
CLASSNOTES_OPTIONS += -V fontsize=12pt -V papersize=a4 -V mainfont="Palatino" -V sansfont="Helvetica" -V monofont="Menlo"
CLASSNOTES_OPTIONS += --highlight-style=tango
CLASSNOTES_OPTIONS += -V colorlinks -V linkcolor=headcolor -V citecolor=headcolor -V urlcolor=headcolor

# CLASSNOTES_OPTIONS += --include-before-body=/dados/rogerio/UTFPR/extensao/projeto-escola-de-computacao-paralela/minicursos/minicurso-computacao-heterogenea-cuda/figuras/banner.tex

default:
	@echo Executando make em paralelo [$(shell nproc) tarefas]
	@make -s -j $(shell nproc) all

all : clean slides-metropolis hangouts notes

# COMMOM_OPTIONS += --pdf-engine=pdflatex --pdf-engine-opt=""
# SLIDES_OPTIONS += -V theme:Madrid
config-madrid:
	$(eval COMMOM_OPTIONS += $(shell echo '--pdf-engine=pdflatex --pdf-engine-opt=""'))
	$(eval SLIDES_OPTIONS += $(shell echo '-V theme:Madrid'))
	
#COMMOM_OPTIONS += --pdf-engine=xelatex
#SLIDES_OPTIONS += -V theme:metropolis
# $(eval COMMOM_OPTIONS += $(shell echo '--pdf-engine=xelatex --pdf-engine-opt=""'))
config-metropolis:
	$(eval COMMOM_OPTIONS += $(shell echo '--pdf-engine=tectonic'))
	$(eval SLIDES_OPTIONS += $(shell echo '-V theme:metropolis'))

slides-madrid: clean config-madrid $(SLIDES)

slides-metropolis: clean config-metropolis $(SLIDES) 

hangouts: $(HANDOUTS) 

notes: $(NOTES)

%.md.slides.pdf : %.md
	pandoc $^ ${COMMOM_OPTIONS} ${SLIDES_OPTIONS} ${FILTEROPTIONS} -o $@
	evince $@ &

%.md.handout.pdf : %.md
	pandoc $^ ${COMMOM_OPTIONS} ${SLIDES_OPTIONS} ${FILTEROPTIONS} ${HANDOUTOPTIONS} -o $@ 
	pdfnup $@ --nup 1x2 --no-landscape --keepinfo \
		--paper letterpaper --frame true --scale 0.9 \
		--suffix "nup"
	mv $*.md.handout-nup.pdf $@

%.md.notes.pdf : %.md
	pandoc $^ ${COMMOM_OPTIONS} ${CLASSNOTES_OPTIONS} ${FILTEROPTIONS} -o $@

deploy:
	@echo "Deploying the PDF files in ../../pdf"
	$(shell cp $(SLIDES) $(HANDOUTS) $(NOTES) $(DEPLOYDIR))		

clean: 
	rm -f $(SLIDES)
	rm -f $(HANDOUTS)
	rm -f $(NOTES)
	rm *~ *.aux *.dvi *.bbl *.blg *.log *.lot *.lof *.toc *.out *.nav *.snm *.vrb main.pdf main.synctex.gz


