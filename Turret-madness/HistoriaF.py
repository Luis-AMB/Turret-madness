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
    b1,b2,b3,b4,b5=0,600,750,950,150
    a0,a1,a2,a3,a4=[],[],[],[],[]
    k,t,y,n,m,v=0,0,0,0,0,0
    guion1=[]
    guion2=[]
    guion3=[]
    guion4=[]
    guion1.append("Planeta Surata.")
    guion1.append("2.200 años despues de la guerra universal.")
    guion1.append("Un millon de años luz de la Tierra.")
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
    guion0=[] #crixos
    guion0.append("En el año 2.200 los Crixos descubrieron el planeta Surata")
    guion0.append("el cual tiene una superficie rocosa y desertica con clima muy calido,")
    guion0.append("en el habitan unos seres vivos con forma de torretas.")
    guion0.append("Los crixos son una especie alienigena aniquiladora que")
    guion0.append("viajan por el universo en busca de recursos y alimento,")
    guion0.append("acabando con los planetas y destruyendo toda forma de vida.")
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
        #aa=escrito,bb=mostrar_t, 
               
    ll=textos(100,500)
    for d in range(len(guion0)):
        a0.append(len(ll.guiones(guion0[d])))
    ff=textos(210,500)
    for d in range(len(guion1)):
        a1.append(len(ff.guiones(guion1[d])))
    qq=textos(200,500)
    for d in range(len(guion2)):
        a2.append(len(qq.guiones(guion2[d])))
    ww=textos(800,500)
    for d in range(len(guion3)):
        a3.append(len(ww.guiones(guion3[d])))
    ee=textos(500,500)
    for d in range(len(guion4)):
        a4.append(len(ee.guiones(guion4[d])))
        
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
            ll.mostrar(v,a0,mostrar_t)        
            for i in range(0,len(mostrar_t)):
                if i==0:
                    escrito[0]=escrito[0]+ll.escribir_g(ll.guiones(guion0[0]),v,"")
                else:
                    if mostrar_t[i]:
                        escrito[i]=escrito[i]+ll.escribir_g(ll.guiones(guion0[i]),v,"",ll.sumatoria(a0,i))
        if k>b1:
            ff.mostrar(t,a1,mostrar_t1)
            for i in range(0,len(mostrar_t1)):
                if i==0:
                    escrito1[0]=escrito1[0]+ff.escribir_g(ff.guiones(guion1[0]),t,"")
                else:
                    if mostrar_t1[i]:
                        escrito1[i]=escrito1[i]+ff.escribir_g(ff.guiones(guion1[i]),t,"",ff.sumatoria(a1,i))
         
        if k>b2:
            qq.mostrar(y,a2,mostrar_t2)
            for i in range(0,len(mostrar_t2)):
                if i==0:
                    escrito2[0]=escrito2[0]+qq.escribir_g(qq.guiones(guion2[0]),y,"")
                else:
                    if mostrar_t2[i]:
                        escrito2[i]=escrito2[i]+qq.escribir_g(qq.guiones(guion2[i]),y,"",qq.sumatoria(a2,i))
        
        if k>b3:
            ww.mostrar(m,a3,mostrar_t3)
            for i in range(0,len(mostrar_t3)):
                if i==0:
                    escrito3[0]=escrito3[0]+ww.escribir_g(ww.guiones(guion3[0]),m,"")
                else:
                    if mostrar_t3[i]:
                        escrito3[i]=escrito3[i]+ww.escribir_g(ww.guiones(guion3[i]),m,"",ww.sumatoria(a3,i))
        
        if k>b4:
            ee.mostrar(n,a4,mostrar_t4)
            for i in range(0,len(mostrar_t4)):
                if i==0:
                    escrito4[0]=escrito4[0]+ee.escribir_g(ee.guiones(guion4[0]),n,"")
                else:
                    if mostrar_t4[i]:
                        escrito4[i]=escrito4[i]+ee.escribir_g(ee.guiones(guion4[i]),n,"",ee.sumatoria(a4,i))
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
        p.display.flip()
        p.display.update()
        k=k+1