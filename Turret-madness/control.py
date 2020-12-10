import pygame as p
import sys
import lvl_1

p.init()
p.mixer.init()
p.display.set_caption("Tower-Madness")
font= p.font.Font('Fuentes\\spacerunnertwoital.TTF',35)
font_3= p.font.Font('Fuentes\\spacerunnertwoital.TTF',30)
font_4= p.font.Font('Fuentes\\spacerunnertwoital.TTF',50)
font_1= p.font.Font('Fuentes\\spacerunnertwoital.TTF',100)
font_2= p.font.Font('Fuentes\\spacerunnertwoital.TTF',150)
font_5= p.font.Font('Fuentes\\raidercrusaderpunch.TTF',30)
clock=p.time.Clock()
size=width,height=1280,720
pantalla=p.display.set_mode(size)
bg_image=p.image.load("images\\fondo-proyecto.png")
bg_image=bg_image.convert()
boton=p.image.load("images\\boton.png")
back=p.image.load("images\\flecha-regresar.png")
select=p.mixer.Sound('efectos\\sonido_boton.wav')
tap=p.mixer.Sound('efectos\\boton_tap.wav')
#p.mixer.music.load("effectos\\fondo.wav")
#p.mixer.music.play(-1)
#p.mixer.music.set_volume(0.2)
canal1=p.mixer.Channel(0)
canal2=p.mixer.Channel(1)
#carga de imagenes del teclado
centro=1280/2
escala=0.7
A=[]
D=[]
S=[]
W=[]
Enter=[]
Up=[]
Left=[]
Down=[]
Right=[]
Mouse_moveL=[]
Mouse_moveR=[]
Mouse_moveU=[]
Mouse_moveD=[]
Mouse_clickR=[]
Mouse_clickL=[]
borrar=[]
Titulos=["MOVIMIENTO","COLOCAR TORRETAS","QUITAR TORRETAS"]
Movimiento=[]
Movimiento2=[]
Movimiento3=[]
Movimiento4=[]
"""Colocar_torretas=[]
Quitar_Torretas=[]
paginas=[]"""
for i in range(2):
    A.append(p.image.load("teclado\\A"+str(i)+".png").convert_alpha())
    D.append(p.image.load("teclado\\D"+str(i)+".png").convert_alpha())
    S.append(p.image.load("teclado\\S"+str(i)+".png").convert_alpha())
    W.append(p.image.load("teclado\\W"+str(i)+".png").convert_alpha())
    Enter.append(p.image.load("teclado\\enter"+str(i)+".png").convert_alpha())
    Up.append(p.image.load("teclado\\up"+str(i)+".png").convert_alpha())
    Left.append(p.image.load("teclado\\left"+str(i)+".png").convert_alpha())
    Down.append(p.image.load("teclado\\down"+str(i)+".png").convert_alpha())
    Right.append(p.image.load("teclado\\rigth"+str(i)+".png").convert_alpha())
    borrar.append(p.image.load("teclado\\del"+str(i)+".png").convert_alpha())
    Mouse_clickL.append(p.image.load("teclado\\MB"+str(i)+".png").convert_alpha())
    Mouse_clickR.append(p.image.load("teclado\\MB"+str(i*2)+".png").convert_alpha())
    Mouse_moveL.append(p.image.load("teclado\\M"+str(i)+".png").convert_alpha())
    Mouse_moveU.append(p.image.load("teclado\\M"+str(i*2)+".png").convert_alpha())
    Mouse_moveR.append(p.image.load("teclado\\M"+str(i*3)+".png").convert_alpha())
    Mouse_moveD.append(p.image.load("teclado\\M"+str(i*4)+".png").convert_alpha())
    A[i]=p.transform.rotozoom(A[i], 0, escala)
    D[i]=p.transform.rotozoom(D[i], 0, escala)
    S[i]=p.transform.rotozoom(S[i], 0, escala)
    W[i]=p.transform.rotozoom(W[i], 0, escala)
    Up[i]=p.transform.rotozoom(Up[i], 0, escala)
    Left[i]=p.transform.rotozoom(Left[i], 0, escala)
    Down[i]=p.transform.rotozoom(Down[i], 0, escala)
    Right[i]=p.transform.rotozoom(Right[i], 0, escala)
    Mouse_moveL[i]=p.transform.rotozoom(Mouse_moveL[i], 0, escala*4)
    Mouse_moveU[i]=p.transform.rotozoom(Mouse_moveU[i], 0, escala*4)
    Mouse_moveD[i]=p.transform.rotozoom(Mouse_moveD[i], 0, escala*4)
    Mouse_moveR[i]=p.transform.rotozoom(Mouse_moveR[i], 0, escala*4)
    Mouse_clickL[i]=p.transform.rotozoom(Mouse_clickL[i], 0, escala*4)
    Mouse_clickR[i]=p.transform.rotozoom(Mouse_clickR[i], 0, escala*4)
    Enter[i]=p.transform.rotozoom(Enter[i], 0, escala*2)
    borrar[i]=p.transform.rotozoom(borrar[i], 0, escala*2)
for i in range(4):
    Movimiento.append(p.image.load("teclado\\"+str(i)+".png").convert_alpha())
    Movimiento[i]=p.transform.rotozoom(Movimiento[i], 0, 0.8)
    
for i in range(3):
    Movimiento2.append(p.image.load("teclado\\"+str(i+5)+".png").convert_alpha())
    Movimiento2[i]=p.transform.rotozoom(Movimiento2[i], 0, 0.8)
for i in range(10):
    Movimiento3.append(p.image.load("teclado\\"+str(i+8)+".png").convert_alpha())
    Movimiento3[i]=p.transform.rotozoom(Movimiento3[i], 0, 0.8)
    Movimiento4.append(p.image.load("teclado\\"+str(i+18)+".png").convert_alpha())
    Movimiento4[i]=p.transform.rotozoom(Movimiento4[i], 0, 0.8)
def draw_txt(texto, font, color, surface, x, y):
    textobj=font.render(texto, True, color)
    textrect=textobj.get_rect(center=(x,y))
    #textrect.topleft=( x, y)
    surface.blit(textobj,textrect)

def controles_1(controles,volumen):
    running = True 
    click=False
    al,al1,al2,al3,al4,al5,al6=0,0,3,0,3,0,0
    count=0
    pos1=180,550
    pos2=180,410
    pos3=1080,500
    color=[(255,255,255),(0,0,0)]
    continuar=False
    space=False
    page=0
    while running:
        pantalla.blit(bg_image,(0,0))
        draw_txt("COMO JUGAR",font_1, (0,0,0),pantalla,centro+13,83)
        draw_txt("COMO JUGAR",font_1, (255,255,255),pantalla,centro,80)
        draw_txt("MOUSE", font_4, (0,0,0), pantalla, 1090,238)
        draw_txt("MOUSE", font_4, (255,255,255), pantalla, 1090,235)
        draw_txt("TECLADO", font_4, (0,0,0), pantalla, 180,238)
        draw_txt("TECLADO", font_4, (255,255,255), pantalla, 180,235)
        draw_txt(Titulos[page], font_4, (0,0,0), pantalla, centro+13, 188)
        draw_txt(Titulos[page], font_4, (255,255,255), pantalla, centro, 185)
        if al<=2-0.03:
            al+=0.03
        else:
            al=0
            count+=1
        if al1<4-0.015:
            al1+=0.015
        else:
            al1=0
        if al2>=0:#.015:
            al2-=0.015
        else:
            al2=4-0.015
        if al5<=2-0.1:
            al5+=0.1
        else:
            al5=0
        if al6<10-0.03:
            al6+=0.03
        else:
            al6=0
        casilla=False

        if page==0:
            if count<3:
                centro_img3=Movimiento[0].get_rect(center=(centro,450))
                pantalla.blit(Movimiento[int(al1)],centro_img3)
                centro_img1=A[0].get_rect(center=(pos1))
                centro_img2=Down[0].get_rect(center=pos2)
                centro_img4=Mouse_moveL[0].get_rect(center=pos3)
                pantalla.blit(S[0],centro_img1)
                pantalla.blit(A[int(al)],(centro_img1[0]-70,centro_img1[1]))
                pantalla.blit(D[0],(centro_img1[0]+70,centro_img1[1]))
                pantalla.blit(W[0],(centro_img1[0],centro_img1[1]-70))
                pantalla.blit(Down[0],centro_img2)
                pantalla.blit(Left[int(al)],(centro_img2[0]-70,centro_img2[1]))
                pantalla.blit(Right[0],(centro_img2[0]+70,centro_img2[1]))
                pantalla.blit(Up[0],(centro_img2[0],centro_img2[1]-70))
                pantalla.blit(Mouse_moveL[int(al)],centro_img4)
            elif count>=3 and count<6:
                continuar=True
                centro_img3=Movimiento[0].get_rect(center=(centro,450))
                pantalla.blit(Movimiento[int(al2)],centro_img3)
                centro_img1=A[0].get_rect(center=(pos1))
                centro_img2=Down[0].get_rect(center=pos2)
                pantalla.blit(S[0],centro_img1)
                pantalla.blit(A[0],(centro_img1[0]-70,centro_img1[1]))
                pantalla.blit(D[int(al)],(centro_img1[0]+70,centro_img1[1]))
                pantalla.blit(W[0],(centro_img1[0],centro_img1[1]-70))
                pantalla.blit(Down[0],centro_img2)
                pantalla.blit(Left[0],(centro_img2[0]-70,centro_img2[1]))
                pantalla.blit(Right[int(al)],(centro_img2[0]+70,centro_img2[1]))
                pantalla.blit(Up[0],(centro_img2[0],centro_img2[1]-70))
                pantalla.blit(Mouse_moveR[int(al)],centro_img4)
            elif count>=6 and count<8:
                if al3<3-0.015:
                    al3+=0.015
                else:
                    al1=0
                centro_img3=Movimiento[0].get_rect(center=(centro,450))
                pantalla.blit(Movimiento2[int(al3)],centro_img3)
                centro_img1=A[0].get_rect(center=(pos1))
                centro_img2=Down[0].get_rect(center=pos2)
                pantalla.blit(S[0],centro_img1)
                pantalla.blit(A[0],(centro_img1[0]-70,centro_img1[1]))
                pantalla.blit(D[0],(centro_img1[0]+70,centro_img1[1]))
                pantalla.blit(W[int(al)],(centro_img1[0],centro_img1[1]-70))
                pantalla.blit(Down[0],centro_img2)
                pantalla.blit(Left[0],(centro_img2[0]-70,centro_img2[1]))
                pantalla.blit(Right[0],(centro_img2[0]+70,centro_img2[1]))
                pantalla.blit(Up[int(al)],(centro_img2[0],centro_img2[1]-70))
                pantalla.blit(Mouse_moveU[int(al)],centro_img4)
            elif count>=8 and count<10:
                if al4>=0.015:
                    al4-=0.015
                else:
                    al4=2-0.015
                centro_img3=Movimiento[0].get_rect(center=(centro,450))
                pantalla.blit(Movimiento2[int(al4)],centro_img3)
                centro_img1=A[0].get_rect(center=(pos1))
                centro_img2=Down[0].get_rect(center=pos2)
                pantalla.blit(S[int(al)],centro_img1)
                pantalla.blit(A[0],(centro_img1[0]-70,centro_img1[1]))
                pantalla.blit(D[0],(centro_img1[0]+70,centro_img1[1]))
                pantalla.blit(W[0],(centro_img1[0],centro_img1[1]-70))
                pantalla.blit(Down[int(al)],centro_img2)
                pantalla.blit(Left[0],(centro_img2[0]-70,centro_img2[1]))
                pantalla.blit(Right[0],(centro_img2[0]+70,centro_img2[1]))
                pantalla.blit(Up[0],(centro_img2[0],centro_img2[1]-70))
                pantalla.blit(Mouse_moveD[int(al)],centro_img4)
                               
            else:
                count=0
                al1,al2,al3,al4=0,3,0,3
        elif page==1:
            continuar=False
            centro_mov=Movimiento3[0].get_rect(center=(centro,450))
            pantalla.blit(Movimiento3[int(al6)],centro_mov)
            if count>=4 and count<10:
                continuar=True
            if int(al6)==3 or int(al6)==8:
                pantalla.blit(Enter[1],(centro_img1[0]-50,centro_img1[1]-150))
                pantalla.blit(Mouse_clickL[1],(centro_img4[0]+50,centro_img4[1]))
            else:
                pantalla.blit(Enter[0],(centro_img1[0]-50,centro_img1[1]-150))
                pantalla.blit(Mouse_clickL[0],(centro_img4[0]+50,centro_img4[1]))
        elif page==2:
            continuar=False
            centro_mov=Movimiento4[0].get_rect(center=(centro,450))
            pantalla.blit(Movimiento4[int(al6)],centro_mov)
            if count>=4 and count<10:
                draw_txt("Oprime espacio para jugar", font_5, color[int(al5)], pantalla, centro, 670)
            if int(al6)%2!=0:
                pantalla.blit(borrar[1],(centro_img1[0]-50,centro_img1[1]-150))
                pantalla.blit(Mouse_clickR[1],(centro_img4[0]+50,centro_img4[1]))
            else:
                pantalla.blit(borrar[0],(centro_img1[0]-50,centro_img1[1]-150))
                pantalla.blit(Mouse_clickR[0],(centro_img4[0]+50,centro_img4[1]))
        
        if continuar:    
            draw_txt("Oprime espacio para continuar", font_5, color[int(al5)], pantalla, centro, 670)
        if space and page<=2:
            space=False
            page+=1
            count=0
            al,al1,al2,al3,al4,al5,al6=0,0,3,0,3,0,0
        if page>=3:
            lvl_1.game(volumen,controles)
        mx,my=p.mouse.get_pos()
        boton_b=pantalla.blit(back,(50,630))
        if boton_b.collidepoint((mx,my)):
            casilla=True
            pantalla.blit(bg_image,boton_b,boton_b)
            boton_b=pantalla.blit(back,(50,625))
            canal1.play(tap)
            if click:
                running=False
                break
                #main_menu()
        for event in p.event.get():
            if event.type==p.QUIT:
                p.quit()
                sys.exit()
            elif event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    running==False
                    break
                    #main_menu()
                if event.key==p.K_SPACE:
                    space=True
                    #else:
            elif event.type==p.MOUSEBUTTONDOWN:
                if event.button==1 and casilla:
                    click=True
        p.display.update()
        clock.tick(60)
