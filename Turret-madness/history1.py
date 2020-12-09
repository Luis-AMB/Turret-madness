# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 04:03:17 2020

@author: familia
"""
import pygame as p
from pygame import mixer
def historia():    
    p.init()
    #p.mixer.music.load("")
    mixer.init()
    mixer.music.set_volume(0.3)
    letras=mixer.Sound("Sound\\sonidot.mp3")
    mixer.music.load("Sound\\cancion1.mp3")
    mixer.music.play(-1)
    letrass=mixer.Channel(1)
    
    planeta1=p.image.load("images//invasion//planeta0.jpg")
    invasion1=p.image.load("images//invasion//superficie.jpg")
    torresp=p.image.load("images//invasion//torresplaneta.jpg")
    fondo=p.image.load("images//invasion//fondo.jpg")
    cuadro0=p.image.load("images//cuadro0.png")
    cuadro11=p.image.load("images//cuadro11.png")
    cuadro12=p.image.load("images//cuadro12.png")
    cuadro111=p.image.load("images//cuadro111.png")
    cuadro112=p.image.load("images//cuadro112.png")
    torresplaneta0=p.image.load("images//invasion//torresplaneta0.jpg")
    aliensplaneta=p.image.load("images//invasion//aliensplaneta.jpg")
    x0,x1,x2,x3,x4,x01,x02=0,210,110,710,350,0,0
    y0,y1,y2,y3,y4,y01,y02=600,500,460,460,430,600,600
    t1,t2,t3,t4,t5,t01,t02=0,150,630,780,960,330,420
    a0,a1,a2,a3,a4,a01,a02=[],[],[],[],[],[],[]
    k,contador1,contador2,contador3,contador4,contador5,contador01,contador02=0,0,0,0,0,0,0,0 
    guion0,guion1,guion2,guion3,guion4,guion01,guion02=[],[],[],[],[],[],[]
    guion1.append("Planeta Surata.")
    guion1.append("2.200 años despues de la guerra universal.")
    guion1.append("Un millon de años luz de la Tierra.")
    guion0.append("En el año 2.200 los Crixos descubrieron el planeta Surata")
    guion0.append("el cual tiene una superficie rocosa y desertica con clima muy calido,")
    guion01.append("en el habitan unos seres vivos con forma de torretas.")
    guion02.append("Los crixos son una especie alienigena aniquiladora que")
    guion02.append("viajan por el universo en busca de recursos y alimento,")
    guion02.append("acabando con los planetas y destruyendo toda forma de vida.")
    guion2.append("¡Invadiremos el planeta Surata!,")
    guion2.append("nos llevaremos todos los suministros alimenticios,")
    guion2.append("destruiremos todas las bases de las torretas.")
    guion3.append("No permitiremos que nos destruyan,")
    guion3.append("nuestra base resistira las oleadas alienigenas,")
    guion3.append("¡salvaremos este planeta de la extincion!.")
    guion4.append("Tu mision es defender el planeta Surata")
    guion4.append("de la invasion alienigena, para ello debes")
    guion4.append("posicionar las torretas de forma estrategica,")
    guion4.append("evitando que los alienigenas lleguen a tu base.")
    suma=0
    escrito=["",""]
    escrito01=[""]
    escrito02=["","",""]
    escrito1=["","",""]
    escrito2=["","",""]
    escrito3=["","",""]
    escrito4=["","","",""]
    pantalla=p.display.set_mode((1280,720))
    Run=True
    p.display.set_caption("Turret Madness")
    robot=[]
    alien=[]
    torretas=[]
    mifuente=p.font.SysFont("Cambria",20)
    clock=p.time.Clock()
    mostrar_t=[True,False]
    mostrar_t01=[True]
    mostrar_t02=[True,False,False]
    mostrar_t1=[True,False,False]
    mostrar_t2=[True,False,False]
    mostrar_t3=[True,False,False]
    mostrar_t4=[True,False,False,False]
    class textos:
        def __init__(self,x,y):
            self.x=x
            self.y=y
        def guiones(self,guione):
            guion_t=guione.split()
            for i in range(2*len(guion_t)):
                if i%2==1:
                    guion_t.insert(i,"")
            guion=[]
            for i in range(len(guion_t)):
                if len(guion_t[i])==0:
                    guion.append("")
                for j in range(len(guion_t[i])):
                    guion.append(guion_t[i][j])
            return guion
        def escribir_g(self,gui,w,gu,mmm=0):
            if (w-mmm)<len(gui):
                if len(gui[w-mmm-1])==0:
                    gu=gu+" "+gui[w-mmm]
                else:
                    gu=gu+gui[w-mmm]
            return gu
        def texto(self,escr):
            return mifuente.render(escr,50,(255,255,0))
        def cordenadas(self):
            return (self.x,self.y)
        def sumatt(self,sumas,cc):
            for i in range(len(cc)):
                sumas=sumas+cc[i]
            return sumas
        #kk=a0,zz=mostrar_t
        def mostrar(self,z,kk,zz,verdad=False):
            if z==(self.sumatt(suma,kk)+20):
                for i in range(len(zz)):
                    zz[i]=False
            if len(kk)>=2:
                if z==kk[0]:
                    zz[1]=True
            if len(kk)>=3:
                if z==(kk[0]+kk[1]):
                    zz[2]=True
            if len(kk)>=4:
                if z==(kk[0]+kk[1]+kk[2]):
                    zz[3]=True
            if len(kk)>=5:
                if z==(kk[0]+kk[1]+kk[2]+kk[3]):
                    zz[4]=True
            if len(kk)>=6:
                if z==(kk[0]+kk[1]+kk[2]+kk[3]+kk[4]):
                    zz[5]=True
        #o=a0
        def sumatoria(self,o,p,sumat=0):
            for s in range(p):
                sumat=sumat+o[s]
            return sumat
        #mm=mostrar_t,nn=escrito
        def mostrart(self,mm,nn,h=0):
            if mm[0]:            
                pantalla.blit(self.texto(nn[0]),self.cordenadas())
                h=0
            for j in range(1,len(mm)):
                if mm[j]:
                    h+=20
                    pantalla.blit(self.texto(nn[j]),(self.x,self.y+h)) 
    class escribir:
        def __init__(self,d2,d3,d4,d5,d6,hh):
            self.d2=d2
            self.d3=d3
            self.d4=d4
            self.d5=d5
            self.d6=d6
            self.hh=hh
        def resumen(self):
            self.hh.mostrar(self.d2,self.d3,self.d4)
            for i in range(len(self.d4)):
                if i==0:
                    self.d5[0]=self.d5[0]+self.hh.escribir_g(self.hh.guiones(self.d6[0]),self.d2,"")
                else:
                    if self.d4[i]:
                        self.d5[i]=self.d5[i]+self.hh.escribir_g(self.hh.guiones(self.d6[i]),self.d2,"",self.hh.sumatoria(self.d3,i))
    class añadir:
        def __init__(self,hh):
            self.hh=hh
        def insertar(self,q1,q2):
            for d in range(len(q2)):
                q1.append(len(self.hh.guiones(q2[d])))
    ll=textos(x0,y0)
    p0=añadir(ll)
    p0.insertar(a0,guion0)
    ff=textos(x1,y1)
    p1=añadir(ff)
    p1.insertar(a1,guion1)
    qq=textos(x2,y2)
    p2=añadir(qq)
    p2.insertar(a2,guion2)
    ww=textos(x3,y3)
    p3=añadir(ww)
    p3.insertar(a3,guion3)
    ee=textos(x4,y4)
    p4=añadir(ee)
    p4.insertar(a4,guion4)
    l01=textos(x01,y01)  
    p01=añadir(l01)
    p01.insertar(a01,guion01)
    l02=textos(x02,y02)  
    p02=añadir(l02)
    p02.insertar(a02,guion02)
    for i in range(5):
        robot.append(p.image.load("images\\Historia\\historia1"+str(i)+".jpg"))
    for i in range(9):
        alien.append(p.image.load("images\\Historia\\historia2"+str(i)+".jpg"))
    for i in range(2):
        torretas.append(p.image.load("images\\Historia\\historia3"+str(i)+".jpg"))
    while Run:
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                p.quit()
        if k>t2:
            #d1=ll d2=k d3=a0 d4=mostrar_t[] d5=escrto[] d6=guion0[]
            g1=escribir(contador5,a0,mostrar_t,escrito,guion0,ll)
            g1.resumen()
            if k>t2 and k<=(t2+100):
                letrass.play(letras)
        if k>t1:
            g2=escribir(contador1,a1,mostrar_t1,escrito1,guion1,ff)
            g2.resumen()
            if k>t1 and k<=(t1+80):
                letrass.play(letras)
        if k>t3:
            g3=escribir(contador2,a2,mostrar_t2,escrito2,guion2,qq)
            g3.resumen()
            if k>t3 and k<=(t3+100):
                letrass.play(letras)
        if k>t4:
            g4=escribir(contador4,a3,mostrar_t3,escrito3,guion3,ww)
            g4.resumen()
            if k>t4 and k<=(t4+100):
                letrass.play(letras)
        if k>t5:
            g5=escribir(contador3,a4,mostrar_t4,escrito4,guion4,ee)
            g5.resumen()
            if k>t5 and (k<=t5+150):
                letrass.play(letras)
        if k>t01:
            g01=escribir(contador01,a01,mostrar_t01,escrito01,guion01,l01)
            g01.resumen()
            if k>t01 and k<=(t01+30):
                letrass.play(letras)
        if k>t02:
            g02=escribir(contador02,a02,mostrar_t02,escrito02,guion02,l02)
            g02.resumen()
            if k>t02 and k<=(t02+140):
                letrass.play(letras)
        pantalla.blit(fondo,(0,0))
        if k<=(t2-20):
            pantalla.blit(planeta1,(0,0))
        if k>(t2-20) and k<180:
            pantalla.blit(invasion1,(0,0))
            pantalla.blit(cuadro0,(x0,y0))
        if k>=180 and k<300:
            pantalla.blit(torresp,(0,0))
            pantalla.blit(cuadro0,(x0,y0))
        if k>=300 and k<400:
            pantalla.blit(torresplaneta0,(0,0))
            pantalla.blit(cuadro0,(x01,y01))
        if k>=400 and k<630:
            pantalla.blit(aliensplaneta,(0,0))
            pantalla.blit(cuadro0,(x02,y02))
        if k>=630 and k<930:
            pantalla.blit(cuadro11,(100,220))
            pantalla.blit(cuadro11,(700,220))
            pantalla.blit(cuadro111,(x2,y2))
            pantalla.blit(cuadro111,(x3,y3))
            pantalla.blit(alien[1],(110,230))
            pantalla.blit(robot[3],(710,230))
        if k>=930:
            pantalla.blit(cuadro12,(340,190))
            pantalla.blit(cuadro112,(x4,y4))
            pantalla.blit(robot[0],(350,200))
        if k>=1150:
            Run=False
        if k>t1:
            contador1+=1
        if k>t3:
            contador2+=1
        if k>t4:
            contador4+=1
        if k>t5:
            contador3+=1
        if k>t2:
            contador5+=1
        if k>t01:
            contador01+=1
        if k>t02:
            contador02+=1
        ff.mostrart(mostrar_t1,escrito1)
        ll.mostrart(mostrar_t,escrito)
        qq.mostrart(mostrar_t2,escrito2)
        ww.mostrart(mostrar_t3,escrito3)
        ee.mostrart(mostrar_t4,escrito4)
        l01.mostrart(mostrar_t01,escrito01)
        l02.mostrart(mostrar_t02,escrito02)
        clock.tick(12)
        p.display.update()
        k=k+1
historia()