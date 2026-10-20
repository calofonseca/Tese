"""Original, compact vector MDP cycle; conceptual source: Sutton & Barto (2018).
Warm editorial palette, restrained emblems and two directional channels.
Reward indexing follows the thesis: r_t is received after action a_t.
"""
from pathlib import Path
from math import atan2, cos, sin, pi
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

HERE = Path(__file__).resolve().parent
INK = '#302D29'
MUTED = '#66635C'
TERRA = '#AB6048'
SAGE = '#5E7166'
CREAM = '#F4EEE5'
MIST = '#EAF0E9'


def main():
    for name, file in [('Sans', 'LiberationSans-Regular.ttf'),
                       ('Serif', 'LiberationSerif-Regular.ttf'),
                       ('Math', 'LiberationSerif-Italic.ttf')]:
        pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/liberation2/' + file))
    c = canvas.Canvas(str(HERE / 'foundations-rl-cycle.pdf'), pagesize=(740, 235), invariant=1)
    c.setTitle('Agent–environment interaction in a fully observable MDP')
    c.setAuthor('Tiago Fonseca')
    c.setLineCap(1)
    c.setLineJoin(1)

    def line(points, colour, width=1.7):
        c.setStrokeColor(HexColor(colour)); c.setLineWidth(width)
        p = c.beginPath(); p.moveTo(*points[0])
        for xy in points[1:]: p.lineTo(*xy)
        c.drawPath(p)

    def arrow(x1, y1, x2, y2, colour):
        line([(x1, y1), (x2, y2)], colour, 2)
        angle = atan2(y2-y1, x2-x1)
        line([(x2-8*cos(angle-pi/6), y2-8*sin(angle-pi/6)), (x2, y2),
              (x2-8*cos(angle+pi/6), y2-8*sin(angle+pi/6))], colour, 2)

    def circle(x, y, radius, colour, stroke=None, width=1.6):
        c.setFillColor(HexColor(colour)); c.setLineWidth(width)
        if stroke: c.setStrokeColor(HexColor(stroke))
        c.circle(x, y, radius, stroke=int(stroke is not None), fill=1)

    def text(x, y, value, size=18, font='Sans', colour=INK):
        c.setFillColor(HexColor(colour)); c.setFont(font, size)
        c.drawCentredString(x, y, value)

    def mathlabel(x, y, parts):
        # Each part is (text, font, size, baseline shift), with real subscripts.
        widths = [pdfmetrics.stringWidth(t, f, z) for t, f, z, dy in parts]
        left = x-sum(widths)/2
        c.setFillColor(HexColor(MUTED))
        for (t, f, z, dy), w in zip(parts, widths):
            c.setFont(f, z); c.drawString(left, y+dy, t); left += w

    # Decision emblem: one incoming condition and two possible choices.
    circle(112, 156, 43, CREAM)
    line([(91, 156), (109, 156), (126, 173)], TERRA, 2.4)
    line([(109, 156), (126, 139)], '#C9BFB3', 2.1)
    circle(91, 156, 4.5, TERRA)
    circle(128, 175, 5.7, TERRA)
    circle(128, 137, 5.2, CREAM, '#ADA398')
    text(112, 84, 'Agent', 26, 'Serif')
    text(112, 60, 'Choose an action', 18, colour=MUTED)
    mathlabel(112, 34, [('Policy ', 'Sans', 17, 0), ('π', 'Math', 19, 0)])

    # Transition emblem: the state changes in response to the chosen action.
    circle(628, 156, 43, MIST)
    circle(610, 156, 10, MIST, SAGE, 1.7)
    arrow(625, 156, 639, 156, SAGE)
    circle(652, 156, 7, SAGE)
    text(628, 84, 'Environment', 26, 'Serif')
    text(628, 60, 'Update the state', 18, colour=MUTED)
    mathlabel(628, 34, [('s', 'Math', 19, 0), ('t', 'Math', 13, -4),
                         ('  →  ', 'Sans', 17, 0), ('s', 'Math', 19, 0),
                         ('t+1', 'Math', 13, -4)])

    # The upper channel is the selected action; the lower carries both outputs.
    arrow(162, 174, 578, 174, TERRA)
    mathlabel(370, 193, [('Action ', 'Sans', 19, 0), ('a', 'Math', 21, 0),
                         ('t', 'Math', 14, -4)])
    arrow(578, 137, 162, 137, SAGE)
    mathlabel(370, 105, [('Next state ', 'Sans', 18, 0), ('s', 'Math', 21, 0),
                         ('t+1', 'Math', 14, -4), ('   ·   Reward ', 'Sans', 18, 0),
                         ('r', 'Math', 21, 0), ('t', 'Math', 14, -4)])
    c.save()


if __name__ == '__main__':
    main()
