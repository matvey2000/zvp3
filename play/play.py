import pygame,os,easygui,pickle,datetime,time,_thread
from distutils.command.config import config
def flips():
    while True:
        pass
class Image:
    def image(self,image,cor,screen):
        self.image=pygame.image.load(image)
        screen.blit(image,cor)


tl=40
class LUKOSTREL:
    def image(self,image,cor,screen):
        self.image=pygame.image.load(image)
        self.cor=cor
        screen.blit(self.image,self.cor)
    def __init__(self):
        global st
        global screen
        global mst_class
        time.sleep(2)
        s=-1
        crs=self.cor
        for i in range(50):
            self.cor=[(self.cor[0]+1),(self.cor[1])]
            screen.blit(self.image,self.cor)
            pygame.display.flip()
        for zb in st:
            s+=1
            if zb[1][1]>=(self.cor[1]-tl) and zb[1][1]<=(self.cor[1]+tl):
                t=st[s]
                t[2]=t[2]-2
            pygame.display.flip()
        time.sleep(1)
        screen.blit(self.image,crs)
        pygame.display.flip()
for i in os.listdir('C:\\Users\\matve\\eclipse-workspace\\play'):
    if not i=='.project' and not i=='.pydevproject' and not i=='play.py':
        print(i)
class ntn:
    def __init__(self):
        self.type='000'
def anal():
    global grstrl
    global st
    for i in st:
        lg=True
        for j in grstrl:
            if grstrl.cor-tl>=i[1] and grstrl.cor+tl<=i[1]:
                lg=False
        if lg :
            easygui.msgbox('вас заметили')
def pole():
    global sln
    global log
    global st
    global rasresh
    global screen
    global bl
    global grstrl
    global k
    pf=pygame.event.get()
    NTN=ntn()
    NTN.__init__()
    pf.append(NTN)
    for event in pf:
        if event.type==pygame.QUIT:
            log=False
        elif event.type==pygame.MOUSEBUTTONUP:
            pos= pygame.mouse.get_pos()
            l=easygui.buttonbox('кого поставить? У вас '+str(sln)+' кристалов.',choices=rasresh)
            pos=[1030,pos[1]]
            s=[l,pos,mst[l]]
            k+=1
            if k==2:
                print('pppp')
            if sln>=mst[l]:
                easygui.msgbox('готово')
                image=pygame.image.load(str(l))
                #s[0]=image
                st.append(s)
                screen.blit(image,pos)
            else:
                easygui.msgbox('нельзя!')
        screen.fill([225,225,225])
        image=pygame.image.load('египет.jpg')
        screen.blit(image,[0,0])
        s=-1
        p=False
        for lukostrel_class_i in mst_class:
                #lukostrel_class_i.__init__()
                pass
        for zb in st:
            s+=1
        
            print(zb,s)
            l=pygame.image.load(zb[0])
            t=st[s]
            t[1]=[(t[1][0]+(-1)),(t[1][1]+(0))]
            st[s]=t
            screen.blit(l,zb[1])
            pygame.display.flip()
            if zb[1][0]<=400:
                st=[]
                sln=0
                return True
                p=True
            lg=False
            lg_2=True
            print('ppppppppppppp')
            anal()
            print('end lukostrel')
            continue
            pygame.display.flip()
def sad():
    pass
try:
    file=open('dst.pkl','rb')
    rasresh=pickle.load(file)
    file.close()
except:
    rasresh=['дремалой.jpg']
    file=open('dst.pkl','wb')
    print(file)
    pickle.dump(rasresh,file)
    file.close()
try:
    file=open('bl.pkl','rb')
    bl=pickle.load(file)
    file.close()
except:
    bl=0
    file=open('bl.pkl','wb')
    print(file)
    pickle.dump(bl,file)
    file.close()
st=[]
rasresh_r=['горохострел.jpeg','солнышко.jpeg']
rst={'горохострел.jpeg':['лук.jpeg',1,'strel'],'картошка.jpeg':['not',10,'stoi'],'солнышко.jpeg':['not',3,'dav']}
mst={'sundak.jpg':30,'ведро.jpg':20,'великан.jpg':100,'дремалой.jpg':5,'зомби конус 1.png':15,'зомби обыкновенный египет 1.jpg':10,'костяшка.jpg':15,'притягатель.jpg':15,'профессор.png':300,'факел.jpg':10,'фараон 1.png':10,'флаг.jpg':12}
log=True
zbm=[]
k=0
for i in mst.keys():
    zbm.append(i)
sln=0
krs=0
grstrl=[]
rast=[]
for ras in rst.keys():
    rast.append(ras)
mst_class=[]
grstrl=[]
screen=pygame.display.set_mode([2000,850])
image=pygame.image.load('египет.jpg')
screen.blit(image,[0,0])
pygame.display.flip()
start=datetime.datetime.timestamp(datetime.datetime.now())
while log:
    sln=100
    krs=100
    l=False
    try:
     if pole():
        bl+=1
        l=True
    except:pass
    if not l:
        end=datetime.datetime.timestamp(datetime.datetime.now())
        if end-start>=5:
            sln+=3
            krs+=3
            start=datetime.datetime.timestamp(datetime.datetime.now())
    if 1==1:
        file=open('dst.pkl','wb')
        pickle.dump(rasresh,file)
        file.close()
        file=open('bl.pkl','wb')
        pickle.dump(bl,file)
        file.close()