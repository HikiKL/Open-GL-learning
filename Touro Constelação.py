import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()


screen_largura = 1000
screen_altura = 800

tela = pygame.display.set_mode((screen_largura,screen_altura), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Olá MUNDO ")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

done = True

init_ortho()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex2i(500,70)
    glVertex2i(460, 140)
    glVertex2i(370, 240)
    glVertex2i(400, 290)
    glVertex2i(300, 250)
    glVertex2i(150, 400)
    glVertex2i(350, 330)
    glVertex2i(360, 390)

    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()



