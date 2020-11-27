# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 04:03:17 2020

@author: familia
"""

import pygame as p
def historia():    
    p.init()
    planeta1=p.image.load("images//invasion//planeta0.jpg")
    invasion1=p.image.load("images//invasion//superficie.jpg")
    torresp=p.image.load("images//invasion//torresplaneta.jpg")
    fondo=p.image.load("images//invasion//fondo.jpg")
    x0,x1,x2,x3,x4=100,210,200,800,500
    y0,y1,y2,y3,y4=500,500,500,500,500
    b1,b2,b3,b4,b5=0,600,750,950,150
    a0,a1,a2,a3,a4=[],[],[],[],[]
    k,t,y,n,m,v=0,0,0,0,0,0
    guion0,guion1,guion2,guion3,guion4=[],[],[],[],[]
    guion1.append("Planeta Surata.")
    guion1.append("2.200 años despues de la guerra universal.")
    guion1.append("Un millon de años luz de la Tierra.")
    guion0.append("En el año 2.200 los Crixos descubrieron el planeta Surata")
    guion0.append("el cual tiene una superficie rocosa y desertica con clima muy calido,")
    guion0.append("en el habitan unos seres vivos con forma de torretas.")
    guion0.append("Los crixos son una especie alienigena aniquiladora que")
    guion0.append("viajan por el universo en busca de recursos y alimento,")
    guion0.append("acabando con los planetas y destruyendo toda forma de vida.")
    guion2.append("¡Invadiremos el planeta Surata!,")
    guion2.append("nos llevaremos todos los suministros alimentcios,")
    guion2.append("destruiremos todas las bases de las torretas.")
    guion3.append("No permitiremos que nos destrullan,")
    guion3.append("nuestra base resistira las oleadas alienigenas,")
    guion3.append("¡salvaremos este planeta de la extincion!.")
    guion4.append("Tu mision es defender el planeta Surata de la invasion alienigena,")
    guion4.append("para ello debes posicionar las torretas de forma estrategica,")
    guion4.append("evitando que los alienigenas lleguen a tu base.")
    suma=0
    escrito=["","","","","",""]
    escrito1=["","",""]
    escrito2=["","",""]
    escrito3=["","",""]
    escrito4=["","",""]
    pantalla=p.display.set_mode((1280,720))
    Run=True
    p.display.set_caption("Turret Madness")
    robot=[]
    alien=[]
    torretas=[]
    mifuente=p.font.SysFont("Cambria",20)
    clock=p.time.Clock()
    mostrar_t=[True,False,False,False,False,False]
    mostrar_t1=[True,False,False]
    mostrar_t2=[True,False,False]
    mostrar_t3=[True,False,False]
    mostrar_t4=[True,False,False]
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
        def __init__(self,d2,d3,d4,d5,d6,xx,yy):
            self.d2=d2
            self.d3=d3
            self.d4=d4
            self.d5=d5
            self.d6=d6
            self.xx=xx
            self.yy=yy
        def resumen(self):
            d1=textos(self.xx,self.yy)
            d1.mostrar(self.d2,self.d3,self.d4)
            for i in range(len(self.d4)):
                if i==0:
                    self.d5[0]=self.d5[0]+d1.escribir_g(d1.guiones(self.d6[0]),self.d2,"")
                else:
                    if self.d4[i]:
                        self.d5[i]=self.d5[i]+d1.escribir_g(d1.guiones(self.d6[i]),self.d2,"",d1.sumatoria(self.d3,i))
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
        if k>b5:
            #d1=ll d2=k d3=a0 d4=mostrar_t[] d5=escrto[] d6=guion0[]
            g1=escribir(v,a0,mostrar_t,escrito,guion0,x0,x0)
            g1.resumen()
        if k>b1:
            g2=escribir(t,a1,mostrar_t1,escrito1,guion1,x1,y1)
            g2.resumen()
        if k>b2:
            g3=escribir(y,a2,mostrar_t2,escrito2,guion2,x2,y2)
            g3.resumen()
        if k>b3:
            g4=escribir(m,a3,mostrar_t3,escrito3,guion3,x3,y3)
            g4.resumen()
        if k>b4:
            g5=escribir(n,a4,mostrar_t4,escrito4,guion4,x4,y4)
            g5.resumen()
        pantalla.blit(fondo,(0,0))
        if k<=(b5-20):
            pantalla.blit(planeta1,(0,0))
        if k>(b5-20) and k<350:
            pantalla.blit(invasion1,(0,0))
        if k>=350 and k<550:
            pantalla.blit(torresp,(0,0))
        if k>=550 and k<910:
            pantalla.blit(alien[1],(200,230))
            pantalla.blit(robot[3],(800,250))
        if k>=910:
            pantalla.blit(robot[0],(500,300))
        if k>=1150:
            Run=False
        if k>b1:
            t=t+1
        if k>b2:
            y=y+1
        if k>b3:
            m+=1
        if k>b4:
            n+=1
        if k>b5:
            v+=1
        ff.mostrart(mostrar_t1,escrito1)
        ll.mostrart(mostrar_t,escrito)
        qq.mostrart(mostrar_t2,escrito2)
        ww.mostrart(mostrar_t3,escrito3)
        ee.mostrart(mostrar_t4,escrito4)
        clock.tick(15)
        p.display.update()
        k=k+1
