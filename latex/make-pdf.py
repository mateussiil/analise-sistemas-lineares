import numpy as np

from pylatex import Document, Head, Figure, PageStyle, Command, Center, Section, NewLine, Matrix, Subsection, Math, Alignat,TikZ
from pylatex.utils import italic, NoEscape
import os
# from PyPDF2 import PdfFileReader, PdfFileMerger


faculdade= 'Universidade Federal do Maranhão'
coordenacao = 'Coordenação do Curso de Engenharia da Computação'

# files_dir = os.getcwd()
# pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
# merger = PdfFileMerger()

def header(doc):
    with doc.create(Figure(position="h!")) as brasao_pic:
        brasao_pic.add_image(brasao_filename, width='70px')

    with doc.create(Center()) as center:
        center.append(NoEscape(r'{\large \rm \textbf {Universidade Federal do Maranhão} \linebreak}'))
        center.append(NoEscape(r'{\large \rm \textbf {Coordenação do Curso de Engenharia da Computação} \linebreak}'))

if __name__ == '__main__':
    brasao_filename = os.path.join(os.path.join(os.getcwd(),"imagens"), 'ufma.png')
    margins = {"tmargin": "20mm", "bmargin":"20mm", "lmargin":"25mm", "rmargin":"25mm"}

    # Basic document
    doc = Document('Teste', geometry_options=margins)

    doc.documentclass = Command(        
        'documentclass',
        options=['a4paper','12pt', 'twoside'],
        arguments=['article']
    )

    header(doc)

    a = np.array([[100, 10, 20]]).T
    M = np.matrix([[2, 3, 4],
                   [0, 0, 1],
                   [0, 0, 2]])

    with doc.create(Section('The fancy stuff')):
        with doc.create(Subsection('Correct matrix equations')):
            doc.append(Math(data=[Matrix(M), Matrix(a), '=', Matrix(M * a)]))

        with doc.create(Subsection('Alignat math environment')):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\frac{a}{b} &= 0 \\')
                agn.extend([Matrix(M), Matrix(a), '&=', Matrix(M * a)])

    doc.append(NoEscape(r'$\int_{a}^{b} x^2 \,dx$'))
    
       
    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()

    # for filename in pdf_files:
    #     merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))

    # merger.write(os.path.join(files_dir, "merged_full.pdf"))
    