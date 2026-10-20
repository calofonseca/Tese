"""Runtime view: vector text/flows with pictograms adapted from the original figure."""
from pathlib import Path
from reportlab.lib.utils import ImageReader
from build_energaize_lifecycle import Diagram, controller, INK, BLUE, GREEN, PURPLE, GOLD, YELLOW, PALEBLUE, PALEORANGE
from reportlab.lib.colors import HexColor
from math import cos,sin,pi
P=Path(__file__).parent
RED='#B95750'

def icon(d,name,x,y,w,h):
    im=ImageReader(str(P/'runtime-icons'/f'{name}.png'));iw,ih=im.getSize();s=min(w/iw,h/ih)
    d.c.drawImage(im,x+(w-iw*s)/2,y+(h-ih*s)/2,width=iw*s,height=ih*s,mask='auto')

def heatpump(d,x,y,w=64,h=92):
    d.rect(x,y,w,h,'#F4F5F5',INK,r=7,lw=3)
    for yy in (y+25,y+66):
        d.circle(x+24,yy,16,'#F4F5F5',INK,2.3)
        for a in range(0,360,60):
            ang=a*pi/180;d.line([(x+24,yy),(x+24+13*cos(ang),yy+13*sin(ang))],INK,3)
        d.circle(x+24,yy,3,INK,INK)
    d.rect(x+47,y+55,9,13,'#FFFFFF',INK,lw=1.5)
    for yy in (y+18,y+25,y+32):d.line([(x+45,yy),(x+56,yy)],INK,2)

def box(d,x,y,w,h,label,fill=PALEORANGE,stroke=GOLD,size=23):
    d.rect(x,y,w,h,fill,stroke,r=7,lw=2.2)
    lines=label.split('\n');top=y+h/2+(len(lines)-1)*size*.625-size*.34
    d.text(x+w/2,top,label,size,True)

def both(d,pts,color=INK,width=2):
    d.arrow(pts,color,width);d.arrow(list(reversed(pts)),color,width)

def main():
    d=Diagram('energaize-runtime-revised.pdf',1320,950)
    d.c.saveState()
    d.c.translate(0,-150)
    d.rect(18,349,812,730,YELLOW,GOLD,r=32,lw=2.5)
    d.rect(870,349,430,730,'#F4F5F5','#7A858A',r=27,lw=2.2)
    d.text(44,1045,'EnergAIze - Building 1',27,True,align='left')
    d.text(1120,1045,'Building 1',27,True)
    icon(d,'building',888,953,95,85)
    # Monitoring is a distinct dashed tree rooted at Watchdog.
    d.line([(240,880),(284,880)],GOLD,2.2,dash=[7,5])
    d.arrow([(284,880),(284,953),(341,953)],GOLD,2.2,dash=[7,5])
    d.arrow([(284,880),(284,670),(401,670)],GOLD,2.2,dash=[7,5])
    d.arrow([(284,880),(284,867),(716,867),(716,857)],GOLD,2.2,dash=[7,5])
    d.text(175,952,'Service\nmonitoring',20,color='#966E17')
    # Observation and proposed-action channels.
    d.arrow([(450,742),(450,877)],BLUE,2.8)
    d.text(438,807,'Observations',20,color=BLUE,align='right')
    d.arrow([(514,878),(514,741)],PURPLE,2.8)
    d.text(531,840,'Proposed\nactions',18,color=PURPLE,align='left')
    # Independent validation: proposed actions out; validated actions back.
    d.arrow([(549,707),(584,707),(584,788),(629,788)],PURPLE,2.5)
    d.arrow([(630,757),(603,757),(603,682),(558,682)],PURPLE,2.8)
    d.text(661,704,'Validated\nactions',19,color=PURPLE)
    # Provider measurements and commands use different ports and routes.
    d.line([(892,797),(850,797),(850,653)],BLUE,2.6)
    d.line([(892,694),(850,694)],BLUE,2.6)
    d.arrow([(850,653),(557,653)],BLUE,2.6)
    d.text(722,663,'Observations',20,color=BLUE)
    d.line([(552,639),(866,639),(866,775)],PURPLE,2.6)
    d.arrow([(866,775),(891,775)],PURPLE,2.6)
    d.arrow([(866,669),(891,669)],PURPLE,2.6)
    d.text(719,612,'Validated actions',20,color=PURPLE)
    # Records originate at Percepta and reach each recipient.
    d.line([(424,616),(321,616)],GREEN,2.7)
    d.line([(321,554),(321,712)],GREEN,2.7)
    for yy in (712,633,554):d.arrow([(321,yy),(252,yy)],GREEN,2.7)
    d.text(252,495,'Decision records',19,color='#557E43',align='right')
    # Vehicle data and forecasts arrive through Percepta.
    d.arrow([(245,394),(381,394),(381,572),(430,610)],BLUE,2.7)
    d.arrow([(480,562),(480,591)],BLUE,2.7)
    d.text(503,570,'Forecasts',19,color=BLUE,align='left')
    d.arrow([(945,391),(945,327),(147,327),(147,364)],RED,2.4)
    d.text(541,300,'Vehicle API',21,color=RED)
    # Components are drawn after routing so all strokes terminate at boundaries.
    box(d,60,850,180,60,'Watchdog')
    for yy,label in [(685,'Database'),(606,'User interfaces'),(527,'KPI Manager')]:box(d,50,yy,202,55,label,PALEBLUE,BLUE,22)
    d.rect(342,878,272,153,PALEBLUE,BLUE,r=14,lw=2.3)
    controller(d,358,907,240,110)
    d.text(478,888,'Inference service',20,True)
    d.circle(480,670,78,PALEORANGE,GOLD,2.6);d.text(480,662,'Percepta',26,True)
    box(d,630,730,174,127,'',size=22)
    d.text(717,824,'Fail-Safe\nSupervisor',22,True)
    d.text(717,767,'Limits and\nRBC fallback',17)
    box(d,50,365,195,58,'PulseCharge',PALEBLUE,BLUE,22)
    d.rect(414,362,385,200,'#FFF8E7',GOLD,r=11,lw=2)
    d.text(606,532,'Forecasting',23,True)
    d.rect(430,380,165,130,PALEORANGE,GOLD,r=5)
    d.rect(614,380,169,130,PALEORANGE,GOLD,r=5)
    d.text(512,480,'Predictor',23,True);d.text(512,446,'Production and\nconsumption',18)
    d.text(698,480,'Flexon',23,True);d.text(698,446,'Available\nflexibility',18)
    # Physical installation. Reuse original pictograms, with clear, brief labels.
    box(d,892,755,178,72,'CW Cloud\nPlatform','#F5D0CC','#B9635F',22)
    box(d,892,645,178,72,'Other IoT\nAPIs','#FFF3CE',GOLD,22)
    d.text(1150,1000,'PV',23,True)
    d.text(1245,1000,'Heat pump',20,True)
    icon(d,'pv',1107,889,90,93);heatpump(d,1214,889,64,92)
    d.text(1235,704,'Storage',21,True);icon(d,'storage',1210,724,50,78)
    d.text(1205,507,'EV chargers',22,True)
    icon(d,'charger',1135,531,62,94);icon(d,'charger',1231,531,62,94)
    # Logical equipment association, separate from the measurement/action channels.
    d.line([(1110,853),(1246,853)],INK,3)
    for xx,yy in [(1150,900),(1246,889)]:d.line([(xx,853),(xx,yy)],INK,3)
    d.line([(1235,853),(1235,802)],INK,3)
    d.line([(1110,853),(1110,650),(1262,650)],INK,3)
    d.line([(1166,650),(1166,615)],INK,3)
    d.line([(1262,650),(1262,615)],INK,3)
    # Provider interfaces connect to the installation, without device-specific API clutter.
    both(d,[(1070,790),(1110,790)],'#487481',2.4)
    both(d,[(1070,682),(1110,682)],'#487481',2.4)
    d.text(979,596,'Equipment\ninterfaces',20,color='#365C68')
    icon(d,'ev',923,375,161,86);d.text(1005,366,'EV',22,True)
    d.c.restoreState()
    # The two abbreviated building instances share one row to keep the overview compact.
    for x,label in [(24,'2'),(695,'n')]:
        box(d,x,24,225,86,f'EnergAIze\nBuilding {label}',YELLOW,GOLD,23)
        both(d,[(x+225,67),(x+261,67)],INK,2.5)
        d.rect(x+261,24,340,86,'#F4F5F5','#7A858A',r=16,lw=2)
        d.c.saveState();d.c.translate(x+304,63);d.c.scale(.49,.49);d.house(0,0);d.c.restoreState()
        box(d,x+339,36,122,62,'CW Cloud\nPlatform','#F5D0CC','#B9635F',19)
        box(d,x+471,36,117,62,'Other IoT\nAPIs','#FFF3CE',GOLD,19)
    d.text(660,62,'...',25,True)
    d.done()

if __name__=='__main__':main()
