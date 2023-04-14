SLIDES := $(patsubst %.md,%.md.slides.pdf,$(wildcard *.md))
HANDOUTS := $(patsubst %.md,%.md.handout.pdf,$(wildcard *.md))
NOTES := $(patsubst %.md,%.md.notes.pdf,$(wildcard *.md))
WORDCLOUD := $(patsubst %.md,%.md.wordcloud.png,$(wildcard *.md))
ARTICLE := $(patsubst %.md,%.md.article.pdf,$(wildcard *.md))

CLASSNAME=$(shell basename $(CURDIR))
DEPLOYDIR := ../../pdf

DATADIR   = ..
TEMPLATES = ${DATADIR}/templates

PANDOC=/usr/bin/pandoc

# pandoc aoc-aula-001-apresentacao-introducao.md --filter pandoc-citeproc --csl ../csl/apsa.csl --bibliography ref.bib 
# --filter ../filters/columns-filter.py --filter ../filters/terminal-filter.py --filter 
# ../filters/framebreaks-filter.py --verbose -f markdown --listings --variable=version:2020.01 
# --variable=lang:pt-br -t beamer --pdf-engine=pdflatex --template=../templates/beamer-rag.template --variable=theme:Madrid --variable=themeoptions:numbering=none --variable=themeoptions:progressbar=foot --standalone --slide-level=2 --include-in-header=../templates/header-beamer.tex 
# -V toc --highlight-style=pygments -o aoc-aula-001-apresentacao-introducao.md.slides.pdf

#Filters
# FILTEROPTIONS = --filter pandoc-citeproc --csl=${DATADIR}/csl/apsa.csl --bibliography=ref.bib
# FILTEROPTIONS = --citeproc --bibliography=ref.bib --csl=${DATADIR}/csl/apsa.csl
# FILTEROPTIONS += --biblatex
FILTEROPTIONS = --filter ${DATADIR}/filters/pandoc_run_filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/columns-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/terminal-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/framebreaks-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/appendix-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/exampleblock-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/hideonbeamer-with-space-filter.py
FILTEROPTIONS += --filter ${DATADIR}/filters/background-filter.py
# FILTEROPTIONS += --filter pandoc-xnos
FILTEROPTIONS += --filter pandoc-crossref
FILTEROPTIONS += --citeproc --bibliography=ref.bib --csl=${DATADIR}/csl/apsa.csl

# FILTEROPTIONS += --filter ${DATADIR}/filters/hide-on-beamer-without-space-filter.py
# COMMOM_OPTIONS += --filter ${DATADIR}/filters/change-listings-language-to-style.py

# Common Options.
COMMOM_OPTIONS += +RTS -K512m -RTS
COMMOM_OPTIONS += --verbose
COMMOM_OPTIONS += -f markdown
# COMMOM_OPTIONS += --listings
#COMMOM_OPTIONS += --pdf-engine=pdflatex --pdf-engine-opt=""
COMMOM_OPTIONS += --variable=version:2023.01
COMMOM_OPTIONS += --metadata-file ${TEMPLATES}/model-metadata.yml --metadata-file ../../../course-metadata.yml
# COMMOM_OPTIONS += --highlight-style ${TEMPLATES}/mycode.theme 
# COMMOM_OPTIONS += --syntax-definition=${TEMPLATES}/c.xml

# Slides Options.
# SLIDES_OPTIONS = -V lang=pt-br -M lang=pt-br -V babel-lang=brazil
SLIDES_OPTIONS = -t beamer 
SLIDES_OPTIONS += --template=${TEMPLATES}/beamer-slides-template.tex
SLIDES_OPTIONS += --include-in-header=${TEMPLATES}/beamer-header.tex
#SLIDES_OPTIONS += --default-image-extension=pdf
SLIDES_OPTIONS += --variable=lang:pt-br --variable=babel-lang:pt-BR
SLIDES_OPTIONS += --standalone --slide-level=2
# SLIDES_OPTIONS += -V theme:Madrid
# SLIDES_OPTIONS += -V aspectratio=169
SLIDES_OPTIONS += --toc -V toc-title:Agenda
# needs adapted beamer template (see https://github.com/jgm/pandoc-templates/pull/211)
SLIDES_OPTIONS += -V themeoptions:numbering=none -V themeoptions:progressbar=foot
SLIDES_OPTIONS += --highlight-style=pygments
# SLIDES_OPTIONS += -V fontsize=smaller
# SLIDES_OPTIONS += --filter=${PREFIX}/texnotes.py

# Handouts options.
HANDOUTOPTIONS = -V handout

# Notes options.
CLASSNOTES_OPTIONS = -t latex
CLASSNOTES_OPTIONS += --template=${TEMPLATES}/latex-classnotes-template.tex
CLASSNOTES_OPTIONS += --include-in-header=${TEMPLATES}/latex-header.tex
# CLASSNOTES_OPTIONS += -N --latex-engine=pdflatex
CLASSNOTES_OPTIONS += --variable=lang:pt-BR --variable=babel-lang:portugues
CLASSNOTES_OPTIONS += --standalone 
# CLASSNOTES_OPTIONS += --toc --toc-depth=2
# CLASSNOTES_OPTIONS += --default-image-extension=pdf
# CLASSNOTES_OPTIONS += -V documentclass=scrartcl -V beamerarticle
CLASSNOTES_OPTIONS += --number-sections --toc --toc-depth=1 -V toc-title:Sumário
CLASSNOTES_OPTIONS += -V geometry:left=2.0cm -V geometry:right=2.0cm -V geometry:top=2.0cm -V geometry:bottom=2.0cm -V geometry:margin=2.0cm
CLASSNOTES_OPTIONS += -V fontsize=12pt -V papersize=a4  
# CLASSNOTES_OPTIONS += -V mainfont="Palatino" -V sansfont="Helvetica" -V monofont="Menlo"
CLASSNOTES_OPTIONS += --listings
CLASSNOTES_OPTIONS += --highlight-style=tango
CLASSNOTES_OPTIONS += -V colorlinks -V linkcolor=headcolor -V citecolor=headcolor -V urlcolor=headcolor

# CLASSNOTES_OPTIONS += --include-before-body=/dados/rogerio/UTFPR/extensao/projeto-escola-de-computacao-paralela/minicursos/minicurso-computacao-heterogenea-cuda/figuras/banner.tex

# Article options.
# Notes options.
ARTICLE_OPTIONS = --template ${TEMPLATES}/svm-latex-ms.tex
ARTICLE_OPTIONS += --include-in-header ${TEMPLATES}/article-header.tex
ARTICLE_OPTIONS += --pdf-engine pdflatex
ARTICLE_OPTIONS += --variable=lang:brazil --variable=babel-lang:brazil -V lang=brazil
ARTICLE_OPTIONS += --standalone --self-contained 
ARTICLE_OPTIONS += --number-sections
ARTICLE_OPTIONS += --listings
ARTICLE_OPTIONS += --highlight-style tango

ARTICLE_OPTIONS += --toc --toc-depth=2 -V toc-title="Sumário"

ARTICLE_OPTIONS += -V fontsize=12pt

ARTICLE_OPTIONS += -V colorlinks -V linkcolor=headcolor -V citecolor=headcolor -V urlcolor=headcolor

#ARTICLE_OPTIONS += --lua-filter /home/rag/R/x86_64-pc-linux-gnu-library/3.6/rmarkdown/rmarkdown/lua/pagebreak.lua

#ARTICLE_OPTIONS += --lua-filter /home/rag/R/x86_64-pc-linux-gnu-library/3.6/rmarkdown/rmarkdown/lua/latex-div.lua 


default:
	@echo Executando make em paralelo [$(shell nproc) tarefas]
	@make -s -j $(shell nproc) all

all : wordcloud slides-metropolis handouts notes article

# COMMOM_OPTIONS += --pdf-engine=pdflatex --pdf-engine-opt=""
# SLIDES_OPTIONS += -V theme:Madrid
config-madrid:
	$(eval COMMOM_OPTIONS += $(shell echo '--pdf-engine=pdflatex --pdf-engine-opt=""'))
	$(eval SLIDES_OPTIONS += $(shell echo '-V theme:Madrid'))
	
#COMMOM_OPTIONS += --pdf-engine=xelatex
#SLIDES_OPTIONS += -V theme:metropolis
# $(eval COMMOM_OPTIONS += $(shell echo '--pdf-engine=xelatex --pdf-engine-opt=""'))
config-metropolis:
	$(eval COMMOM_OPTIONS += $(shell echo '--pdf-engine=xelatex'))
	$(eval SLIDES_OPTIONS += $(shell echo '-V theme:metropolis'))

config-notes:
	$(eval COMMOM_OPTIONS += $(shell echo '--pdf-engine=xelatex'))

config-article:
	$(eval COMMOM_OPTIONS += $(shell echo '--pdf-engine pdflatex'))

slides-madrid: config-madrid $(SLIDES)

slides-metropolis: config-metropolis $(SLIDES) wordcloud

handouts: config-metropolis $(HANDOUTS) wordcloud

notes: config-notes $(NOTES) wordcloud

wordcloud: $(WORDCLOUD)

article: config-article $(ARTICLE) wordcloud

%.md.slides.pdf : %.md
	${PANDOC} $^ ${COMMOM_OPTIONS} ${SLIDES_OPTIONS} ${FILTEROPTIONS} -o $@
	okular $@ &

%.md.handout.pdf : %.md
	${PANDOC} $^ ${COMMOM_OPTIONS} ${SLIDES_OPTIONS} ${FILTEROPTIONS} ${HANDOUTOPTIONS} -o $@ 
	pdfjam $@ --nup 1x2 --no-landscape --keepinfo \
		--paper letterpaper --frame true --scale 0.9 \
		--suffix "nup"
	mv $*.md.handout-nup.pdf $@

%.md.notes.pdf : %.md
	${PANDOC} $^ ${COMMOM_OPTIONS} ${CLASSNOTES_OPTIONS} ${FILTEROPTIONS} -o $@

%.md.article.pdf : %.md
	${PANDOC} $^ ${COMMOM_OPTIONS} ${ARTICLE_OPTIONS} ${FILTEROPTIONS} -o $@

deploy:
	@echo "Deploying the PDF files in ../../pdf"
	$(shell mkdir -p $(DEPLOYDIR))
	$(shell cp $(SLIDES) $(HANDOUTS) $(NOTES) $(DEPLOYDIR))
	@echo "Compressing src files..."
	zip -T -r $(CLASSNAME)-cod.zip src
	@echo "Deploying the COD files in ../../pdf"
	cp $(CLASSNAME)-cod.zip $(DEPLOYDIR)

clean: 
	rm -f $(SLIDES)
	rm -f $(HANDOUTS)
	rm -f $(NOTES)
	rm -f $(ARTICLE)
	rm *~ *.aux *.dvi *.bbl *.blg *.log *.lot *.lof *.toc *.out *.nav *.snm *.vrb main.pdf main.synctex.gz 
	rm figuras/*.md.wordcloud.png

%.md.wordcloud.png: %.md
	rm -f figuras/$@
	python ${HOME}/Documentos/wordcloud/generate-word-cloud.py --max 1000 --width 666 --height 500 $^ -o figuras/$@
