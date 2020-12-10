import pygame as p
from pygame import mixer
import random as r
import sys
import gameover
import gamewin
import nivel
import math as m
import numpy as np
def c1():
    p.init()
    x,y=1280,720
    pantalla=p.display.set_mode((x,y))
    p.display.set_caption("Turret Madness")
    font=p.font.Font('Fuentes\\raidercrusadercond.ttf',30)
    Dialogo0=["Felicitaciones por su última misión soldados, han defendido bastante bien la tierra de las manos de esos inmundos", "aliens."]
    Dialogo1=["Sin embargo los daños colaterales en una geuerra son inevitables.",""]
    Dialogo2=["Por lo tanto es nuestra misión eliminar a los enemigos que estén causando estragos en nuestra galaxia. No podemos", "permitir que se salgan con la suya."]
    Dialogo3=["Los invito soldados, a hacer un contraataque.",""]
    k1,k2=0,0
    countc=0
    n=0
    Fondos=[]
    for i in range(4):
        Fondos.append(p.image.load("images/Historia/30"+str(i)+".png").convert())
    def mostrartext(texto,k,x,y,c=[1,1,1]):
        t=font.render(texto[0:int(k)],True,(c[0]*255,c[1]*255,c[2]*255))
        pantalla.blit(t,(int(x),int(y)))
    t=font.render("Presiona 'esc' para omitir.",True,(255,255,255))
    Dialogos=[Dialogo0,Dialogo1,Dialogo2,Dialogo3]
    trans1,trans2=0,0
    cin=True
    while cin:
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                cin=False
                sys.exit()
            if event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    cin=False
                    break
        pantalla.fill((0,0,0))
        if k1<len(Dialogos[n][0]):
            k1+=1
        else:
            if k2<len(Dialogos[n][1]):
                k2+=1
            else:
                if countc<300:
                    countc+=1
                else:
                    countc=0
                    k1,k2=0,0
                    n+=1
                    trans2,trans1=255,0
                    if n==4:
                        cin=False
                        break
        if n>0:
            Fondos[n-1].set_alpha(int(trans2))
            pantalla.blit(Fondos[n-1],(0,0))
        Fondos[n].set_alpha(int(trans1))
        pantalla.blit(Fondos[n],(0,0))
        if trans2>5:
            trans2-=5
        else:
            if trans1<255:
                trans1+=3
        mostrartext(Dialogos[n][0],k1,20,600)
        mostrartext(Dialogos[n][1],k2,20,650)
        pantalla.blit(t,(10,10))
        p.display.update()
def c2():
    p.init()
    x,y=1280,720
    pantalla=p.display.set_mode((x,y))
    p.display.set_caption("Turret Madness")
    font=p.font.Font('Fuentes\\raidercrusadercond.ttf',30)
    Dialogo0=["Muy bien soldado, excelente misión hemos hecho allá, eh, muchas gracias por salvarnos del ataque de estos Aliens.", "todo es gracias a tí.",""]
    Dialogo1=["Ahora el universo podra respirar en paz y si alguna vez volvemos a ver a estos aliens, te tenemos a tí para", "vencerlos."]
    Dialogo2=["Ve a descansar con los tuyos y con tu familia soldado, lo mereces.", "Es hora de volver a casa."]
    Dialogo3=["Oh shit                                                             ", "here we go again..."]
    k1,k2=0,0
    countc=0
    n=0
    Fondos=[]
    for i in range(4):
        Fondos.append(p.image.load("images/Historia/31"+str(i)+".png").convert())
    def mostrartext(texto,k,x,y,c=[1,1,1]):
        t=font.render(texto[0:int(k)],True,(c[0]*255,c[1]*255,c[2]*255))
        pantalla.blit(t,(int(x),int(y)))
    t=font.render("Presiona 'esc' para omitir.",True,(255,255,255))
    Dialogos=[Dialogo0,Dialogo1,Dialogo2,Dialogo3]
    trans1,trans2=0,0
    cin=True
    while cin:
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                cin=False
                sys.exit()
            if event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    cin=False
                    break
        pantalla.fill((0,0,0))
        if k1<len(Dialogos[n][0]):
            k1+=1
        else:
            if k2<len(Dialogos[n][1]):
                k2+=1
            else:
                if countc<300:
                    countc+=1
                else:
                    countc=0
                    k1,k2=0,0
                    n+=1
                    trans2,trans1=255,0
                    if n==4:
                        cin=False
                        break
        if n>0:
            Fondos[n-1].set_alpha(int(trans2))
            pantalla.blit(Fondos[n-1],(0,0))
        Fondos[n].set_alpha(int(trans1))
        pantalla.blit(Fondos[n],(0,0))
        if trans2>5:
            trans2-=5
        else:
            if trans1<255:
                trans1+=3
        mostrartext(Dialogos[n][0],k1,20,600)
        mostrartext(Dialogos[n][1],k2,20,650)
        pantalla.blit(t,(10,10))
        p.display.update()

def game(controles=True,volumen=0.2):
    Save=open("Save.txt","r")
    state1=Save.readline()
    st1=Save.readline()
    state2=Save.readline()
    st2=Save.readline()
    state3=Save.readline()
    st3=Save.readline()
    Save.close()
    countent=1
    def draw_txt(texto, font, color, surface, x, y):
        textobj=font.render(texto, True, color)
        textrect=textobj.get_rect(center=(x,y))
        surface.blit(textobj,textrect)
    class Torreta:
        def __init__(self,x,y,salud,salud_total=1):
            self.x=int(x)
            self.y=int(y)
            self.salud=salud
            self.salud_total=salud_total
        def mostrar(self,img,i=0,di=0):
            if isinstance(img,int):
                return self
            else:
                if isinstance(img,list):
                    centro=img[i//di].get_rect(center=(self.x,self.y))
                    pantalla.blit(img[i//di],centro)
                else:
                    centro=img.get_rect(center=(self.x,self.y))
                    pantalla.blit(img,centro)
                return self
        def vida(self):
            p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-50,80,10))
            p.draw.rect(pantalla,(0,255,0),(self.x-40,self.y-50,int(80*self.salud/self.salud_total),10))
            return self
    class bala:
        def __init__(self,x,y,n):
            self.x=x
            self.x2=x
            self.y=y
            self.y2=y
            self.tipo=n
        def mostrar(self,img,a,l,colision1=False):
            if l==0 or l==6:
                velbal=0
            elif l==1:
                velbal=4
            elif l==2:
                velbal=6
            elif l==3:
                velbal=8
            elif l==4:
                velbal=10
            elif l==5:
                velbal=12
            else:
                velbal=0
            if self.x<=1280:
                self.x+=4*velbal
                if self.x>=self.x2:
                    centro=img.get_rect(center=(int(self.x),int(self.y)))
                    pantalla.blit(img,centro)
                    if colision1:
                        if l!=6 and l!=-1:
                            self.x=self.x2-(1280-self.x)
            else:
                self.x=self.x2
            return self
    class Hand:
        def __init__(self, x , y):
            self.x=int(x)
            self.y=int(y)
        def mostrar(self,img,i=0,di=0,a=0):
            if isinstance(img,list):
                manita=p.transform.rotozoom(img[i//di],a,1)
                centro=manita.get_rect(center=(self.x,self.y))
                pantalla.blit(manita,centro)
            else:
                manita=p.transform.rotozoom(img,a,1)
                centro=manita.get_rect(center=(self.x,self.y))
                pantalla.blit(manita,centro)
            return self   
        def cuadrado(self):
            if self.y!=150:
                p.draw.rect(pantalla,(255,0,0),(self.x+25,self.y-40,80,80),4)
            else:
                p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-105,80,80),4)
            return self
        def select(self):
            return self.x+25,self.y-40,False
    class celda:
        def __init__(self,x,y,vacia=True):
            self.x=int(x)
            self.y=int(y)
            self.state=vacia
        def mostrar(self,img,salud=100,salud_total=1):
            if self.state:
                p.draw.rect(pantalla,(50,50,50),(self.x,self.y,80,80),4)
            else:
                PP=Torreta(self.x+40,self.y+40,salud,salud_total)
                PP.mostrar(img).vida()
            return self
    class enemigo:
        def __init__(self,x,y,vida,salud_total):
            self.x=x
            self.y=y
            self.v=vida
            self.salud_total=salud_total
        def mostrar(self,img,i=0,di=0):
            if isinstance(img,int):
                return self
            else:
                if isinstance(img,list):
                    centro=img[i//di].get_rect(center=(self.x,self.y))
                    pantalla.blit(img[i//di],centro)
                else:
                    centro=img.get_rect(center=(self.x,self.y))
                    pantalla.blit(img,centro)
                return self
        def colision1(self,kk,mm,l):
            if l!=6:
                r=30
            else:
                r=200
            if ((self.x-kk)**2+(self.y-mm)**2)<=r**2:
                return True
            else:
                return False
        def vida(self,daño=0):
            p.draw.rect(pantalla,(255,0,0),(self.x-40,self.y-50,80,10)) 
            if self.v>0:
                p.draw.rect(pantalla,(0,255,0),(self.x-40,self.y-50,int(80*self.v/self.salud_total),10))
            else:
                p.draw.rect(pantalla,(0,255,0),(self.x-40,self.y-50,0,10))
            return self
        def colision(self,o1,o2):
            if (o1.x-self.x)**2+(self.y-o1.y)**2<=50:
                return True
            else: 
                return False
            if o2.x-50<=self.x<=o2.x+50:
                return True
            else: 
                return False
         
    #Inicio de declaración de variables
    p.init()
    p.display.set_caption("Tower-Madness")
    mixer.init()
    Aliensound=mixer.Sound("Sound\\Aliens.wav")
    soundselect=mixer.Sound("Sound\\select.wav")
    soundmano=mixer.Sound("Sound\\hand.wav")
    pausesound=mixer.Sound("Sound\\message.ogg")
    bomba=mixer.Sound("Sound\\bombexplosion.ogg")
    mixer.music.load("Sound\\airship.mp3")
    mixer.music.set_volume(volumen*1.5)
    mixer.music.play(-1)
    canalAliens=mixer.Channel(0)
    canalAliens.set_volume(volumen)
    canalselect=mixer.Channel(1)
    canalmano=mixer.Channel(2)
    canalpause=mixer.Channel(3)
    canalbomba=mixer.Channel(4)
    canalmano.set_volume(volumen)
    canalpause.set_volume(volumen)
    canalbomba.set_volume(volumen)
    daño=[0,10,20,30,40,50,60,0]
    clock=p.time.Clock()
    angulo=0
    salud=[]
    dinero=7000
    xhand,yhand=50,150
    est=(0,0,0)
    est1=(0,0,0)
    pantalla=p.display.set_mode((1280,720))
    p.display.set_caption("Turret Madness")
    fondo=p.image.load("images\\Fondo3.png").convert()
    fondo_pause=p.image.load("teclado\\fondo_pausa.jpg").convert_alpha()
    boton=p.image.load("images\\boton.png")
    fondo_pause=p.transform.rotozoom(fondo_pause,0 , 0.3)
    cfondo=fondo.get_rect(center=(int(1280/2),int(720/2)))
    moverd,movera,moverr,moverl=False,False,False,False
    celdas=[]
    turrets=[]
    usable=[]
    balimg=[]
    vida=[1000,200,300,400,500,600,800]
    daño_enemigos=[1,2,3,4]
    vidturr=0
    vid=0
    a=[]
    sal=[]
    balas=[]
    nb=-1
    turr=-1
    superficies=[]

    #Explosión
    Explo=[]
    exp=[]
    countexp=[]
    for i in range(24):
        Explo.append(p.image.load("images\\Exp\\Exp"+str(i)+".png").convert_alpha())

    #torretas
    for i in range(7):
        usable.append(False)
        turrets.append(p.image.load("images\\Torreta"+str(i)+".png"))
        if 0<=i<=2 or i==6:
            balimg.append(p.image.load("images\\Balas\\0.png"))
        else:
            balimg.append(p.image.load("images\\Balas\\"+str(i)+".png"))
    
    #Mano
    manoimg=p.image.load("images\\Mano.png")
    for i in range(75,976,150):
        for j in range(210,611,100):
            exp.append(False)
            exp.append(False)
            countexp.append(0)
            countexp.append(0)
            salud.append(0)
            salud.append(0)
            balas.append(bala(i+50,j+30,0))
            sal.append(0)
            sal.append(0)
            a.append(-1)
            a.append(-1)
            celdas.append((i,j))
            celdas.append(celda(i,j,True))
            superficies.append(p.Rect(i,j,80,80))

    #Menú
    menu=[]
    mx=[90,240,390,540,690,840,990]
    for i in range(14):
        menu.append(p.image.load("images\\MenuT"+str(i)+".png"))

    #Aliens
    Aliens=[]
    Alien1=[]
    Alien2=[]
    Alien3=[]
    Alien4=[]
    Alien1attack=[]
    Alien2attack=[]
    Alien3attack=[]
    Alien4attack=[]
    Alien1death=[]
    Alien2death=[]
    Alien3death=[]
    Alien4death=[]
    vel=[]
    enemigos=[]
    vidaenemigo=[]
    vidaenemigototal=[]
    al,al1=0,0
    X=[]
    Y=[]
    N=[]
    countenemigos=[]
    countcambio=[]
    for i in range(4,11):
        Alien1attack.append(p.image.load("images\\Alien1"+str(i)+".png").convert_alpha())
        Alien2attack.append(p.image.load("images\\Alien2"+str(i)+".png").convert_alpha())
        Alien3attack.append(p.image.load("images\\Alien3"+str(i)+".png").convert_alpha())
        Alien4attack.append(p.image.load("images\\Alien4"+str(i)+".png").convert_alpha())
    for i in range(4):
        Alien1.append(p.image.load("images\\Alien1"+str(i)+".png").convert_alpha())
        Alien2.append(p.image.load("images\\Alien2"+str(i)+".png").convert_alpha())
        Alien3.append(p.image.load("images\\Alien3"+str(i)+".png").convert_alpha())
        Alien4.append(p.image.load("images\\Alien4"+str(i)+".png").convert_alpha())
    for i in range(11,13):
        Alien1death.append(p.image.load("images\\Alien1"+str(i)+".png").convert_alpha())
        Alien2death.append(p.image.load("images\\Alien2"+str(i)+".png").convert_alpha())
        Alien3death.append(p.image.load("images\\Alien3"+str(i)+".png").convert_alpha())
        Alien4death.append(p.image.load("images\\Alien4"+str(i)+".png").convert_alpha())

    for i in range(15): #Esta variable controla el número de enemigos en el tablero
        vidaenemigo.append(300)
        vidaenemigototal.append(300)
        n=3
        countcambio.append(0)
        N.append(n)
        Aliens.append(Alien3)
        vel.append(5)
        X.append(1280+i*1000+300)
        Y.append(240+r.randint(0,4)*100)
        countenemigos.append(0)
    for i in range(50):
        n=r.randint(1,2)
        N.append(n)
        Aliens.append(eval("Alien"+str(n)))
        Y.append(240+r.randint(1,2)*100)
        countenemigos.append(0)
        X.append(1280+i*r.randint(100,1000)+300)
        if n==1:
            vel.append(5.5)
            vidaenemigototal.append(250)
            vidaenemigo.append(250)
        elif n==2:
            vel.append(4.5)
            vidaenemigototal.append(400)
            vidaenemigo.append(400)
    for i in range(25):
        vidaenemigo.append(600)
        vidaenemigototal.append(600)
        n=4
        N.append(n)
        Aliens.append(Alien4)
        vel.append(4)
        X.append(1280+i*1000+300)
        Y.append(240+r.randint(0,4)*100)
        countenemigos.append(0)

    
    #Nucleo
    pilar,cpilar=p.image.load("images\\Nucleo\\Pilar.png"),[]
    esfera=[]
    estadonucleo=[]
    nucleoimg=[]
    yn=[]
    xn=[]
    vn=[]
    countnucleo,countndest=0,[]
    destruir=[]
    cnucleo=[]
    for i in range(8):
        if i<5:
            destruir.append(p.image.load("images\\Nucleo\\D"+str(i)+".png"))
        nucleoimg.append(p.image.load("images\\Nucleo\\"+str(i)+".png"))
        esfera.append(p.image.load("images\\Nucleo\\E"+str(i)+".png"))
    for i in range(5):
        countndest.append(0)
        estadonucleo.append(0)
        xn.append(40)
        vn.append(30)
        yn.append(240+i*100)
        cpilar.append(nucleoimg[i].get_rect(center=(xn[i],yn[i])))
        cnucleo.append(nucleoimg[i].get_rect(center=(xn[i],yn[i])))

    #Guardado
    save=False

    #Cinemática
    cin=True

    #Pausa
    font=p.font.Font("Fuentes\\raidercrusadersemistraight.ttf",32)
    cp=0
    pause=False
    Pausado="PAUSA"
    color=1
    def Pause(a,color):
        hola=font.render(a,True,(color*255,color*255,color*255))
        cent=hola.get_rect(center=(int(1280/2),int(720/2-100)))
        pantalla.blit(hola,cent)
    fondoent=p.image.load("images\\fondo.png").convert()
    pause=False
    Run=True
    click=False
    while Run:
        casilla=False
        if cin:
            c1()
            cin=False
            canalAliens.play(Aliensound,-1)
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                p.quit()
                sys.exit()
            if event.type==p.KEYDOWN:
                if event.key == p.K_s or event.key == p.K_DOWN:
                    if not moverd and not controles:
                        moverd = True
                elif event.key == p.K_w or event.key == p.K_UP:
                    if not movera and  not controles:
                        movera = True
                elif event.key == p.K_a or event.key == p.K_LEFT:
                    if not moverl and not controles:
                        moverl = True
                elif event.key == p.K_d or event.key == p.K_RIGHT:
                    if not moverr and not controles:
                        moverr = True
                elif event.key== p.K_RETURN:
                    est=mano.select()
                    canalselect.play(soundselect)
                elif event.key== p.K_BACKSPACE:
                    est1=mano.select()
                elif event.key== p.K_ESCAPE:
                    canalpause.play(pausesound)
                    pause=True
            elif event.type==p.MOUSEBUTTONDOWN:
                if event.button==1 and controles:
                    est=mano.select()
                    canalselect.play(soundselect)
                if event.button==3 and controles:
                    est1=mano.select()
        Mx,My=p.mouse.get_pos()
        
        pantalla.blit(fondo,cfondo)
        p.draw.rect(pantalla,(0,0,0),(75,150,1000,30))
        p.draw.rect(pantalla,(50,50,50),(80,155,990,20))
        p.draw.rect(pantalla,(143,49,255),(80,155,int(990*dinero/7000),20))
        if dinero<7000:
            dinero+=100
        for l in range(1,7):
            p.draw.rect(pantalla,(0,0,0),(int(80+990*l/7),155,5,20))
        botones_menu=[]

        #Celdas y menú
        for i in range(70):
            if i%2!=0:
                for j in range(7):
                    if (dinero-1000)/1000<j:
                        botones_menu.append(pantalla.blit(menu[j+7],(mx[j],45)))
                        usable[j]=False
                    else:
                        usable[j]=True
                        botones_menu.append(pantalla.blit(menu[j],(mx[j],45)))            
                    if est[0]-65==mx[j] and est[1]==110:
                        if usable[j]:
                            turr=turrets[j]
                            nb=j
                            vidturr=vida[j]
                            vid=vida[j] 
                if a[i-1]!=-1:
                    balas[i//2].mostrar(balimg[a[i-1]],True,a[i-1])
                    for h in range(len(N)): 
                        if enemigos[h].colision1(balas[i//2].x,balas[i//2].y,a[i-1]):
                            if a[i-1]==6:
                                canalbomba.play(bomba)
                                vidaenemigo[h]=0
                                a[i-1]=-1
                                a[i]=-1
                                salud[i]=0
                                exp[i]=True
                                celdas[i].state=True
                            if balas[i//2].x>=balas[i//2].x2:
                                vidaenemigo[h]-=daño[a[i-1]]
                            balas[i//2].mostrar(balimg[a[i-1]],False,a[i-1],True)
                            if vidaenemigo[h]<=0:
                                nivel.contadormuertes +=1
                                X[h]=5000
                                Y[h]=5000
                                countenemigos[h]=1
                if exp[i]:
                    if countexp[i]<len(Explo)-1:
                        countexp[i]+=1
                        pantalla.blit(Explo[int(countexp[i])],(int(celdas[i].x)-10,int(celdas[i].y-40)))
                    else:
                        countexp[i]=0
                        exp[i]=False
                celdas[i].mostrar(a[i],salud[i],sal[i])  
            else:
                if (est[0]==celdas[i][0] and est[1]==celdas[i][1]):
                    if celdas[i+1].state:
                        a[i+1]=turr
                        a[i]=nb
                        sal[i+1]=vidturr
                        salud[i+1]=vid
                    if a[i+1]!=-1 and a[i]!=-1:
                        if not usable[nb]:
                            vid=0
                            nb=-1
                            turr=-1
                        if celdas[i+1].state:
                            dinero-=(nb+1)*1000
                            celdas[i+1]=celda(est[0],est[1],est[2])
                    est=(0,0,0)
                elif est1[0]==celdas[i][0] and est1[1]==celdas[i][1]:
                    a[i+1]=-1
                    a[i]=-1
                    salud[i+1]=0
                    celdas[i+1]=celda(est1[0],est1[1],True)
                    est1=(0,0,0)
                if celdas[i+1].state:
                    a[i+1]=-1
                    a[i]=-1
                    salud[i+1]=0
                    celdas[i+1]=celda(celdas[i][0],celdas[i][1],True)
                    
        #Nucleo
        if countnucleo<len(nucleoimg)-0.4:
            countnucleo+=0.4
        else:
            countnucleo=0
        for i in range(5):
            cnucleo[i]=nucleoimg[i].get_rect(center=(xn[i],yn[i]))
            if estadonucleo[i]==0:
                pantalla.blit(nucleoimg[int(countnucleo)],cnucleo[i])
                for k in range(len(Aliens)):
                    if abs(xn[i]-X[k])<40 and yn[i]==Y[k]:
                        estadonucleo[i]=1
            elif estadonucleo[i]==1:
                for k in range(len(Aliens)):
                    if abs(xn[i]-X[k])<40 and yn[i]==Y[k]:
                        X[k]=5000
                        Y[k]=5000
                        nivel.contadormuertes +=1
                        countenemigos[k]=1
                    if X[k]<20:
                        estadonucleo[i]=2
                pantalla.blit(pilar,cpilar[i])
                if xn[i]<1240:
                    xn[i]+=vn[i]
                    pantalla.blit(esfera[int(countnucleo)],cnucleo[i])
                else:
                    if countndest[i]<len(destruir)-0.2:
                        if xn[i]!=5000:
                            if countndest[i]<0.9:
                                countndest[i]+=0.1
                            else:
                                countndest[i]+=0.2
                            pantalla.blit(destruir[int(countndest[i])],cnucleo[i])
                    else:
                        xn[i],yn[i]=5000,5000
            elif estadonucleo[i]==2:
                pantalla.blit(pilar,cpilar[i])
                nivel.levelok = 3
                nivel.contadormuertes = 0
                gameover.main_menu()
                estadonucleo[i]=3              
            elif estadonucleo[i]==3:
                pantalla.blit(pilar,cpilar[i])
                estadonucleo=[0,0,0,0,0]
                yn=[240,340,440,540,640]
                xn=[40,40,40,40,40]

        if movera or moverd or moverl or moverr:
            canalmano.play(soundmano)

        #Mover la mano
        if moverd:
            yhand+=100
            moverd=False
        elif movera:
            yhand-=100
            movera=False
        elif moverl:
            xhand-=150
            moverl=False
        elif moverr:
            xhand+=150
            moverr=False
        if yhand<=150:
            angulo=90
            yhand=150
            mano=Hand(xhand+80,yhand)
        elif yhand>650:
            yhand=650
        else:
            mano=Hand(xhand,yhand)
            angulo=0
        if xhand<50:
            xhand=50
        elif xhand>950:
            xhand=950
        mano.mostrar(manoimg,0,0,angulo).cuadrado()
        if controles:
            for i in range(7):
                if botones_menu[i].collidepoint((Mx,My)):
                    xhand=mx[i]-40
                    yhand=150                  
            for i in range(35):
                if i%2==0:
                    if superficies[i].collidepoint((Mx,My)):
                        
                        xhand=celdas[i*2][0]-25
                        yhand=celdas[i*2][1]+40
                else:
                    if superficies[i].collidepoint((Mx,My)):
                        
                        xhand=celdas[i*2][0]-25
                        yhand=celdas[i*2][1]+40
        if al<len(Alien1)-0.3:
            al+=0.3
        else:
            al=0
        if al1<len(Alien1attack)-0.15:
            al1+=0.15
        else:
            al1=0

        #este pedazo se encarga de mostrar los enemigos caminando
        enemigos=[]
        for i in range(len(Aliens)):
            enemigos.append(enemigo(X[i],Y[i],vidaenemigo[i],vidaenemigototal[i]))
            if vel[i]!=0:
                X[i]-=vel[i]
                if -100<=Y[i]<=820:
                    if N[i]==3:
                        if countcambio[i]==0 and 20<X[i]<1280:
                            if r.randint(0,200)==2:
                                countcambio[i]+=1
                                if 340<=Y[i]<=540:
                                    Y[i]+=100-200*r.randint(0,1)
                                elif Y[i]==240:
                                    Y[i]+=100
                                elif Y[i]==640:
                                    Y[i]-=100
                    if 0<X[i]<1380:
                        enemigos[i].mostrar(eval("Aliens["+str(i)+"][int(al)]")).vida()
        if countenemigos.count(1)==len(N):
            countenemigos[0]=0
            save=True
        
        #Guardado
        if save:
            stars=estadonucleo.count(0)
            Save=open("Save.txt","w")
            Save.close()
            Save=open("Save.txt","a")
            Save.write("Completo\n")
            Save.write(st1)
            Save.write("Completo"+"\n")
            Save.write(int(stars))
            Save.write("Disponible"+"\n")
            Save.write(st3)
            Save.close()
            save=False
            mixer.music.pause()
            canalAliens.pause()
            c2()
            break


        #este pedazo se encarga de las colisiones
        for j in range(0,len(Aliens)):   
            for i in range(6,-1,-1):
                for k in range(1,10,2):
                    if m.sqrt((eval("X"+str([j]))-(185+i*150))**2+(eval("Y"+str([j]))-(celdas[int(str(i)+str(k))-1][1]))**2)<40:
                        if not celdas[int(str(i)+str(k))].state:
                            vel[j]=0
                            if N[j] == 1:
                                enemigos[j].mostrar(Alien1attack[int(al1)]).vida()
                                if salud[int(str(i)+str(k))]>=0:
                                    salud[int(str(i)+str(k))]-=daño_enemigos[N[j]-1]
                                else:
                                    salud[int(str(i)+str(k))]=0
                                    celdas[int(str(i)+str(k))].state=True
                            if N[j] == 2:
                                enemigos[j].mostrar(Alien2attack[int(al1)]).vida()
                                if salud[int(str(i)+str(k))]>=0:
                                    salud[int(str(i)+str(k))]-=daño_enemigos[N[j]-1]
                                else:
                                    salud[int(str(i)+str(k))]=0
                                    celdas[int(str(i)+str(k))].state=True
                            if N[j] == 3:
                                enemigos[j].mostrar(Alien3attack[int(al1)]).vida()
                                if salud[int(str(i)+str(k))]>=0:
                                    salud[int(str(i)+str(k))]-=daño_enemigos[N[j]-1]
                                else:
                                    salud[int(str(i)+str(k))]=0
                                    celdas[int(str(i)+str(k))].state=True
                            if N[j] == 4:
                                enemigos[j].mostrar(Alien4attack[int(al1)]).vida()
                                if salud[int(str(i)+str(k))]>=0: 
                                    salud[int(str(i)+str(k))]-=daño_enemigos[N[j]-1]
                                else:
                                    salud[int(str(i)+str(k))]=0
                                    celdas[int(str(i)+str(k))].state=True
                            PP=Torreta(celdas[int(str(i)+str(k))-1][0]+40,celdas[int(str(i)+str(k))-1][1]+40,salud[int(str(i)+str(k))],vida[a[int(str(i)+str(k))-1]])
                            PP.mostrar(turrets[a[int(str(i)+str(k))-1]]).vida()
                        else:
                            if X[j] <= 1500 and N[j] == 3:
                                vel[j] = 3
                            elif X[j] <= 1500 and N[j] == 2:
                                vel[j] = 3
            X[j]-=vel[j]    

            
        if countent>0:
            countent-=0.05
            fondoent.set_alpha(int(countent*255))
            pantalla.blit(fondoent,(0,0))  
            
        if nivel.contadormuertes == 3:
            nivel.contadormuertes = 0
            gamewin.main_menu()
        
        click=False
        #pausa
        while pause:
            Mx,My=p.mouse.get_pos()
            mixer.music.pause()
            canalAliens.pause()
            if cp<=100:
                cp+=1
            else:
                cp=0
            if cp<=50:
                color=1
            else:
                color=0
            center=fondo_pause.get_rect(center=(1280/2,720/2))
            center_1=boton.get_rect(center=(640,350))
            pantalla.blit(fondo_pause,center)
            boton_1=pantalla.blit(boton,center_1)
            draw_txt("reanudar",font, (0,0,0),pantalla,638,353)
            draw_txt("reanudar",font, (255,255,255),pantalla,640,350)
            Pause(Pausado,color)
            if boton_1.collidepoint((Mx,My)):
                casilla=True
                pantalla.blit(fondo_pause,center)
                Pause(Pausado,color)
                boton_1=pantalla.blit(boton,(center_1[0],center_1[1]-5))
                draw_txt("reanudar",font, (0,0,0),pantalla,638,348)
                draw_txt("reanudar",font, (255,255,255),pantalla,640,345)
                #if k==0:
                    #canal1.play(tap)
                   #k+=1
                if click:
                    mixer.music.unpause()
                    canalAliens.unpause()
                    pause=False
                    break
            for event in p.event.get():
                if event.type== p.QUIT:
                    pause=False
                    Run=False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        if pause==True:
                            canalpause.play(pausesound)
                            mixer.music.unpause()
                            canalAliens.unpause()
                            pause=False
                elif event.type==p.MOUSEBUTTONDOWN:
                    if event.button==1 and casilla:
                        click=True
            clock.tick(60)
            p.display.update()
        clock.tick(60)
        p.display.update()
