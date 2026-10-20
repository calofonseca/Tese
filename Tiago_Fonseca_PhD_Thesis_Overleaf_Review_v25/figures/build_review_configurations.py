"""Original vector comparisons for Section 3.3: learning and representation.
No energy-specific entities or empirical measurements. Uses the thesis palette.
Run to regenerate both review PDFs.
"""
from build_foundations_diagrams import Drawing, INK, BLUE, GREEN, MUTED, BORDER

PALE='#EDF4F8'; PG='#EDF4E9'; GOLD='#A97D2C'; PURPLE='#75648F'
COLS=[BLUE,GOLD,PURPLE]
FILLS=['#E8F1F8','#FAF0DA','#EEEAF4']

def entities(d,x,ys,updated=False):
    for i,y in enumerate(ys):
        d.circle(x,y,22,FILLS[i],COLS[i],2.4 if updated else 1.4)
        d.text(x,y-7,str(i+1),22,True,COLS[i])

def mechanisms():
    d=Drawing('review-variable-configurations',720)
    d.text(270,694,'Input entities',21,True)
    d.text(445,694,'Processing',21,True)
    d.text(650,694,'Result',21,True)
    rows=[(580,'Set aggregation',['Encode each entity;','pool the results.']),
          (415,'Attention',['Weight information','from other entities.']),
          (250,'Graph message passing',['Exchange information','along specified edges.']),
          (85,'Typed modules',['Choose the mapping','by entity type.'])]
    for y,title,explain in rows:
        if y!=85:d.line([(0,y-82),(1000,y-82)],BORDER,1.1)
        if title=='Graph message passing':
            d.words(0,y+42,['Graph message','passing'],23,bold=True,align='left')
        else:d.text(0,y+23,title,23,True,align='left')
        d.words(0,y-24,explain,19,colour=MUTED,align='left')
    # Shared per-entity encoder followed by invariant aggregation.
    y=580;ys=[y+47,y,y-47]
    entities(d,270,ys)
    for yy in ys:
        d.arrow([(295,yy),(330,yy)],BLUE,1.8)
        d.box(334,yy-19,55,38,['f'],PALE,23)
        d.arrow([(391,yy),(457,y)],BLUE,1.8)
    d.box(460,y-30,97,60,['sum /','mean'],PALE,20)
    d.arrow([(560,y),(607,y)],BLUE,2)
    d.box(610,y-30,100,60,['Collection','summary'],PG,19)
    d.words(770,y+17,['One summary,','independent of','entity order'],21,align='left')
    d.text(362,y+70,'shared encoder f',18,False,MUTED)
    # Weighted relationships are computed separately for every output entity.
    y=415;ys=[y+47,y,y-47]
    for j,yout in enumerate(ys):
        for i,yin in enumerate(ys):
            d.line([(295,yin),(621,yout)],COLS[j],3.0 if i==(j+1)%3 else 1.0)
    entities(d,270,ys);entities(d,646,ys,True)
    d.text(455,y+60,'Learned attention weights',19,False,MUTED)
    d.words(770,y+28,['One contextual','representation','for each entity'],21,align='left')
    # The explicit graph determines the neighbourhoods used in each update.
    y=250
    for shift in [0,316]:
        pts=[(251+shift,y+48),(325+shift,y-44),(400+shift,y+48)]
        d.line([pts[0],pts[1],pts[2]],BLUE,2.0)
        for i,(x,yy) in enumerate(pts):
            d.circle(x,yy,22,FILLS[i],COLS[i],2.3 if shift else 1.4)
            d.text(x,yy-7,str(i+1),22,True,COLS[i])
    d.arrow([(437,y),(520,y)],BLUE,2.3)
    d.words(481,y+42,['Neighbour','aggregation'],18,colour=MUTED)
    d.words(770,y+28,['Update each node','using its connected','neighbours'],21,align='left')
    # A repeated type uses the same mapping for separate entities.
    y=85;ys=[y+47,y,y-47]
    entities(d,270,ys)
    for i,yy in enumerate(ys):
        d.arrow([(295,yy),(380,yy)],BLUE,1.8)
        d.box(383,yy-20,126,40,['Type B' if i==1 else 'Type A'],PALE if i==1 else PG,21)
        d.arrow([(512,yy),(620,yy)],BLUE,1.8)
    entities(d,646,ys,True)
    d.words(770,y+40,['Entities 1 and 3','reuse the Type A','mapping; outputs','remain separate.'],21,align='left')
    d.c.setSubject('Conceptual mechanisms: set aggregation, attention, graph message passing and typed mappings.')
    d.end()

def actor_critics():
    """Compact critic comparison with one shared local-execution strip."""
    d=Drawing('review-actor-critics',430)
    d.text(0,410,'Training: information and learning signals',22,True,align='left')
    centers=[158,500,842]
    for x in [329,671]:d.line([(x,110),(x,383)],BORDER,1.2)
    for j,(x,name) in enumerate(zip(centers,['MADDPG','MATD3','MAPPO'])):
        d.text(x,370,name,26,True,BLUE)
        d.text(x,338,'Replay buffer' if j<2 else 'Recent trajectories',21,False,MUTED)
        d.words(x,305,['Joint observations + actions'] if j<2 else ['Global / joint information'],20)
        if j==1:
            d.arrow([(x,292),(x,279),(x-60,279),(x-60,267)],BLUE,1.8)
            d.arrow([(x,279),(x+60,279),(x+60,267)],BLUE,1.8)
            for xx,label in [(x-60,'Q1'),(x+60,'Q2')]:
                d.circle(xx,244,24,PG,GREEN,1.5)
                d.text(xx,237,label,22,True,GREEN)
            d.text(x,200,'Minimum target trains both critics',18,False,MUTED)
            d.arrow([(x-85,244),(x-140,244),(x-140,150),(x-126,150)],BLUE,1.8)
        else:
            d.arrow([(x,292),(x,269)],BLUE,1.8)
            d.circle(x,244,24,PG,GREEN,1.5)
            d.text(x,237,'Q' if j==0 else 'V',23,True,GREEN)
            d.text(x,200,'Action-value critic' if j==0 else 'State-value critic',20,False,MUTED)
            d.arrow([(x,188),(x,173)],BLUE,1.8)
        d.box(x-124,129,248,42,['Deterministic actor' if j<2 else 'Stochastic actor'],PALE,21)
        d.text(x,108,['Policy gradient through Q','Delayed update through Q1','Advantages + clipped PPO'][j],18,False,MUTED)
    d.line([(0,88),(1000,88)],BORDER,1.5)
    d.words(0,58,['Local execution','in each agent'],20,bold=True,align='left')
    d.text(350,39,'Local observation',21)
    d.arrow([(444,46),(508,46)],BLUE,2)
    d.box(514,25,198,42,['Trained actor'],PALE,21)
    d.arrow([(718,46),(783,46)],BLUE,2)
    d.text(850,39,'Action',22,True,GREEN)
    d.c.setSubject('One-agent critic and actor update in MADDPG, MATD3 and MAPPO. Shared local-execution pattern. Target networks and exploration omitted.')
    d.end()

if __name__=='__main__':
    mechanisms();actor_critics()
