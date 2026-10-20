"""Original vector CTDE illustration; conceptual source: Lowe et al. (2017).
Two sites recur in training and execution. Arrows distinguish joint experience,
policy updates, local inputs and charging decisions. No deployment topology implied.
"""
from pathlib import Path
from math import atan2, cos, sin, pi
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

HERE=Path(__file__).resolve().parent
INK='#302D29'; MUTED='#66635C'; TERRA='#AB6048'; SAGE='#5E7166'
CREAM='#F4EEE5'; MIST='#EAF0E9'; EDGE='#DED8CF'

def main():
    for name,file in [('Sans','LiberationSans-Regular.ttf'),('Serif','LiberationSerif-Regular.ttf')]:
        pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/liberation2/'+file))
    c=canvas.Canvas(str(HERE/'foundations-ctde.pdf'),pagesize=(800,320),invariant=1)
    c.setTitle('Centralised training and decentralised execution across two sites')
    c.setAuthor('Tiago Fonseca');c.setLineCap(1);c.setLineJoin(1)
    def text(x,y,value,size=17,font='Sans',colour=INK):
        c.setFillColor(HexColor(colour));c.setFont(font,size);c.drawCentredString(x,y,value)
    def path(points,colour,width=1.7,dashed=False,arrow=False):
        c.setStrokeColor(HexColor(colour));c.setLineWidth(width);c.setDash(5,4) if dashed else c.setDash()
        p=c.beginPath();p.moveTo(*points[0])
        for xy in points[1:]:p.lineTo(*xy)
        c.drawPath(p);c.setDash()
        if arrow:
            x,y=points[-1];a=atan2(y-points[-2][1],x-points[-2][0]);size=7
            p=c.beginPath();p.moveTo(x-size*cos(a-pi/6),y-size*sin(a-pi/6));p.lineTo(x,y);p.lineTo(x-size*cos(a+pi/6),y-size*sin(a+pi/6));c.drawPath(p)
    def box(x,y,w,h,colour,r=9):
        c.setFillColor(HexColor(colour));c.roundRect(x,y,w,h,r,stroke=0,fill=1)
    def site(x,label):
        # Site boundary contains its actor and a recognisable installation icon.
        box(x-63,59,126,111,'#F8F6F1')
        box(x-49,137,98,30,MIST,7);text(x,146,'Actor '+label,17,colour=SAGE)
        path([(x-23,102),(x,120),(x+23,102)],MUTED,1.7)
        path([(x-18,105),(x-18,83),(x+18,83),(x+18,105)],MUTED,1.7)
        path([(x-4,83),(x-4,97),(x+5,97),(x+5,83)],MUTED,1.5)
        text(x,66,'Site '+label,16)
    text(192,294,'a  Joint training',23,'Serif')
    text(600,294,'b  Local execution',23,'Serif')
    path([(400,20),(400,303)],EDGE,1)
    for x,label in [(100,'A'),(284,'B'),(506,'A'),(690,'B')]:site(x,label)
    # Experience from both sites reaches the critic through the outer channels.
    box(115,221,154,41,CREAM)
    text(192,236,'Centralised critic',18)
    path([(45,115),(22,115),(22,242),(111,242)],TERRA,1.9,arrow=True)
    path([(339,115),(362,115),(362,242),(273,242)],TERRA,1.9,arrow=True)
    text(192,272,'Observations and actions',15,colour=TERRA)
    # Policy learning uses the critic's evaluations; dashed paths carry updates.
    path([(158,221),(158,202),(100,202),(100,173)],SAGE,1.8,True,True)
    path([(226,221),(226,202),(284,202),(284,173)],SAGE,1.8,True,True)
    text(192,183,'Policy updates',15,colour=SAGE)
    text(192,30,'Learn from both sites',16,colour=MUTED)
    # Execution has no critic: each actor maps its available inputs to a power.
    text(600,252,'Local inputs at each site',18)
    text(600,231,'SoC · departure target · price',15,colour=MUTED)
    for x in (506,690):
        path([(x,216),(x,173)],TERRA,1.9,arrow=True)
        path([(x,56),(x,34)],SAGE,1.9,arrow=True)
        text(x,13,'Charging power',16,colour=SAGE)
    c.save()

if __name__=='__main__':main()
