"""Original vector illustration: organisational scales around an energy community.
Reuses the thesis equipment artwork. Tiers express scope, not ownership or a
universal command chain. No empirical quantities are plotted.
"""
from build_foundations_diagrams import Drawing, bulb, dishwasher, solar, heatpump
from build_introduction_energy import house, battery, charger

INK='#233A46'; BLUE='#3978A8'; GREEN='#557F48'; GOLD='#B88720'
MUTED='#526773'; BORDER='#C4CFD4'


def tower(d,x,y):
    d.line([(x-26,y-40),(x,y+53),(x+26,y-40)],INK,3)
    for yy,half in [(24,42),(2,34),(-20,25)]:
        d.line([(x-half,y+yy),(x+half,y+yy)],INK,3)
        if yy>=0:
            for xx in [-half,half]:
                d.line([(x+xx,y+yy),(x+xx,y+yy-12)],BLUE,3)
    d.line([(x-18,y-13),(x+15,y+10),(x-10,y+29)],INK,2)
    d.line([(x+18,y-13),(x-15,y+10),(x+10,y+29)],INK,2)
    d.line([(x-25,y-40),(x+18,y-13),(x-18,y-13),(x+25,y-40)],INK,2)


def distribution(d,x,y):
    # A transformer and outgoing distribution lines.
    d.line([(x-78,y+39),(x+78,y+39)],BLUE,2.5)
    for xx in [-65,65]:
        d.line([(x+xx,y+40),(x+xx,y-37)],INK,3)
        d.line([(x+xx-16,y+25),(x+xx+16,y+25)],INK,2)
    d.rect(x-26,y-30,52,62,'#E5EDF2',INK,4,2)
    for xx in [-16,-5,6,17]:d.line([(x+xx,y-17),(x+xx,y+17)],BLUE,2)
    d.line([(x,y+32),(x,y+39)],INK,2)
    d.line([(x,y-30),(x,y-44),(x+53,y-44)],BLUE,2)


def building(d,x,y):
    d.rect(x-35,y-41,70,92,'#E2EBF0',INK,2,2)
    for xx in [-20,0,20]:
        for yy in [-12,12,36]:d.rect(x+xx-5,y+yy-6,10,12,'#FFFFFF',BORDER,0,1)
    d.rect(x-8,y-41,16,19,'#FFFFFF',INK,0,1)


def factory(d,x,y):
    d.poly([(x-49,y-34),(x-49,y+17),(x-16,y+39),(x-16,y+17),(x+16,y+39),(x+16,y+17),(x+47,y+17),(x+47,y-34)],'#E8E9E0',INK,2)
    d.rect(x+29,y+17,13,41,'#CCD7DD',INK,0,2)
    for xx in [-30,-4,22]:d.rect(x+xx-7,y-6,14,14,'#FFFFFF',BORDER,0,1)


def community(d,x,y):
    # A shared ring connects sites, with a small collective solar installation.
    d.c.setStrokeColorRGB(.33,.50,.28);d.c.setLineWidth(2)
    d.c.ellipse(x-128,y-27,x+128,y+36,stroke=1,fill=0)
    for xx,yy in [(-90,0),(0,29),(90,0)]:d.icon(house,x+xx,y+yy,.38)
    d.icon(solar,x,y-24,.48)


def draw():
    d=Drawing('foundations-community-structure',650)
    centre=320
    # Pyramid bands with white gutters, increasing in width towards resources.
    def half(y):return 292-(y-30)*.43
    levels=[(30,140,'#FCF5E5'),(149,259,'#F7F0E5'),(268,378,'#EAF2E4'),(387,497,'#E9F1F7'),(506,625,'#DDE9F2')]
    for lo,hi,col in levels:
        d.poly([(centre-half(lo),lo),(centre+half(lo),lo),(centre+half(hi),hi),(centre-half(hi),hi)],col,col,0)
    d.icon(tower,320,555,.79)
    d.icon(distribution,320,438,.93)
    community(d,320,312)
    d.icon(house,172,193,.49)
    d.icon(building,320,201,.71)
    d.icon(factory,466,197,.67)
    for fn,x,scale in [(bulb,115,.65),(dishwasher,212,.66),(battery,317,.62),(charger,426,.76),(heatpump,523,.65)]:
        d.icon(fn,x,86,scale)
    for cy,title,lines,colour in [
        (561,'Transmission',['TSO: wider system operation','and interconnections'],BLUE),
        (442,'Distribution',['DSO: network operation','and local grid constraints'],BLUE),
        (323,'RECs',['Participating members','and shared resources'],GREEN),
        (204,'Sites',['Homes, commercial buildings,','and industrial facilities'],GOLD),
        (85,'Assets',['Loads, generation,','and storage'],GOLD)]:
        edge=centre+half(cy)
        d.line([(edge+13,cy),(659,cy)],BORDER,1.7)
        d.circle(edge+13,cy,3,colour,colour,0)
        d.text(684,cy+26,title,26,True,colour,'left')
        d.words(684,cy-5,lines,21,colour=MUTED,align='left')
    d.end()

if __name__=='__main__':draw()
