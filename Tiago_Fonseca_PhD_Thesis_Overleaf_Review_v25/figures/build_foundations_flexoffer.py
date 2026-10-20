"""Vector FlexOffer example, adapted from Fonseca et al. (2022), Figure 1.

Source: Flexible Loads Scheduling Algorithms for Renewable Energy Communities,
Energies 15(23), 8875, doi:10.3390/en15238875 (CC BY 4.0).
The illustrative profile and selected values are new explanatory choices,
not measured data. All labels and geometric elements remain vector artwork.
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

HERE = Path(__file__).parent
INK = '#233A46'
BLUE = '#3978A8'
GREEN = '#76A95D'
GOLD = '#B88720'


def main():
    c = canvas.Canvas(str(HERE / 'foundations-flexoffer.pdf'), pagesize=(1000, 590))
    c.setTitle('Start-time and energy flexibility in a FlexOffer')
    c.setAuthor('Tiago Fonseca')

    def line(x1, y1, x2, y2, color=INK, width=1.7, dash=None):
        c.setStrokeColor(HexColor(color)); c.setLineWidth(width)
        c.setDash(dash or []); c.line(x1, y1, x2, y2); c.setDash([])

    def text(x, y, value, size=21, color=INK, bold=False, align='left'):
        c.setFillColor(HexColor(color))
        c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
        if align == 'centre': c.drawCentredString(x, y, value)
        else: c.drawString(x, y, value)

    def rich(x, y, value, width=290, size=21, color=INK, align=0):
        style = ParagraphStyle('label', fontName='Helvetica', fontSize=size,
                               leading=size*1.25, textColor=HexColor(color), alignment=align)
        p = Paragraph(value, style); _, h = p.wrap(width, 100)
        p.drawOn(c, x, y-h)

    def rect(x, y, w, h, fill, stroke=INK):
        c.setFillColor(HexColor(fill)); c.setStrokeColor(HexColor(stroke))
        c.setLineWidth(1.4); c.rect(x,y,w,h,fill=1,stroke=1)

    def flexible(x, y, w, h):
        rect(x,y,w,h,'#FFF1CD',GOLD)
        c.saveState()
        path=c.beginPath(); path.rect(x,y,w,h); c.clipPath(path,stroke=0)
        for offset in range(-int(h), int(w+h), 12):
            line(x+offset,y,x+offset+h,y+h,'#D3AD55',0.7)
        c.restoreState()

    def double_arrow(x1,x2,y,color=BLUE):
        line(x1,y,x2,y,color,1.8)
        for x,direction in [(x1,1),(x2,-1)]:
            line(x,y,x+direction*9,y+4,color,1.8)
            line(x,y,x+direction*9,y-4,color,1.8)

    # Legend: fill and line styles remain distinct in greyscale.
    rect(105, 536, 28, 21, '#B7D59E', GREEN)
    text(145, 537, 'Minimum energy')
    flexible(455, 536, 28, 21)
    text(495, 537, 'Available energy range')
    line(105, 506, 135, 506, BLUE, 3.8)
    rich(145, 520, 'Selected energy, <i>E</i><sub>k</sub>', width=300)
    text(100, 460, 'Energy per interval [kWh]', bold=True)

    x0,y0,step,unit=100,180,110,64
    for value in [0,1,2,3]:
        y=y0+unit*value
        line(x0,y,785,y,'#DCE2E5',0.8)
        text(x0-23,y-6,str(value),size=19,align='centre')
    line(x0,y0,x0,415,INK,2)
    line(x0,y0,802,y0,INK,2)
    line(802,y0,792,y0+5);line(802,y0,792,y0-5)
    for h in range(18,25):
        x=x0+(h-18)*step
        line(x,y0,x,y0-7)
        text(x,y0-30,f'{h:02d}:00',size=19,align='centre')
    text(810,174,'Time',size=20)

    lower=[2.0,1.0,0.5]; upper=[3.0,2.0,1.5]; selected=[2.5,1.5,1.0]
    assert all(lo <= e <= hi for lo,e,hi in zip(lower,selected,upper))
    for k,(lo,hi,e) in enumerate(zip(lower,upper,selected),start=1):
        x=320+(k-1)*step
        rect(x,y0,step,lo*unit,'#B7D59E',GREEN)
        flexible(x,y0+lo*unit,step,(hi-lo)*unit)
        line(x+3,y0+e*unit,x+step-3,y0+e*unit,BLUE,3.8)
        c.setFillColor(HexColor(BLUE));c.circle(x+step/2,y0+e*unit,4,fill=1,stroke=0)
        text(x+step/2,y0+hi*unit+13,f'Interval {k}',size=19,align='centre')

    double_arrow(320,650,425,INK)
    text(485,441,'Three one-hour intervals',size=20,align='centre')
    # Label the physical bounds of the final interval, not a power amplitude.
    line(652,276,697,276,GOLD,1.4,[4,3])
    rich(708,293,'Upper bound <i>E</i><sub>3</sub><super>max</super>',size=21)
    line(652,212,697,212,GREEN,1.4,[4,3])
    rich(708,229,'Lower bound <i>E</i><sub>3</sub><super>min</super>',size=21)

    # Independent choice of start time for the complete profile.
    rect(100,121,440,17,'#DAEAF7',BLUE)
    double_arrow(101,539,129)
    for x in [100,320,540]: line(x,139,x,178,BLUE,1.5,[4,3])
    for x,symbol,label in [(100,'es','Earliest start'),(320,'sch','Selected start'),(540,'ls','Latest start')]:
        rich(x-85,118,f'<i>t</i><sub>{symbol}</sub>',width=170,size=23,color=BLUE,align=1)
        text(x,60,label,size=20,color=BLUE,align='centre')
    text(320,26,'Start-time flexibility',size=21,color=BLUE,bold=True,align='centre')
    c.save()


if __name__ == '__main__':
    main()
