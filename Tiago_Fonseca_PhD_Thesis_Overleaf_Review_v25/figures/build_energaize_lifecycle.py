"""Editable vector companions to the author's pictorial EnergAIze figures."""
from pathlib import Path
from math import atan2, cos, sin, pi
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white

HERE = Path(__file__).parent
INK = '#233A46'
BLUE = '#508AB9'
GREEN = '#76A95D'
PURPLE = '#A27BAF'
GOLD = '#D6A02D'
YELLOW = '#FFF3CE'
PALEBLUE = '#DAEAF7'
PALEORANGE = '#FDE8CD'
SALMON = '#F5D0CC'

class Diagram:
    def __init__(self,name,w,h):
        self.c=canvas.Canvas(str(HERE/name),pagesize=(w,h))
        self.c.setTitle(name.replace('.pdf','').replace('-',' '))
        self.c.setAuthor('Tiago Fonseca')
        self.c.setFillColor(white); self.c.rect(0,0,w,h,fill=1,stroke=0)
    def line(self,points,color=INK,width=2,dash=None):
        c=self.c;c.setStrokeColor(HexColor(color));c.setLineWidth(width)
        c.setDash(dash or [])
        p=c.beginPath();p.moveTo(*points[0])
        for x,y in points[1:]:p.lineTo(x,y)
        c.drawPath(p);c.setDash([])
    def arrow(self,points,color=INK,width=2.4,dash=None):
        self.line(points,color,width,dash)
        x,y=points[-1];a=atan2(y-points[-2][1],x-points[-2][0])
        p=self.c.beginPath();p.moveTo(x,y)
        p.lineTo(x-11*cos(a-pi/7),y-11*sin(a-pi/7))
        p.lineTo(x-11*cos(a+pi/7),y-11*sin(a+pi/7));p.close()
        self.c.setFillColor(HexColor(color));self.c.drawPath(p,fill=1,stroke=0)
    def text(self,x,y,text,size=20,bold=False,color=INK,align='center'):
        c=self.c;c.setFillColor(HexColor(color));c.setFont('Helvetica-Bold' if bold else 'Helvetica',size)
        for i,s in enumerate(text.split('\n')):
            yy=y-i*size*1.25
            if align=='center':c.drawCentredString(x,yy,s)
            elif align=='right':c.drawRightString(x,yy,s)
            else:c.drawString(x,yy,s)
    def rect(self,x,y,w,h,fill,stroke=INK,r=0,lw=2):
        c=self.c;c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor(stroke));c.setLineWidth(lw)
        if r:c.roundRect(x,y,w,h,r,fill=1,stroke=1)
        else:c.rect(x,y,w,h,fill=1,stroke=1)
    def circle(self,x,y,r,fill,stroke=INK,lw=2):
        c=self.c;c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor(stroke));c.setLineWidth(lw);c.circle(x,y,r,fill=1,stroke=1)
    def polygon(self,pts,fill,stroke=INK,lw=2):
        c=self.c;p=c.beginPath();p.moveTo(*pts[0])
        for pt in pts[1:]:p.lineTo(*pt)
        p.close();c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor(stroke));c.setLineWidth(lw);c.drawPath(p,fill=1,stroke=1)
    def database(self,x,y,w=94,h=82):
        c=self.c
        c.setFillColor(HexColor(PALEBLUE));c.setStrokeColor(HexColor(BLUE));c.setLineWidth(2.4)
        p=c.beginPath();p.moveTo(x-w/2,y+h/2)
        p.lineTo(x-w/2,y-h/2)
        p.curveTo(x-w/2,y-h/2-17,x+w/2,y-h/2-17,x+w/2,y-h/2)
        p.lineTo(x+w/2,y+h/2);p.close();c.drawPath(p,fill=1,stroke=1)
        c.ellipse(x-w/2,y+h/2-13,x+w/2,y+h/2+13,fill=1,stroke=1)
        for yy in [y-h/2+24]:
            p=c.beginPath();p.moveTo(x-w/2,yy+7);p.curveTo(x-w/2,yy-10,x+w/2,yy-10,x+w/2,yy+7);c.drawPath(p)
    def document(self,x,y,w=64,h=84):
        self.polygon([(x-w/2,y-h/2),(x+w/2,y-h/2),(x+w/2,y+h/2-18),(x+w/2-18,y+h/2),(x-w/2,y+h/2)],'#FFFFFF',BLUE)
        self.line([(x+w/2-18,y+h/2),(x+w/2-18,y+h/2-18),(x+w/2,y+h/2-18)],BLUE)
        for off in [12,-3,-18]:self.line([(x-w/2+12,y+off),(x+w/2-12,y+off)],BLUE,2.5)
    def server(self,x,y,w=58,h=81):
        self.rect(x-w/2,y-h/2,w,h,PALEBLUE,INK,r=5)
        for off in [-24,0,24]:
            self.rect(x-w/2+7,y+off-7,w-14,15,'#FFFFFF',BLUE,r=2,lw=1.5)
            self.circle(x+w/2-15,y+off,2,GREEN,GREEN)
    def monitor(self,x,y,w=82,h=54):
        self.rect(x-w/2,y-h/2,w,h,PALEBLUE,INK,r=4)
        self.rect(x-w/2+6,y-h/2+6,w-12,h-12,'#FFFFFF',BLUE,lw=1)
        self.line([(x,y-h/2),(x,y-h/2-17)],INK,4)
        self.line([(x-22,y-h/2-18),(x+22,y-h/2-18)],INK,4)
        self.line([(x-26,y-5),(x-11,y+8),(x+3,y-1),(x+25,y+13)],GREEN,3)
    def laptop(self,x,y):
        self.rect(x-37,y-17,74,50,PALEBLUE,INK,r=4)
        self.rect(x-31,y-11,62,38,'#FFFFFF',BLUE,lw=1)
        self.polygon([(x-37,y-17),(x+37,y-17),(x+49,y-31),(x-49,y-31)],'#B9D4E2')
        self.line([(x-10,y-24),(x+10,y-24)],BLUE,2)
    def cloud(self,x,y):
        for xx,yy,rr in [(x-26,y,24),(x,y+15,31),(x+28,y+2,23)]:self.circle(xx,yy,rr,PALEBLUE,BLUE)
        self.c.setFillColor(HexColor(PALEBLUE));self.c.rect(x-35,y-18,73,32,fill=1,stroke=0)
        self.line([(x-37,y-22),(x+42,y-22)],BLUE,2)
        self.rect(x-19,y-17,38,27,'#FFFFFF',BLUE,r=3)
        self.text(x,y-8,'GPU',12,True,BLUE)
    def chip(self,x,y):
        self.rect(x-31,y-27,62,54,'#CFE7BA','#52743D',r=5)
        self.rect(x-19,y-16,38,32,'#FFFFFF','#52743D',r=3)
        for off in [-19,-6,7,20]:
            self.line([(x+off,y+27),(x+off,y+36)],'#52743D',3)
            self.line([(x+off,y-27),(x+off,y-36)],'#52743D',3)
            self.line([(x-31,y+off),(x-40,y+off)],'#52743D',3)
            self.line([(x+31,y+off),(x+40,y+off)],'#52743D',3)
    def network(self,x,y):
        layers=[[(x-35,y-25),(x-35,y),(x-35,y+25)],[(x,y-36),(x,y-12),(x,y+12),(x,y+36)],[(x+35,y-20),(x+35,y+20)]]
        for a,b in zip(layers,layers[1:]):
            for p in a:
                for q in b:self.line([p,q],'#92A5AD',1.3)
        for i,layer in enumerate(layers):
            for xx,yy in layer:self.circle(xx,yy,5,[PALEBLUE,PALEORANGE,'#CFE7BA'][i])
    def house(self,x,y,s=1):
        self.rect(x-37*s,y-32*s,74*s,63*s,'#F8E3B9',INK,r=2)
        self.polygon([(x-47*s,y+27*s),(x,y+68*s),(x+47*s,y+27*s),(x+39*s,y+18*s),(x,y+52*s),(x-39*s,y+18*s)],'#EE9A79')
        self.rect(x-6*s,y-32*s,20*s,38*s,'#FFFFFF',INK,lw=1.8)
        for xx in [x-25*s,x+23*s]:self.rect(xx-7*s,y+7*s,14*s,16*s,PALEBLUE,INK,lw=1.5)
    def charger(self,x,y):
        self.rect(x-16,y-31,32,69,'#98C344','#65768C',r=3)
        self.rect(x-12,y+18,10,9,'#E9ED9A','#98C344',lw=0.1)
        self.polygon([(x+1,y+11),(x-8,y-6),(x,y-6),(x-3,y-20),(x+10,y),(x+2,y)],'#FFF19F','#FFF19F',0.4)
        self.line([(x+16,y+17),(x+30,y+6),(x+26,y-12)],BLUE,4)
    def done(self):self.c.showPage();self.c.save()

def stage(d,x,y,number):
    """Shared stage identifiers persist when an artefact crosses figure views."""
    d.circle(x,y,17,INK,INK)
    d.text(x,y-7,str(number),20,True,color='#FFFFFF')

def controller(d,x,y,w,h):
    """One visual identity for the policy during learning and runtime execution."""
    d.rect(x,y,w,h,PALEORANGE,GOLD,r=12,lw=2.2)
    compact=h<80
    scale=min(w/125,h/(85 if compact else 155))
    d.c.saveState();d.c.translate(x+w/2,y+h*(.50 if compact else .64));d.c.scale(scale,scale)
    d.network(0,0);d.c.restoreState()
    if not compact:d.text(x+w/2,y+17,'Controller',23,True)

def bundle(d,x,y,w=240):
    """The same model/contract object at export and at catalogue admission."""
    d.c.saveState();d.c.translate(x,y);d.c.scale(w/240,w/240)
    d.rect(0,0,240,156,'#E8F2E2',GREEN,r=16,lw=2.3)
    d.document(53,109,40,55)
    controller(d,122,81,94,60)
    d.text(120,44,'Model bundle',24,True)
    d.text(120,18,'Model + contract',21)
    d.c.restoreState()

def experiment(d,x,y,w=360):
    """Expanded job: reuses the simulator/controller pair of the training view."""
    d.rect(x,y,w,100,'#E8F2E2',GREEN,r=12,lw=2.2)
    d.rect(x+14,y+62,74,27,INK,INK,r=13,lw=0)
    d.text(x+51,y+68,'4 / 5',19,True,color='#FFFFFF')
    d.text(x+205,y+70,'Experiment',21,True)
    for dx,dy in [(0,0),(11,0),(22,0),(11,11),(22,11)]:
        d.rect(x+w-49+dx,y+68+dy,9,9,PALEBLUE,BLUE,r=1,lw=.7)
    d.rect(x+20,y+14,120,36,'#FFFFFF',BLUE,r=8)
    d.text(x+80,y+24,'CityLearn',20,True)
    controller(d,x+w-143,y+7,124,50)
    d.arrow([(x+149,y+39),(x+w-151,y+39)],BLUE,1.6)
    d.arrow([(x+w-151,y+20),(x+149,y+20)],PURPLE,1.6)

def container(d,x,y,w,h,title,subtitle='',fill=PALEORANGE,stroke=GOLD):
    d.rect(x,y,w,h,fill,stroke,r=12,lw=2.2)
    # Stacked cargo blocks distinguish a software container from a host.
    for dx,dy in [(0,0),(12,0),(24,0),(12,12),(24,12)]:
        d.rect(x+12+dx,y+h-29+dy,10,10,PALEBLUE,BLUE,r=1,lw=0.8)
    d.text(x+w/2,y+h/2-1,title,21,True)
    if subtitle:d.text(x+w/2,y+13,subtitle,20)

def host(d,x,y,w,h,title,icon='server',fill='#F7FAFC'):
    d.rect(x,y,w,h,fill,BLUE,r=20,lw=2.5)
    d.c.saveState(); d.c.translate(x+41,y+h-39);d.c.scale(0.58,0.58)
    getattr(d,icon)(0,0);d.c.restoreState()
    d.text(x+78,y+h-33,title,23,True,align='left')
    d.line([(x+18,y+h-72),(x+w-18,y+h-72)],'#BACBD5',1.3)

def api_badge(d,x,y):
    d.circle(x,y,15,BLUE,BLUE)
    d.text(x,y-7,'A',19,True,color='#FFFFFF')

def orchestration():
    d=Diagram('energaize-orchestration.pdf',1080,1190)
    # The current deployment places the orchestrator and remote adapters on OPEVA.
    host(d,20,575,1040,590,'OPEVA server',fill=YELLOW)
    d.text(1040,1131,'Docker containers use the stacked-block symbol',19,align='right')
    container(d,55,985,240,83,'Web interface')
    container(d,365,985,275,83,'Backend API')
    container(d,710,985,310,83,'Job Orchestrator')
    d.arrow([(302,1026),(358,1026)],BLUE)
    d.arrow([(175,1075),(175,1083),(865,1083),(865,1074)],BLUE)
    api_badge(d,865,963)
    d.text(545,931,'A  Common job interface: requests, status and progress',21,color=BLUE)
    d.database(136,867,87,58)
    d.text(211,883,'Shared storage',22,True,align='left')
    d.text(211,853,'Datasets, configurations, logs, results and model files',20,align='left')
    d.arrow([(865,945),(865,864),(824,864)],GREEN)
    d.text(944,876,'Persist',19,color=GREEN)
    # Worker and job are sibling containers on the host, not nested Docker.
    container(d,60,725,270,90,'Worker Agent','Docker adapter')
    api_badge(d,309,828)
    experiment(d,60,592)
    d.arrow([(195,717),(195,698)],BLUE)
    d.text(226,700,'Host Docker',18,color=BLUE,align='left')
    container(d,460,725,260,90,'Worker Agent','Deucalion adapter')
    api_badge(d,699,828)
    container(d,775,725,250,90,'Worker Agent','Union adapter')
    api_badge(d,1004,828)
    d.text(745,667,'Remote execution',21,True)
    d.text(745,638,'Adapters stay on this server',19)
    # Four distinct execution hosts/environments, with recognisable illustrations.
    host(d,20,60,245,430,'Personal',icon='laptop')
    d.text(98,431,'computer',23,True,align='left')
    host(d,285,60,245,430,'Jetson',icon='chip')
    d.text(363,431,'Xavier',23,True,align='left')
    host(d,550,60,245,430,'Deucalion')
    host(d,815,60,245,430,'Union',icon='cloud')
    for x in [40,305]:
        container(d,x,295,205,89,'Worker Agent','Docker adapter')
        api_badge(d,x+183,396)
        container(d,x,132,205,89,'Experiment','CityLearn + controller',fill='#E8F2E2',stroke=GREEN)
        d.arrow([(x+73,286),(x+73,229)],BLUE)
        d.text(x+95,265,'Host',20,color=BLUE,align='left')
        d.text(x+95,242,'Docker',20,color=BLUE,align='left')
    d.text(142,88,'CPU / GPU',19)
    d.text(407,88,'ARM64 / GPU',19)
    d.arrow([(590,717),(590,548),(780,548),(780,350),(772,350)],BLUE)
    d.text(659,518,'SSH',20,color=BLUE,align='right')
    d.rect(576,313,193,74,PALEBLUE,BLUE,r=12)
    d.text(672,353,'Slurm',23,True)
    d.text(672,328,'Resource allocation',18)
    d.arrow([(672,305),(672,229)],BLUE)
    
    d.rect(576,132,193,89,'#E8F2E2',GREEN,r=12)
    d.text(672,183,'Experiment',21,True)
    d.text(672,151,'Singularity / Apptainer',19)
    d.text(672,88,'Compute nodes',19)
    d.arrow([(900,717),(900,548),(1046,548),(1046,350),(1037,350)],BLUE)
    d.text(955,518,'Remote API',20,color=BLUE)
    d.rect(841,313,193,74,PALEBLUE,BLUE,r=12)
    d.text(937,353,'Task service',22,True)
    d.text(937,328,'Remote submission',18)
    d.arrow([(937,305),(937,229)],BLUE)
    
    d.rect(841,132,193,89,'#E8F2E2',GREEN,r=12)
    d.text(937,183,'Experiment',21,True)
    d.text(937,151,'GPU task',19)
    d.text(937,88,'Object-store transfer',18)
    d.text(540,23,'Experiments execute training (4) or evaluation (5) and retain their outputs.',21)
    d.done()

def development():
    d=Diagram('energaize-controller-development.pdf',1080,1040)
    d.house(98,954,0.64)
    d.c.saveState();d.c.translate(163,936);d.c.scale(.7,.7);d.charger(0,0);d.c.restoreState()
    d.database(240,940,68,57)
    d.text(184,873,'Installation records',23,True)
    d.text(184,845,'Demand, production, use',20)
    d.document(805,950,58,77)
    d.text(805,873,'REC configuration',23,True)
    d.text(805,845,'Resources and operating limits',20)
    d.rect(378,746,324,78,PALEBLUE,BLUE,r=18)
    d.text(540,792,'Prepared scenarios',23,True)
    d.text(540,764,'Data + resource models',20)
    d.arrow([(184,830),(184,785),(370,785)],BLUE)
    d.arrow([(805,830),(805,785),(710,785)],BLUE)
    # The simulated interaction loop is distinct from the learning update.
    d.rect(20,360,1040,316,YELLOW,GOLD,r=30,lw=2.2)
    d.text(83,638,'Training',25,True,align='left')
    d.rect(57,409,252,178,'#FFFFFF',BLUE,r=16)
    d.house(120,529,0.51)
    d.c.saveState();d.c.translate(206,518);d.c.scale(.64,.64);d.charger(0,0);d.c.restoreState()
    d.text(183,454,'CityLearn',23,True)
    d.text(183,430,'Simulated environment',20)
    controller(d,425,442,250,145)
    d.rect(805,442,216,145,'#E8F2E2',GREEN,r=16)
    d.c.saveState();d.c.translate(913,537);d.c.scale(.7,.7);d.monitor(0,0);d.c.restoreState()
    d.text(913,473,'Learning',23,True)
    d.text(913,453,'Policy update',19)
    d.arrow([(317,553),(417,553)],BLUE)
    d.text(367,610,'Observations',20,color=BLUE)
    d.arrow([(417,480),(317,480)],PURPLE)
    d.text(367,456,'Actions',20,color=PURPLE)
    d.arrow([(675,550),(798,550)],BLUE)
    d.text(739,610,'Experience',20,color=BLUE)
    d.arrow([(798,482),(682,482)],GREEN)
    d.text(739,459,'Parameters',20,color=GREEN)
    # Experience uses the environment response, including reward.
    d.arrow([(240,401),(240,382),(987,382),(987,434)],BLUE)
    d.text(775,397,'Next observations and rewards',19,color=BLUE)
    d.arrow([(540,737),(540,705),(183,705),(183,595)],BLUE)
    # Candidate policies are evaluated without parameter updates.
    d.circle(550,382,6,YELLOW,YELLOW,lw=0)
    d.arrow([(550,434),(550,323),(439,323),(439,255)],GREEN)
    d.text(681,336,'Candidate policy',20,color=GREEN)
    d.rect(225,100,430,146,PALEBLUE,BLUE,r=18)
    d.monitor(303,183,87,57)
    d.text(484,205,'Evaluation',24,True)
    d.text(484,173,'Policy held fixed',21)
    d.text(442,122,'Cost, peaks, service and scenario outcomes',20)
    d.arrow([(672,738),(672,725),(1072,725),(1072,286),(292,286),(292,255)],BLUE)
    d.text(899,309,'Evaluation scenarios',20,color=BLUE)
    bundle(d,817,106,221)
    d.arrow([(663,182),(808,182)],GREEN)
    d.text(738,210,'Select and export',19,color=GREEN)
    d.text(541,45,'Model bundle (6) continues into deployment with the same controller and contract.',20)
    for x,y,n in [(36,881,1),(618,881,2),(378,824,3),(50,646,4),(225,246,5),(817,250,6)]:
        stage(d,x,y,n)
    d.done()

def deployment():
    d=Diagram('energaize-model-deployment.pdf',920,830)
    # The exported object is identical to the model bundle in development.
    bundle(d,50,632,235)
    d.database(460,739,94,76)
    d.text(460,660,'Bundle catalogue',22,True)
    d.text(460,635,'Stored versions',18)
    d.monitor(760,742,102,62)
    d.text(760,660,'Operator selection',22,True)
    d.text(760,635,'Bundle and target',18)
    d.arrow([(293,739),(402,739)],GREEN)
    d.text(346,763,'Store',18,color=GREEN)
    d.arrow([(516,744),(693,744)],GREEN)
    d.text(605,765,'Inspect',18,color=GREEN)

    d.rect(25,65,870,487,YELLOW,GOLD,r=32,lw=2.2)
    d.text(55,515,'Runtime architecture',23,True,align='left')
    d.house(139,359,0.82);d.charger(215,301)
    d.text(145,244,'Building and equipment',18.5,True)
    d.circle(432,359,61,PALEORANGE,GOLD,2.5)
    d.text(432,353,'Percepta',21,True)
    d.rect(642,285,228,188,PALEBLUE,BLUE,r=18)
    controller(d,664,322,184,137)
    d.text(756,300,'Inference service',20,True)
    d.arrow([(760,609),(760,480)],GREEN,2.8)
    d.text(683,581,'Backend loads\nselected bundle',17.5,color=GREEN)
    d.arrow([(870,424),(882,424),(882,702),(819,702)],GREEN,2,dash=[6,4])
    d.text(828,579,'Active',17.5,color=GREEN)
    d.text(828,557,'version',17.5,color=GREEN)

    d.arrow([(242,382),(368,382)],BLUE)
    d.text(300,404,'Observations',17.5,color=BLUE)
    d.arrow([(491,382),(635,382)],BLUE)
    d.text(572,404,'Observations',17.5,color=BLUE)
    d.arrow([(635,339),(491,339)],PURPLE)
    d.text(570,314,'Proposed actions',17.5,color=PURPLE)
    d.rect(602,136,210,63,PALEORANGE,GOLD,r=7)
    d.text(707,175,'Fail-Safe',20,True)
    d.text(707,151,'Supervisor',20,True)
    d.arrow([(461,302),(461,185),(594,185)],INK)
    d.text(530,207,'Check actions',17.5)
    d.arrow([(594,153),(401,153),(401,302)],PURPLE)
    d.text(498,128,'Validated actions',17.5,color=PURPLE)
    d.arrow([(374,334),(258,334)],PURPLE)
    d.text(303,311,'Validated',17.5,color=PURPLE)
    d.text(303,290,'actions',17.5,color=PURPLE)
    d.text(139,198,'Provider interfaces',18)
    d.text(139,175,'connect measurements',17.5)
    d.text(139,153,'and equipment commands',17.5)
    for x,y,n in [(50,787,6),(407,785,7),(709,788,8),(760,518,9)]:
        stage(d,x,y,n)
    d.done()

if __name__=='__main__':
    development();orchestration();deployment()
