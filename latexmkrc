# latexmk configuration for the book.
#
# The notes use two font packages (dsfont for the indicator symbol, rsfso for
# the script letters) that a minimal TeX Live lacks. Copies in TDS layout live
# in texmf/ so the book builds anywhere; on a full MacTeX install the system
# copies are found first and these are ignored.

$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -synctex=1 %O %S';

ensure_path('TEXINPUTS',   './texmf/tex//');
ensure_path('TFMFONTS',    './texmf/fonts/tfm//');
ensure_path('T1FONTS',     './texmf/fonts/type1//');
ensure_path('VFFONTS',     './texmf/fonts/vf//');
ensure_path('TEXFONTMAPS', './texmf/fonts/map//');

$clean_ext = 'synctex.gz run.xml solutions.tex';   # main.solutions.tex is written by the answers package
