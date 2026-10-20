"""Package the current graphical-abstract artwork for LaTeX.

The illustration is generated artwork, not a vector drawing. Preserve it
unchanged when embedding. The exact generation/refinement prompts are in
introduction-graphical-abstract-prompts.txt. The dashboard traces and community
are schematic and contain no experimental measurements.
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

HERE = Path(__file__).resolve().parent

def build():
    image = ImageReader(str(HERE / 'introduction-graphical-abstract-artwork.png'))
    width, height = image.getSize()
    doc = canvas.Canvas(str(HERE / 'introduction-graphical-abstract.pdf'),
                        pagesize=(width, height))
    doc.setTitle('From learned coordination to real-world energy control')
    doc.setAuthor('Tiago Fonseca')
    doc.setSubject('Schematic graphical abstract of the thesis; AI-generated illustration')
    doc.setFillColorRGB(1, 1, 1)
    doc.rect(0, 0, width, height, fill=1, stroke=0)
    doc.drawImage(image, 0, 0, width=width, height=height, mask='auto')
    doc.showPage()
    doc.save()

if __name__ == '__main__':
    build()
