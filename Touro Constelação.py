import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_largura = 1000      #variaveis que seram usadas pra definir o tamanho da tela
screen_altura = 800        #variaveis que seram usadas pra definir o tamanho da tela
                                    #abaixo
tela = pygame.display.set_mode((screen_largura,screen_altura), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Olá MUNDO ")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

done = True
init_ortho()

def desenha_estrela(x,y, size):     #eu queria variar o tamanho dos pontos então
    glPointSize(size)               #criei uma função desenha_estrela pra poder
    glBegin(GL_POINTS)              #definir o glPoinSize individualmente.
    glVertex2i(x, y)                #já que o glVertex2i só aceita dois valores.
    glEnd()


while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    #Se eu usasse o glPointSize() aqui, o mesmo valor seria igual pra todos os pontos dentro do
    #glBegin e GlEnd, eu teria que repetir os dois comando em cada ponto.

    desenha_estrela(500,70,40)
    desenha_estrela(460, 140, 15)
    desenha_estrela(370, 240, 30)
    desenha_estrela(400, 290, 10)
    desenha_estrela(300, 250, 30)
    desenha_estrela(150, 400, 15)
    desenha_estrela(350, 330, 15)
    desenha_estrela(360, 390, 15)

    pygame.display.flip()


pygame.quit()
