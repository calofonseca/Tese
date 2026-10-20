"""Vector learning diagrams using the established EnergAIze visual vocabulary."""
from pathlib import Path
import importlib.util
HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('energaize_visuals',HERE/'build_energaize_lifecycle.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
Diagram=m.Diagram
INK=m.INK;BLUE=m.BLUE;GREEN=m.GREEN;PURPLE=m.PURPLE;GOLD=m.GOLD
PB=m.PALEBLUE;PO=m.PALEORANGE

def battery(d,x,y):
 d.rect(x-20,y-27,40,54,'#D9EABC',GREEN,r=4)
 d.rect(x-8,y+27,16,6,GREEN,GREEN,r=1)
 d.text(x,y-5,'+',22,True,color=GREEN)

def badge(d,x,y,n):
 d.circle(x,y,14,INK,INK);d.text(x,y-6,str(n),17,True,color='#FFFFFF')

def local():
 d=Diagram('control-local-agent.pdf',1000,570)
 d.rect(22,223,225,320,'#FAF7F0','#D5C7AD',r=16)
 d.text(135,513,'BUILDING',24,True);d.house(116,399,1.0)
 d.charger(186,326);battery(d,72,325)
 d.text(135,253,'Resources and services',19)
 d.rect(310,354,228,152,PB,BLUE,r=12)
 badge(d,328,496,1);d.text(424,467,'Observation',24,True)
 d.text(424,430,'State and headroom\nService and context',20)
 d.text(424,371,'Encode permitted inputs',17,color=BLUE)
 d.arrow([(247,427),(310,427)],BLUE)
 d.rect(592,354,186,152,'#E8F2DE',GREEN,r=12)
 badge(d,610,496,2);d.text(685,467,'Local actor',24,True)
 d.network(685,422);d.text(685,366,'Learned policy',17)
 d.arrow([(538,427),(592,427)],BLUE)
 d.rect(833,354,145,152,PO,GOLD,r=12)
 badge(d,851,496,3);d.text(905,466,'Commands',21,True)
 d.text(905,429,'Battery\nEV charger\nAppliance',18)
 d.arrow([(778,427),(833,427)],GREEN)
 d.arrow([(905,354),(905,291),(247,291)],GREEN)
 d.text(610,304,'Action handling and physical response',20,color=GREEN)
 d.rect(310,24,668,175,'#F7F2FA',PURPLE,r=14)
 d.text(337,170,'LEARNING',20,True,color=PURPLE,align='left')
 d.database(431,95,80,64);d.text(431,34,'Recorded transitions',17)
 d.network(675,104);d.text(675,38,'Policy and value updates',18)
 d.arrow([(482,105),(613,105)],PURPLE)
 d.arrow([(135,223),(135,104),(379,104)],PURPLE)
 d.text(184,119,'Experience',18,color=PURPLE,align='left')
 d.arrow([(766,110),(807,110),(807,328),(701,328),(701,354)],PURPLE,dash=[7,5])
 d.text(904,220,'Policy update',17,color=PURPLE)
 d.done()

def marl():
 d=Diagram('control-marl-training.pdf',1000,565)
 d.rect(22,330,956,209,'#F7F2FA',PURPLE,r=15)
 d.text(48,505,'CENTRALISED TRAINING',24,True,color=PURPLE,align='left')
 d.database(131,413,83,60);d.text(267,433,'Joint observations',21);d.text(267,402,'and submitted actions',19)
 d.arrow([(376,420),(473,420)],PURPLE)
 d.rect(474,376,280,98,'#FFFFFF',PURPLE,r=9)
 d.network(525,422);d.text(659,440,'Critic learning',23,True);d.text(658,406,'Return estimates',19)
 d.text(855,433,'Rewards and',20);d.text(855,405,'next observations',19)
 d.arrow([(781,420),(754,420)],PURPLE)
 d.text(500,7,'DECENTRALISED EXECUTION: ACTORS AND LOCAL INPUTS',17,True,color=GREEN)
 for i,x in enumerate([170,500,830],1):
  d.rect(x-140,28,280,252,'#FAFCF8','#B7CBA9',r=13)
  d.rect(x-100,197,200,62,'#E8F2DE',GREEN,r=10)
  d.text(x,221,f'Local actor {i}',22,True)
  d.house(x,100,.76);d.text(x,45,f'Building {i}',20,True)
  d.arrow([(x-67,120),(x-67,197)],BLUE)
  d.text(x-77,163,'Inputs',16,align='right',color=BLUE)
  d.arrow([(x+66,197),(x+66,122)],GREEN)
  d.text(x+77,163,'Actions',16,align='left',color=GREEN)
  d.arrow([(x,349),(x,259)],PURPLE,dash=[6,4])
 d.line([(170,349),(830,349)],PURPLE,2,dash=[6,4])
 d.line([(540,376),(540,349)],PURPLE,2,dash=[6,4])
 d.text(755,363,'Policy learning',17,color=PURPLE)
 d.text(493,548,'Critics and joint training data remain outside local inference',18)
 d.done()

def hierarchy():
 d=Diagram('control-hierarchy.pdf',1000,490)
 d.rect(256,327,488,135,'#F7F2FA',PURPLE,r=14)
 d.network(319,392);d.text(552,421,'REC coordinator',24,True)
 d.text(552,384,'Aggregate conditions',20);d.text(552,354,'Global or member-specific signal',18)
 d.arrow([(499,327),(499,292)],PURPLE)
 d.line([(159,292),(841,292)],PURPLE,2.3)
 d.text(290,300,'Effective-price signal',18,color=PURPLE);d.text(730,300,'1 = neutral',18,color=PURPLE)
 for i,x in enumerate([160,500,840],1):
  d.rect(x-135,35,270,208,'#FAFCF8','#B7CBA9',r=12)
  d.rect(x-108,168,216,58,'#E8F2DE',GREEN,r=9)
  d.text(x,189,'Local controller',22,True)
  d.arrow([(x,292),(x,226)],PURPLE)
  d.house(x-43,102,.65);d.charger(x+73,102)
  d.arrow([(x+72,168),(x+72,141)],GREEN)
  d.arrow([(x-78,136),(x-78,168)],BLUE)
  d.text(x,46,f'Building {i}: local service and limits',16)
 d.text(498,12,'The bill uses the realised tariff; the coordination signal influences decisions.',17)
 d.done()

def dynamic():
 d=Diagram('control-dynamic-resources.pdf',1000,620)
 d.text(500,590,'CONTROL WITH A CHANGING RESOURCE SET',25,True)
 d.text(500,559,'A new charger adds an observation record and a corresponding command.',20)
 for label,y,extra in [('Initial installation',360,False),('After installation of charger B',113,True)]:
  d.rect(20,y-68,960,212,'#FAFCF8','#B7CBA9',r=13)
  d.text(42,y+112,label,22,True,align='left')
  battery(d,78,y+13);d.text(78,y-40,'Battery',17)
  d.charger(177,y+12);d.text(177,y-40,'Charger A',17)
  if extra:
   d.charger(278,y+12);d.text(278,y-40,'Charger B',17)
   d.circle(309,y+66,14,GREEN,GREEN);d.text(309,y+60,'+',20,True,color='#FFFFFF')
  d.arrow([(333,y+13),(396,y+13)],BLUE)
  d.rect(397,y-32,252,104,PB,BLUE,r=10)
  d.network(446,y+18);d.text(563,y+37,'Local policy',22,True);d.text(563,y+3,'same weights',18)
  d.line([(649,y+13),(687,y+13)],GREEN,2.2)
  d.line([(687,y+62),(687,y-28 if extra else y+17)],GREEN,2.2)
  labels=['Battery command','Charger A command']+(['Charger B command'] if extra else [])
  for j,t in enumerate(labels):
   yy=y+65-j*45;d.rect(708,yy-20,250,35,'#E8F2DE',GREEN,r=6);d.text(833,yy-10,t,18);d.arrow([(687,yy-3),(708,yy-3)],GREEN,1.8)
 d.arrow([(523,326),(523,190)],PURPLE,dash=[7,5])
 d.text(536,267,'Reuse: compatible known resource types',17,color=PURPLE,align='left')
 d.text(499,15,'Resource identity keeps each command connected to the equipment it controls.',18)
 d.done()

if __name__=='__main__':
 local();marl();hierarchy();dynamic()
