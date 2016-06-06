IMGS = img/block_structure.pdf

img/%.pdf: img/%.svg
	inkscape -D -z --file=$< --export-pdf=$@ --export-latex

informe: $(IMGS)
	pdflatex informe.tex
	pdflatex informe.tex
	bibtex informe
	pdflatex informe.tex
	pdflatex informe.tex

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.synctex.gz
	rm -f *.out
	rm -f *.xml
	rm -f *.bcf
	rm -f *.blg
	rm -f *.bbl
	rm -f informe-blx.bib
	rm -f *.toc
	rm -f *.pdf img/*.pdf
