import pygame as p
import sys
import os
import lvl_2
import lvl_1
import gamewin
import imp
import nivel
p.init()
p.mixer.init()
font = p.font.Font('Fuentes\\spacerunnertwoital.TTF', 35)
font_3 = p.font.Font('Fuentes\\spacerunnertwoital.TTF', 30)
font_1 = p.font.Font('Fuentes\\spacerunnertwoital.TTF', 100)
font_2 = p.font.Font('Fuentes\\spacerunnertwoital.TTF', 100)
clock = p.time.Clock()
size = width, height = 1280, 720
pantalla = p.display.set_mode(size)
bg_image = p.image.load("images\\fondowin.jpg")
bg_image = bg_image.convert()
gamewinimg =p.image.load("images\\gamewin.png")
boton = p.image.load("images\\botonwin.png")
select = p.mixer.Sound('efectos\\sonido_boton.mp3')
tap = p.mixer.Sound('efectos\\boton_tap.mp3')
p.mixer.music.load("efectos\\fondo.mp3")
p.mixer.music.play(-1)
p.mixer.music.set_volume(0.2)
canal1 = p.mixer.Channel(0)
canal2 = p.mixer.Channel(1)

def draw_txt(texto, font, color, surface, x, y):
    textobj = font.render(texto, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    running = True
    click = False
    boton_1 = None
    boton_2 = None
    pos = 30, 200
    while running:
        if boton_1 == None and boton_2 == None:
            pantalla.blit(bg_image, (0, 0))
            pantalla.blit(gamewinimg,(700,230))
            draw_txt("TURRET", font_2, (0, 0, 0), pantalla, 197, 65)
            draw_txt("TURRET", font_2, (255, 255, 255), pantalla, 190, 60)
            draw_txt("MADNESS", font_1, (0, 0, 0), pantalla, 650, 65)
            draw_txt("MADNESS", font_1, (255, 255, 255), pantalla, 643, 60)
            draw_txt("LEVEL", font_2, (0, 0, 0), pantalla, 85, 348)
            draw_txt("LEVEL", font_2, (255, 255, 255), pantalla, 80, 340)
            draw_txt("WIN", font_1, (0, 0, 0), pantalla, 125, 436)
            draw_txt("WIN", font_1, (255, 255, 255), pantalla, 120, 428)
        else:
            pantalla.blit(bg_image, boton_1, boton_1)
            pantalla.blit(bg_image, boton_2, boton_2)

        mx, my = p.mouse.get_pos()
        boton_1 = pantalla.blit(boton, (pos[0]+482, pos[1] + 165))
        boton_2 = pantalla.blit(boton, (pos[0]+482, pos[1] + 265))
        draw_txt("Siguiente", font, (0, 0, 0), pantalla, 520, 370)
        draw_txt("Siguiente", font, (255, 255, 255), pantalla, 518, 368)
        draw_txt("Salir", font, (0, 0, 0), pantalla, 560, 470)
        draw_txt("Salir", font, (255, 255, 255), pantalla, 558, 468)

        if boton_1.collidepoint((mx, my)):
            pantalla.blit(bg_image, boton_1, boton_1)
            boton_1 = pantalla.blit(boton, (pos[0]+480, pos[1]+163))
            draw_txt("Siguiente", font, (0, 0, 0), pantalla, 518, 368)
            draw_txt("Siguiente", font, (255, 255, 255), pantalla, 516, 366)
            canal1.play(tap)
            if click:
                canal2.play(select)
                runing = False
                if nivel.levelok == 1:
                    lvl_2.game(True,0.2)
                elif nivel.levelok ==2:
                    lvl_3.game(True,0.2)

                clock.tick(60)
        if boton_2.collidepoint((mx, my)):
            pantalla.blit(bg_image, boton_2, boton_2)
            boton_2 = pantalla.blit(boton, (pos[0]+480, pos[1] + 263))
            draw_txt("Salir", font, (0, 0, 0), pantalla, 558, 468)
            draw_txt("Salir", font, (255, 255, 255), pantalla, 556, 466)
            canal1.play(tap)
            if click:
                canal1.play(select)
                running = False
                sys.exit()
                clock.tick(60)
        for event in p.event.get():
            if event.type == p.QUIT:
                running = True
                sys.exit()
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    running == True
            elif event.type == p.MOUSEBUTTONDOWN:
                if (event.button == 1 and boton_1.collidepoint((mx, my))) or (
                        event.button == 1 and boton_2.collidepoint((mx, my))):
                    click = True
        p.display.update()
        clock.tick(60)

