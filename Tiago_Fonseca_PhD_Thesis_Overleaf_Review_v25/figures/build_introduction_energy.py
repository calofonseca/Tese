"""Publication-sized vector illustration for Figure 1.1.

Two household boundaries distinguish behind-the-meter storage and charging
from sharing through a common electricity network. Green arrows illustrate
possible uses of the surplus, not measured flows or dedicated peer cables.
The pictorial blue/green/terracotta palette follows the Chapter 3 figures.
Run this script with ReportLab to regenerate the standalone PDF.
"""
from math import cos, sin, pi, atan2
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

HERE = Path(__file__).resolve().parent
WIDTH, HEIGHT = 1000, 552
INK = '#233A46'
MUTED = '#526773'
BLUE = '#508AB9'
FLOW = '#42734D'
NETWORK = '#8D9EA7'
BORDER = '#C4CFD4'
PANEL = '#F9FBFC'
FONT_DIR = Path('/usr/share/fonts/truetype/liberation2')


class Figure:
    def __init__(self):
        # Embedded TrueType fonts retain sharp, portable lettering in print.
        for name, filename in [('FigureSans', 'LiberationSans-Regular.ttf'),
                               ('FigureSans-Bold', 'LiberationSans-Bold.ttf')]:
            pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
        self.c = canvas.Canvas(str(HERE / 'introduction-energy-sharing.pdf'),
                               pagesize=(WIDTH, HEIGHT), invariant=1,
                               initialFontName='FigureSans', initialFontSize=20)
        self.c.setTitle('Local storage and sharing of a household solar surplus')
        self.c.setAuthor('Tiago Fonseca')
        self.c.setSubject('Conceptual illustration for Chapter 1; not measured energy flows')
        self.c.setLineCap(1)
        self.c.setLineJoin(1)

    def text(self, x, y, text, size=20, bold=False, colour=INK, align='center'):
        c = self.c
        c.setFillColor(HexColor(colour))
        c.setFont('FigureSans-Bold' if bold else 'FigureSans', size)
        getattr(c, {'center': 'drawCentredString', 'left': 'drawString',
                    'right': 'drawRightString'}[align])(x, y, text)

    def line(self, points, colour=INK, width=2, dash=None):
        c = self.c
        c.setStrokeColor(HexColor(colour))
        c.setLineWidth(width)
        c.setDash(dash or [])
        p = c.beginPath()
        p.moveTo(*points[0])
        for point in points[1:]:
            p.lineTo(*point)
        c.drawPath(p)
        c.setDash([])

    def arrow(self, points, colour=FLOW, width=3):
        self.line(points, colour, width)
        x, y = points[-1]
        a = atan2(y - points[-2][1], x - points[-2][0])
        self.poly([(x, y),
                   (x-10*cos(a-pi/7), y-10*sin(a-pi/7)),
                   (x-10*cos(a+pi/7), y-10*sin(a+pi/7))], colour, colour, .6)

    def rect(self, x, y, w, h, fill, stroke=INK, radius=0, width=2):
        c = self.c
        c.setFillColor(HexColor(fill))
        c.setStrokeColor(HexColor(stroke))
        c.setLineWidth(width)
        if radius:
            c.roundRect(x, y, w, h, radius, fill=1, stroke=1)
        else:
            c.rect(x, y, w, h, fill=1, stroke=1)

    def poly(self, points, fill, stroke=INK, width=2):
        c = self.c
        c.setFillColor(HexColor(fill))
        c.setStrokeColor(HexColor(stroke))
        c.setLineWidth(width)
        p = c.beginPath()
        p.moveTo(*points[0])
        for point in points[1:]:
            p.lineTo(*point)
        p.close()
        c.drawPath(p, fill=1, stroke=1)

    def circle(self, x, y, r, fill, stroke=INK, width=2):
        c = self.c
        c.setFillColor(HexColor(fill))
        c.setStrokeColor(HexColor(stroke))
        c.setLineWidth(width)
        c.circle(x, y, r, fill=1, stroke=1)

    def node(self, x, y):
        self.circle(x, y, 4, FLOW, FLOW, .5)


def sun(d, x, y):
    d.circle(x, y, 16, '#F9E4A5', '#B3892B', 1.6)
    for i in range(8):
        a = i*pi/4
        d.line([(x+23*cos(a), y+23*sin(a)),
                (x+30*cos(a), y+30*sin(a))], '#B3892B', 1.8)


def house(d, x, y):
    """Rooftop PV and household load use the established pictorial vocabulary."""
    c = d.c
    c.saveState()
    c.translate(x, y)
    d.rect(-53, -48, 106, 91, '#F5E8CE', INK, radius=2)
    d.rect(29, 58, 13, 28, '#ECD4BB', INK, width=1.8)
    d.poly([(-65, 40), (0, 97), (65, 40), (57, 31),
            (0, 80), (-57, 31)], '#DCA58E', INK, 2.1)
    d.rect(-10, -48, 28, 51, '#FFFFFF', INK, width=1.8)
    d.circle(10, -23, 1.4, INK, INK, .5)
    for xx in [-36, 29]:
        d.rect(xx-10, 8, 20, 23, '#D9E9F1', INK, width=1.6)
        d.line([(xx, 8), (xx, 31)], '#8CA9B9', 1)
    # Panel sits on the roof plane and has individually drawn cells.
    d.poly([(-51, 45), (24, 45), (40, 77), (-35, 77)], BLUE, INK, 1.6)
    for dx in [-16, 3, 22]:
        d.line([(dx-16, 46), (dx, 76)], '#ECF5FA', 1)
    d.line([(-43, 61), (32, 61)], '#ECF5FA', 1)
    c.restoreState()


def battery(d, x, y):
    d.rect(x-26, y-45, 52, 90, '#EDF3E9', INK, radius=5, width=2)
    d.rect(x-12, y+45, 24, 5, '#EDF3E9', INK, radius=1, width=1.5)
    d.rect(x-17, y+15, 34, 18, '#FFFFFF', '#78976B', radius=2, width=1.2)
    d.text(x, y+20, '+', 14, True, FLOW)
    for yy in [-25, -10]:
        d.rect(x-17, y+yy, 34, 9, '#AECDA1', '#7D9D70', radius=1, width=1)


def charger(d, x, y):
    d.rect(x-15, y-39, 30, 78, '#DBE9D0', INK, radius=4, width=2)
    d.rect(x-10, y+17, 20, 13, '#FFFFFF', '#6F8B60', radius=1, width=1)
    d.poly([(x+2, y+9), (x-7, y-7), (x, y-7),
            (x-3, y-23), (x+9, y-3), (x+2, y-3)],
           FLOW, FLOW, .6)
    d.line([(x-20, y-40), (x+20, y-40)], INK, 2)


def vehicle(d, x, y):
    c = d.c
    c.saveState()
    c.translate(x, y)
    c.setFillColor(HexColor('#C6DFEE'))
    c.setStrokeColor(HexColor(INK))
    c.setLineWidth(2)
    p = c.beginPath()
    p.moveTo(-67, -16)
    p.lineTo(-67, 7)
    p.curveTo(-65, 15, -58, 17, -50, 19)
    p.lineTo(-31, 40)
    p.curveTo(-28, 43, -25, 44, -18, 44)
    p.lineTo(19, 44)
    p.curveTo(24, 44, 28, 42, 32, 38)
    p.lineTo(50, 19)
    p.lineTo(65, 14)
    p.curveTo(70, 12, 72, 7, 73, -1)
    p.lineTo(75, -16)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    d.poly([(-42, 19), (-25, 36), (-5, 36), (-5, 19)], '#F5FAFD', INK, 1.4)
    d.poly([(2, 19), (2, 36), (18, 36), (36, 19)], '#F5FAFD', INK, 1.4)
    d.line([(5, 9), (16, 9)], INK, 1.3)
    d.rect(-60, 3, 6, 6, '#FFFFFF', INK, radius=1, width=1)
    for xx in [-40, 44]:
        d.circle(xx, -15, 12, INK, INK, 1)
        d.circle(xx, -15, 6, '#F9FBFC', INK, 1)
    c.restoreState()


def main():
    d = Figure()
    # The frames indicate which assets belong to each household.
    for x in [15, 525]:
        d.rect(x, 153, 460, 386, PANEL, BORDER, radius=11, width=1.5)
    d.text(245, 510, 'Household with a solar surplus', 23, True)
    d.text(245, 480, 'Low demand at midday', 20, colour=MUTED)
    d.text(755, 510, 'Household in the example', 23, True)
    d.text(755, 480, 'Vehicle connected until afternoon', 20, colour=MUTED)

    # Draw the common network before placing the green conceptual flows.
    d.line([(66, 81), (935, 81)], NETWORK, 3)
    d.line([(160, 302), (160, 81)], NETWORK, 2.5)
    d.line([(650, 302), (650, 81)], NETWORK, 2.5)
    d.arrow([(160, 286), (160, 91)], width=3.2)
    d.arrow([(179, 81), (630, 81)], width=3.2)
    d.arrow([(650, 81), (650, 291)], width=3.2)
    d.node(160, 81)
    d.node(650, 81)
    d.text(413, 109, 'Share the surplus', 21, True, FLOW)
    d.text(500, 46, 'Shared local electricity network', 21)

    house(d, 160, 350)
    house(d, 650, 350)
    sun(d, 61, 431)
    battery(d, 367, 351)
    charger(d, 785, 342)
    vehicle(d, 898, 342)

    # Storage stays behind the producer's connection. Charging is behind the
    # receiving household's connection; neither asset connects directly to a bus.
    d.arrow([(216, 348), (331, 348)], width=3.2)
    d.arrow([(706, 348), (760, 348)], width=3.2)
    # Charging cable terminates at the vehicle's visible socket.
    c = d.c
    c.setStrokeColor(HexColor(INK))
    c.setLineWidth(2.1)
    p = c.beginPath()
    p.moveTo(800, 350)
    p.curveTo(817, 350, 806, 320, 818, 320)
    p.curveTo(829, 320, 828, 348, 838, 348)
    c.drawPath(p)
    d.text(367, 279, 'Stationary battery', 20)
    d.text(856, 279, 'EV charger and vehicle', 20)

    d.text(320, 200, 'Store for later use', 22, True, FLOW)
    d.text(791, 200, 'Charge before departure', 22, True, FLOW)

    # A short key states the meaning of the directional overlay without
    # requiring the reader to infer it from colour alone.
    d.arrow([(254, 17), (285, 17)], width=2.5)
    d.text(297, 10, 'Possible uses of the solar surplus', 19, colour=MUTED, align='left')
    d.c.showPage()
    d.c.save()


if __name__ == '__main__':
    main()
