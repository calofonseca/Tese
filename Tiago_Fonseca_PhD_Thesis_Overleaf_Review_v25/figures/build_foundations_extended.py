"""Original vector foundations figures, 14 October 2026.
Authoritative builder for neural, offline, hierarchy, representations, attention,
and modular figures. The older build_foundations_diagrams.py remains the source
for the unchanged resource illustration. Conceptual sources are cited in LaTeX.
"""
from pathlib import Path
from math import atan2, cos, sin, pi
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
HERE=Path(__file__).resolve().parent
INK='#302D29';MUTED='#66635C';TERRA='#AB6048';SAGE='#5E7166';CREAM='#F4EEE5';MIST='#EAF0E9';EDGE='#D8D1C7'
for n,f in [('Sans','LiberationSans-Regular.ttf'),('Serif','LiberationSerif-Regular.ttf'),('Math','LiberationSerif-Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/liberation2/'+f))
class Fig:
    def __init__(self,name,h):
        self.c=canvas.Canvas(str(HERE/f'foundations-{name}.pdf'),pagesize=(800,h),invariant=1)
        self.c.setTitle('Foundations: '+name);self.c.setAuthor('Tiago Fonseca');self.c.setLineCap(1);self.c.setLineJoin(1)
    def text(self,x,y,s,size=18,font='Sans',colour=INK):
        c=self.c;c.setFillColor(HexColor(colour));c.setFont(font,size);c.drawCentredString(x,y,s)
    def lines(self,x,y,ss,size=17,colour=MUTED):
        for i,s in enumerate(ss):self.text(x,y-i*(size+4),s,size,colour=colour)
    def path(self,ps,colour=INK,w=1.6,dash=False,arrow=False):
        c=self.c;c.setStrokeColor(HexColor(colour));c.setLineWidth(w);c.setDash(4,4) if dash else c.setDash()
        p=c.beginPath();p.moveTo(*ps[0])
        for xy in ps[1:]:p.lineTo(*xy)
        c.drawPath(p);c.setDash()
        if arrow:
            x,y=ps[-1];a=atan2(y-ps[-2][1],x-ps[-2][0]);z=6
            p=c.beginPath();p.moveTo(x-z*cos(a-pi/6),y-z*sin(a-pi/6));p.lineTo(x,y);p.lineTo(x-z*cos(a+pi/6),y-z*sin(a+pi/6));c.drawPath(p)
    def arrow(self,ps,colour=TERRA,dash=False):self.path(ps,colour,1.8,dash,True)
    def box(self,x,y,w,h,label=None,fill=CREAM,size=18):
        c=self.c;c.setFillColor(HexColor(fill));c.roundRect(x,y,w,h,8,fill=1,stroke=0)
        if label:self.text(x+w/2,y+h/2-6,label,size)
    def circle(self,x,y,r=8,fill=MIST):
        c=self.c;c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor(SAGE));c.setLineWidth(1.4);c.circle(x,y,r,stroke=1,fill=1)
    def house(self,x,y,s=1):
        self.path([(x-22*s,y),(x,y+18*s),(x+22*s,y)],MUTED)
        self.path([(x-17*s,y+3*s),(x-17*s,y-20*s),(x+17*s,y-20*s),(x+17*s,y+3*s)],MUTED)
        self.path([(x-4*s,y-20*s),(x-4*s,y-5*s),(x+5*s,y-5*s),(x+5*s,y-20*s)],MUTED)
    def asset(self,x,y,kind,label):
        c=self.c;c.setStrokeColor(HexColor(SAGE));c.setLineWidth(1.5)
        if kind=='battery':
            c.roundRect(x-14,y-18,28,38,3,stroke=1,fill=0);self.path([(x-6,y+24),(x+6,y+24)],SAGE,2.4)
            self.path([(x-6,y+10),(x+6,y+10)],SAGE);self.path([(x,y+4),(x,y+16)],SAGE);self.path([(x-6,y-8),(x+6,y-8)],SAGE)
        elif kind=='charger':
            c.roundRect(x-12,y-18,24,38,3,stroke=1,fill=0);self.path([(x+12,y+8),(x+23,y+8),(x+23,y-10),(x+17,y-10)],SAGE)
            self.path([(x+3,y+13),(x-4,y+2),(x+3,y+2),(x-3,y-9)],TERRA)
        else:
            c.roundRect(x-17,y-18,34,38,3,stroke=1,fill=0);c.circle(x,y-1,10,stroke=1,fill=0)
        self.text(x,y-40,label,16)
    def save(self):self.c.save()

def neural():
    d=Fig('neural',265)
    d.text(158,233,'Input features',23,'Serif');d.text(407,233,'Learned representation',23,'Serif');d.text(670,233,'Output',23,'Serif')
    ins=[84,130,176];hid=[64,108,152,196]
    for y in ins:
        for z in hid:d.path([(253,y),(391,z)],EDGE,1)
    for y in hid:d.path([(423,y),(654,130)],EDGE,1)
    for y,label in zip(ins,['Price','Time to departure','SoC']):
        d.text(105,y-5,label,17);d.circle(241,y,11,CREAM)
    for y in hid:d.circle(407,y,13)
    d.circle(670,130,14,CREAM);d.text(670,86,'Power request',17)
    d.text(241,25,'3 components',17,colour=MUTED);d.text(407,25,'4 components',17,colour=MUTED);d.text(670,25,'1 component',17,colour=MUTED)
    d.save()

def offline():
    d=Fig('offline',152)
    for x,t in [(82,'Collect'),(298,'Store'),(515,'Learn'),(725,'Use')]:d.text(x,126,t,22,'Serif')
    d.house(82,78,.82)
    for off in [6,3,0]:d.box(271+off,55+off,49,43,fill='#E9E3D9')
    for y in [65,73,81,89]:d.path([(279,y),(311,y)],MUTED,1.2)
    d.circle(515,77,25,CREAM);d.path([(503,77),(514,77),(527,89)],TERRA,2)
    d.box(689,58,72,36,'Policy',MIST,18)
    for x,z in [(110,260),(335,480),(550,680)]:d.arrow([(x,77),(z,77)])
    for x,t in [(82,'Past interactions'),(298,'Fixed dataset'),(515,'Repeated updates'),(725,'New decisions')]:d.text(x,18,t,16,colour=MUTED)
    d.save()

def hierarchy():
    d=Fig('hierarchy',206)
    d.box(7,83,219,76,fill=CREAM)
    d.text(116,130,'REC coordinator',19)
    d.text(116,104,'Signal updated hourly',16,colour=MUTED)
    d.path([(230,120),(314,120)],TERRA,1.8)
    d.arrow([(314,120),(314,159),(371,159)])
    d.arrow([(314,120),(314,82),(371,82)])
    d.text(294,181,'Same signal g',16,colour=TERRA)
    for y,site,condition,result in [(137,'A','Energy still required','Charging power'),(60,'B','Target already met','Zero power')]:
        d.box(375,y,236,43,'Site '+site+' policy',MIST,19)
        d.text(493,y-20,condition,16,colour=MUTED)
        d.arrow([(615,y+21),(670,y+21)],SAGE)
        d.text(735,y+16,result,16,colour=SAGE)
    d.text(116,26,'One signal per hour',16,colour=TERRA)
    d.text(518,8,'Local decisions every 15 minutes',16,colour=SAGE)
    d.save()

def representations():
    d=Fig('representations',310)
    for x,k,t in [(310,'battery','B'),(400,'charger','C1'),(490,'charger','C2')]:d.asset(x,266,k,t)
    for x,title in [(5,'Fixed vector'),(272,'Set'),(539,'Graph')]:
        d.box(x,71,256,142,fill='#F8F6F1');d.text(x+128,185,title,21,'Serif')
    for x,t in [(55,'B'),(132,'C1'),(209,'C2')]:d.box(x-30,124,60,30,t,CREAM,17)
    d.text(133,88,'Declared feature positions',15,colour=MUTED)
    for x,y,t in [(329,128,'C2'),(407,143,'B'),(474,115,'C1')]:d.box(x-26,y-13,52,28,t,MIST,16)
    d.text(400,88,'One record per entity',15,colour=MUTED)
    # The connection is an explicit relation node; leaves are the same assets.
    for x,y in [(581,128),(685,148),(738,117)]:d.path([(651,104),(x,y)],SAGE)
    d.circle(651,104,5)
    for x,y,t in [(581,128,'B'),(685,148,'C1'),(738,117,'C2')]:d.box(x-22,y-11,44,25,t,MIST,15)
    d.text(667,78,'Shared connection',14,colour=MUTED)
    d.text(133,28,'Append a feature group',15);d.text(400,28,'Add an entity record',15);d.text(667,28,'Add a node and its relation',15)
    d.text(45,48,'+ C3',14,colour=TERRA);d.text(307,48,'+ C3',14,colour=TERRA);d.text(575,48,'+ C3',14,colour=TERRA)
    d.save()

def attention():
    d=Fig('attention',427)
    d.text(180,394,'a  One attention head',23,'Serif');d.text(600,394,'b  Transformer block',23,'Serif')
    d.path([(389,20),(389,404)],EDGE,1)
    for x,t in [(70,'Q'),(180,'K'),(302,'V')]:d.box(x-33,320,66,38,t,CREAM,21)
    d.text(70,368,'Queries',15,colour=MUTED);d.text(180,368,'Keys',15,colour=MUTED);d.text(302,368,'Values',15,colour=MUTED)
    d.box(34,237,183,45,'Match and scale',MIST,18)
    d.arrow([(70,317),(70,286),(105,286),(105,285)])
    d.arrow([(180,317),(180,285)])
    d.box(34,159,183,46,'Mask + softmax',MIST,18);d.arrow([(125,234),(125,209)])
    d.box(110,70,244,45,'Weighted combination',CREAM,18)
    d.arrow([(125,156),(125,132),(197,132),(197,118)])
    d.arrow([(302,317),(302,118)],SAGE)
    d.text(69,139,'Weights',14,colour=MUTED)
    d.text(228,43,'One output per query',16,colour=MUTED)
    # Post-normalisation block. Separate bypasses start before each sublayer.
    d.text(591,355,'Entity representations',17)
    d.arrow([(591,341),(591,317)])
    d.box(471,268,240,44,'Multi-head attention',MIST,18)
    d.box(501,205,180,35,'Add + normalise',CREAM,17)
    d.arrow([(591,265),(591,243)])
    d.arrow([(591,329),(742,329),(742,222),(686,222)],MUTED)
    d.box(491,125,200,44,'Feed-forward',MIST,18)
    d.arrow([(591,202),(591,173)])
    d.box(501,62,180,35,'Add + normalise',CREAM,17)
    d.arrow([(591,122),(591,100)])
    d.arrow([(591,186),(742,186),(742,79),(686,79)],MUTED)
    d.arrow([(591,59),(591,32)])
    d.text(591,10,'Updated representations',17)
    d.text(739,346,'Residual paths',14,colour=MUTED)
    d.save()

def modular():
    d=Fig('modular',310)
    d.text(400,285,'Resource representations with shared site context',23,'Serif')
    for x,label in [(138,'Charger C1'),(400,'Charger C2'),(662,'Appliance A')]:d.box(x-89,211,178,40,label,CREAM,19)
    for x in [138,400,662]:d.arrow([(x,208),(x,176)])
    for x in [138,400]:d.box(x-101,127,202,44,'Charger decoder',MIST,18)
    d.box(566,127,192,44,'Appliance decoder',MIST,18)
    d.path([(239,149),(299,149)],SAGE,1.8,True)
    d.text(269,184,'Shared',14,colour=SAGE);d.text(269,167,'parameters',14,colour=SAGE)
    for x in [138,400,662]:d.arrow([(x,124),(x,88)],SAGE)
    d.lines(138,67,['Power for C1'],19,INK);d.lines(400,67,['Power for C2'],19,INK);d.lines(662,67,['Start / wait for A'],19,INK)
    d.text(400,18,'One decoder evaluation for each represented resource',17,colour=MUTED)
    d.save()

if __name__=='__main__':
    for f in [neural,offline,hierarchy,representations,attention,modular]:f()
