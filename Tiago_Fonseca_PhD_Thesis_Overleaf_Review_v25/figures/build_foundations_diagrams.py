"""Original vector illustrations for Chapter 2, 12 October 2026.
Conceptual diagrams; no empirical data. Reuses the thesis equipment symbols.
The FlexOffer illustration has its own attributed builder.
"""
from pathlib import Path
from math import pi, cos, sin
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from build_introduction_energy import Figure, battery, charger, vehicle, house

HERE=Path(__file__).resolve().parent
INK='#233A46'; BLUE='#3978A8'; GREEN='#557F48'; GOLD='#B88720'; MUTED='#526773'
PALE='#E5F0F7'; PG='#EAF2E4'; BORDER='#C4CFD4'; PURPLE='#7B689C'
class Drawing(Figure):
    def __init__(self,name,h):
        for n,f in [('FigureSans','LiberationSans-Regular.ttf'),('FigureSans-Bold','LiberationSans-Bold.ttf')]:
            pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/liberation2/'+f))
        self.c=canvas.Canvas(str(HERE/(name+'.pdf')),pagesize=(1000,h),invariant=1)
        self.c.setTitle(name.replace('-',' '));self.c.setAuthor('Tiago Fonseca')
        self.c.setLineCap(1);self.c.setLineJoin(1)
    def words(self,x,y,lines,size=21,colour=INK,bold=False,align='center'):
        for i,t in enumerate(lines):self.text(x,y-i*(size*1.25),t,size,bold,colour,align)
    def box(self,x,y,w,h,lines,fill=PALE,size=21):
        self.rect(x,y,w,h,fill,BORDER,8,1.6)
        self.words(x+w/2,y+h/2+(len(lines)-1)*size*.625-7,lines,size)
    def icon(self,fn,x,y,scale=.75):
        self.c.saveState();self.c.translate(x,y);self.c.scale(scale,scale);fn(self,0,0);self.c.restoreState()
    def end(self):self.c.save()

def appliance(d,x,y):
    d.rect(x-34,y-43,68,86,'#F6E9D0',INK,5,2)
    d.circle(x,y-5,23,'#DDEAF1',INK,1.8)
    for xx in [-19,0,19]:d.circle(x+xx,y+30,3,INK,INK,1)

def bulb(d,x,y):
    d.circle(x,y+12,25,'#FFF0BF',INK,2)
    d.rect(x-12,y-23,24,18,'#DEE5E9',INK,3,2)
    for a in range(0,360,60):
        an=a*pi/180;d.line([(x+34*cos(an),y+12+34*sin(an)),(x+42*cos(an),y+12+42*sin(an))],GOLD,2)

def solar(d,x,y):
    d.poly([(x-48,y-20),(x+35,y-20),(x+48,y+30),(x-35,y+30)],'#78A7C6',INK,2)
    for xx in [-20,0,20]:d.line([(x+xx-10,y-18),(x+xx+2,y+28)],'#FFFFFF',1.4)
    d.line([(x-42,y+4),(x+41,y+4)],'#FFFFFF',1.4)
    d.line([(x,y-20),(x,y-38),(x-24,y-38),(x+24,y-38)],INK,2)

def graphline(d,x,y,ys,colour=BLUE,dash=None):
    d.line([(x,y),(x+240,y)],BORDER,1.1)
    d.line([(x,y),(x,y+48)],BORDER,1.1)
    d.line([(x+i*240/(len(ys)-1),y+v) for i,v in enumerate(ys)],colour,2.8,dash)

def router(d,x,y):
    d.line([(x-30,y+4),(x-40,y+50)],INK,3)
    d.line([(x+30,y+4),(x+40,y+50)],INK,3)
    d.rect(x-47,y-21,94,35,'#E5EDF2',INK,7,2)
    for xx in [-26,-12,2]:d.circle(x+xx,y-4,2.5,GREEN,GREEN,1)
    d.line([(x+18,y-6),(x+32,y-6)],MUTED,2)

def dishwasher(d,x,y):
    d.rect(x-35,y-44,70,88,'#F6E9D0',INK,5,2)
    d.line([(x-34,y+22),(x+34,y+22)],INK,1.5)
    d.circle(x-22,y+33,3,BLUE,BLUE,1)
    d.line([(x+8,y+33),(x+25,y+33)],MUTED,2)
    d.rect(x-27,y-33,54,44,'#FFFFFF',BORDER,3,1.2)
    # Plate rims and a glass make the appliance distinct from a washer.
    for xx in [-14,0,14]:
        d.c.setStrokeColor(HexColor(BLUE));d.c.setLineWidth(1.8)
        d.c.ellipse(x+xx-5,y-26,x+xx+5,y+3,stroke=1,fill=0)
    d.line([(x-24,y-28),(x+24,y-28)],MUTED,1.5)

def heatpump(d,x,y):
    d.rect(x-47,y-32,94,64,'#EDF3E9',INK,5,2)
    d.circle(x-13,y,23,'#FFFFFF',INK,1.5)
    d.circle(x-13,y,4,GREEN,GREEN,1)
    for angle in [0,120,240]:
        a=angle*pi/180
        d.poly([(x-13+5*cos(a),y+5*sin(a)),
                (x-13+19*cos(a+.3),y+19*sin(a+.3)),
                (x-13+17*cos(a+.9),y+17*sin(a+.9))], '#A8C89B',GREEN,1)
    for yy in [-14,-5,4,13]:d.line([(x+20,y+yy),(x+35,y+yy)],MUTED,1.5)
    for xx in [-30,30]:d.line([(x+xx,y-33),(x+xx,y-41)],INK,3)

def ev_charging(d,x,y):
    d.icon(charger,x-49,y+6,.86)
    d.icon(vehicle,x+10,y-7,.68)
    d.line([(x-62,y+2),(x-70,y+2),(x-70,y-33),(x-21,y-33),(x-21,y-15)],GREEN,2)

def resources():
    """Three illustrated asset classes, including stationary storage as elastic."""
    d=Drawing('foundations-resources',400)
    for x,colour,fill,title,description in [
        (166,GOLD,'#FCF5E5','Fixed','Consumption taken as given'),
        (500,BLUE,'#EFF5FA','Shiftable','Move the operating cycle'),
        (834,GREEN,'#F0F5EC','Elastic','Vary the operating power')]:
        d.circle(x,181,138,fill,fill,0)
        d.text(x,365,title,30,True,colour)
        d.text(x,332,description,21,colour=MUTED)
    # Familiar equipment symbols, grouped by the operation they permit.
    d.icon(bulb,104,235,1.08)
    d.words(104,165,['Lighting'],22)
    d.icon(router,235,177,1.02)
    d.words(235,119,['Wi-Fi router'],22)
    d.icon(appliance,431,235,1.05)
    d.words(431,156,['Washing','machine'],22)
    d.icon(dishwasher,568,177,1.05)
    d.words(568,107,['Dishwasher'],22)
    d.icon(ev_charging,834,266,.91)
    d.words(834,202,['EV charging'],22)
    d.icon(battery,761,137,.93)
    d.words(761,73,['Stationary','battery'],22)
    d.icon(heatpump,909,137,1.02)
    d.words(909,73,['Variable-speed','heat pump'],22)
    d.end()

def offline():
    d=Drawing('foundations-offline',435)
    xs=[120,385,650,895]
    labels=[['Collect experience'],['Fix the archive'],['Learn a policy'],['Use the policy']]
    for x,ls in zip(xs,labels):d.words(x,396,ls,22,bold=True)
    d.icon(house,90,256,.6);d.icon(charger,172,255,.6)
    # Archive symbol: stable record cards, not a software service.
    for delta in [14,7,0]:d.rect(315+delta,208+delta,125,106,'#F6F8FA',INK,4,1.6)
    for yy in [234,251,268,285]:d.line([(329,yy),(425,yy)],BLUE,2)
    # Compact neural representation, reused by the final policy.
    for x in [607,650,693]:
        for yy in [234,265,296]:d.circle(x,yy,7,PALE,BLUE,1.5)
    for xx in [607,650]:
        for a in [234,265,296]:
            for b in [234,265,296]:d.line([(xx+7,a),(xx+36,b)],'#B8CBD9',.8)
    d.box(826,222,138,88,['Policy'],PG,22)
    d.arrow([(212,264),(298,264)],BLUE,2.5)
    d.arrow([(464,264),(585,264)],BLUE,2.5)
    d.arrow([(716,264),(815,264)],GREEN,2.5)
    d.words(120,165,['Historical controller','and environment'],20,colour=MUTED)
    d.words(385,165,['Transitions, rewards,','and episode boundaries'],20,colour=MUTED)
    d.words(650,165,['Repeated updates','from the same data'],20,colour=MUTED)
    d.words(895,165,['New decisions','in operation'],20,colour=MUTED)
    d.line([(262,190),(262,351)],BORDER,1.5,[5,5]);d.line([(785,190),(785,351)],BORDER,1.5,[5,5])
    d.line([(304,92),(711,92)],BLUE,2);d.line([(304,92),(304,105)],BLUE,2);d.line([(711,92),(711,105)],BLUE,2)
    d.words(510,58,['No new environment transitions enter during offline training.'],20,colour=BLUE)
    d.end()

def hierarchy():
    d=Drawing('foundations-hierarchy',580)
    d.box(315,426,370,96,['Higher-level decision'],PALE,24)
    for x,label in [(205,'Local policy A'),(710,'Local policy B')]:
        d.box(x-95,235,190,80,[label],PG,21)
        d.arrow([(500,425),(500,358),(x,358),(x,318)],BLUE,2.5)
        d.arrow([(x,234),(x,171)],GREEN,2.5)
        d.text(x,143,'Primitive actions',20,colour=GREEN)
        d.arrow([(x-165,275),(x-99,275)],MUTED,2)
        d.words(x-150,319,['Local','observations'],18,align='center',colour=MUTED)
    d.text(284,380,'Goal, skill, budget, or incentive',19,colour=BLUE)
    d.arrow([(813,277),(943,277),(943,477),(690,477)],MUTED,2)
    d.words(864,417,['Outcome','feedback'],19,colour=MUTED)
    # Two aligned clocks show differing decisions without implying a fixed ratio.
    d.text(36,89,'Higher level',19,True,align='left');d.text(36,40,'Local level',19,True,align='left')
    for y in [95,46]:d.arrow([(235,y),(951,y)],INK,1.4)
    for x in [250,530,810]:
        d.rect(x-5,89,11,12,BLUE,BLUE,1,1)
        d.line([(x,100),(x,127)],BLUE,1.5)
    for x in range(250,926,70):d.circle(x,46,4,GREEN,GREEN,1)
    d.text(385,116,'Signal held',18,colour=BLUE);d.text(665,116,'Signal renewed',18,colour=BLUE)
    d.end()

def token(d,x,y,label,fill=PALE,w=75):
    d.rect(x-w/2,y-21,w,42,fill,BORDER,5,1.4);d.text(x,y-6,label,19,True)

def representations():
    d=Drawing('foundations-representations',510)
    for fn,x in [(battery,125),(charger,260),(charger,380)]:d.icon(fn,x,409,.7)
    d.text(600,431,'Same resource collection',22,True);d.words(600,399,['Battery B; chargers C1 and C2'],20,colour=MUTED)
    for x in [25,351,677]:d.rect(x,94,298,223,'#FBFCFD',BORDER,9,1.3)
    for x,t in [(174,'Fixed vector'),(500,'Set'),(826,'Graph')]:d.text(x,280,t,23,True)
    for i,t in enumerate(['B','C1','C2']):token(d,93+i*81,210,t,w=69)
    d.words(174,150,['Meaning follows','declared positions'],19,colour=MUTED)
    for x,y,t in [(430,215,'C2'),(550,227,'B'),(503,168,'C1')]:token(d,x,y,t,w=69)
    d.text(500,114,'Order is arbitrary',19,colour=MUTED)
    nodes=[(748,200,'B'),(886,223,'C1'),(884,150,'C2')]
    for x,y,_ in nodes[1:]:d.line([(748,200),(x,y)],BLUE,2)
    for x,y,t in nodes:token(d,x,y,t,w=65)
    d.text(826,114,'Edges encode relations',19,colour=MUTED)
    d.text(500,48,'Adding another charger introduces an entity with its own attributes and action.',20,colour=MUTED)
    d.end()

def attention():
    d=Drawing('foundations-attention',595)
    d.text(40,555,'ONE ATTENTION HEAD',21,True,align='left')
    for x,t in [(120,'Queries Q'),(370,'Keys K'),(660,'Values V')]:d.box(x-85,421,170,75,[t],PALE,22)
    d.arrow([(120,419),(120,363),(269,363)],BLUE,2)
    d.arrow([(370,419),(370,386)],BLUE,2)
    d.box(274,309,192,74,['Match and scale'],PALE,21)
    d.arrow([(466,346),(526,346)],BLUE,2)
    d.box(531,309,258,74,['Mask and normalise'],PG,21)
    d.arrow([(660,419),(840,419),(840,281)],GREEN,2)
    d.arrow([(660,307),(660,263),(738,263)],BLUE,2)
    d.box(743,215,225,64,['Weighted values'],PG,21)
    d.text(312,258,'One weight for each available key',19,colour=MUTED)
    d.line([(35,184),(965,184)],BORDER,1)
    d.text(40,148,'MULTIPLE HEADS',21,True,align='left')
    for x,t in [(363,'Head 1'),(513,'Head 2'),(663,'Head H')]:
        token(d,x,102,t,w=121)
        d.arrow([(x,80),(x,40),(792,40)],BLUE,1.7)
    d.box(794,10,173,65,['Combine'],PG,22)
    d.words(148,96,['Separate learned','projections'],20,colour=MUTED)
    d.end()

def modular():
    d=Drawing('foundations-modular',565)
    d.box(35,372,270,130,['Entity observations','and resource types'],PALE,22)
    d.arrow([(307,437),(373,437)],BLUE,2.5)
    d.box(379,372,252,130,['Shared','representation'],PALE,23)
    # Per-entity embeddings travel separately, sharing the relevant decoder.
    for x,t in [(200,'Battery B'),(502,'Charger C1'),(815,'Appliance A')]:
        d.arrow([(506,370),(506,344),(x,344),(x,314)],BLUE,2)
        token(d,x,291,t,w=179)
    d.box(75,154,552,74,['Shared continuous decoder'],PG,23)
    d.box(697,154,235,74,['Discrete decoder'],'#F5EAD4',22)
    for x in [200,502,815]:d.arrow([(x,268),(x,231)],BLUE,2)
    for x in [200,502,815]:d.arrow([(x,152),(x,104)],GREEN,2.5)
    d.words(200,78,['Battery power','for B'],21,colour=GREEN)
    d.words(502,78,['Charging power','for C1'],21,colour=GREEN)
    d.words(815,78,['Start / wait','for A'],21,colour=GREEN)
    d.text(500,530,'Shared knowledge, outputs tied to individual resources',23,True)
    d.end()

if __name__=='__main__':
    resources()
    # Updated foundations figures are maintained in the extended builder.
    from build_foundations_extended import offline, hierarchy, representations, attention, modular
    for f in [offline, hierarchy, representations, attention, modular]:
        f()
