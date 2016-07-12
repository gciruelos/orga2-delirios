IMGS = img/block_structure.pdf img/directorio.pdf img/inodo.pdf

img/%.pdf: img/%.svg
	inkscape --file=$< --export-pdf=$@

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
	rm -f *.pdf
	rm -f img/*.pdf img/*.pdf_tex
