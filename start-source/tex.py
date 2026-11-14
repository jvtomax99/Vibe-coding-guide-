# Cover maps for the futuristic book: base color, gold mask, glow mask.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random
import os
F=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fonts','')  # put the three .ttf files here (see README.md)
W,H=1024,1536
def font(n,s,var=None):
    f=ImageFont.truetype(F+n,s)
    if var:
        try: f.set_variation_by_axes(var)
        except Exception as e: print('var',e)
    return f
gold=Image.new('L',(W,H),0); glow=Image.new('L',(W,H),0)
g=ImageDraw.Draw(gold); c=ImageDraw.Draw(glow)
# gold double frame
g.rectangle([56,56,W-56,H-56],outline=255,width=5); g.rectangle([76,76,W-76,H-76],outline=255,width=2)
# title
bod=font('BodoniModa.ttf',132); ins=font('InstrumentSans.ttf',30)
def ctext(d,y,t,f,fill=255,sp=0):
    if sp:
        w=sum(d.textlength(ch,font=f)+sp for ch in t)-sp; x=(W-w)/2
        for ch in t: d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
    else:
        w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=fill)
big=font('BodoniModa.ttf',150)
ctext(g,845,'The Launch',big)
ctext(g,1005,'Manual',big)
g.line([W/2-90,1215,W/2+90,1215],fill=255,width=3)
ctext(g,1330,'BUILDING APPS WITH CLAUDE',ins,sp=10)
ctext(c,150,'A COURSE IN 18 BOOKS',ins,sp=12)
# emblem: rings + 18 dots (glow), open book (gold)
cx,cy=W/2,500
c.ellipse([cx-190,cy-190,cx+190,cy+190],outline=255,width=4)
for rot in (-28,28):
    lay=Image.new('L',(W,H),0); d=ImageDraw.Draw(lay)
    d.ellipse([cx-190,cy-66,cx+190,cy+66],outline=255,width=4)
    lay=lay.rotate(rot,center=(cx,cy),resample=Image.BICUBIC); glow.paste(255,mask=lay)
c=ImageDraw.Draw(glow)
for i in range(18):
    a=i/18*2*math.pi-math.pi/2; x=cx+250*math.cos(a); y=cy+250*math.sin(a); r=9
    c.ellipse([x-r,y-r,x+r,y+r],fill=255)
# open book icon in gold
s=3.4; ox,oy=cx-32*s,cy-33*s
def P(x,y): return (ox+x*s,oy+y*s)
pts=[P(8,18),P(16,14.5),P(24,15),P(32,20),P(40,15),P(48,14.5),P(56,18),P(56,48),P(48,44.5),P(40,45),P(32,50),P(24,45),P(16,44.5),P(8,48),P(8,18)]
g.line(pts,fill=255,width=7,joint='curve'); g.line([P(32,20),P(32,50)],fill=255,width=7)
# circuit traces (glow)
def tr(pts):
    c.line([(x/100*W,y/150*H) for x,y in pts],fill=200,width=4)
    x,y=pts[-1]; c.ellipse([x/100*W-9,y/150*H-9,x/100*W+9,y/150*H+9],fill=255)
for p in ([(8,24),(15,24),(21,30),(21,40)],[(92,33),(86,33),(80,39),(80,47)],[(8,121),(14,121),(20,115),(20,104)],[(92,128),(86,128),(80,122),(80,110)],[(30,142),(30,139),(36,133),(45,133)],[(72,142),(72,140),(66,134)]): tr(p)
gold.save('cover_gold.png'); glow.save('cover_glow.png')
# base: deep navy with fine grain
random.seed(4)
base=Image.new('RGB',(W,H),(9,14,34)); px=base.load()
n=Image.effect_noise((W,H),18).point(lambda v:v)
base=Image.blend(base,Image.merge('RGB',(n,n,n)),0.035)
base.save('cover_base.png')
# first page: paper with a welcome
PW,PH=1024,1536
pg=Image.new('RGB',(PW,PH),(246,239,225)); n=Image.effect_noise((PW,PH),10); pg=Image.blend(pg,Image.merge('RGB',(n,n,n)),0.03)
d=ImageDraw.Draw(pg)
def pc(y,t,f,fill):
    w=d.textlength(t,font=f); d.text(((PW-w)/2,y),t,font=f,fill=fill)
pc(430,'Welcome aboard.',font('PinyonScript.ttf',150),(150,18,40))
bd=font('BodoniModa.ttf',62)
for i,t in enumerate(['Take a book from the shelf','and start where you like.']): pc(690+i*86,t,bd,(31,22,19))
d.line([PW/2-70,930,PW/2+70,930],fill=(154,106,51),width=3)
pc(990,'18 SHORT BOOKS',font('InstrumentSans.ttf',34),(123,106,93))
pg.save('page.png')
print('ok')
