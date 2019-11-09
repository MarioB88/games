import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows=0
    w=0
    def __init__(self, start, dx = 1, dy = 0, color=(255, 0, 0)):
        pass

    def move(self, dx, dy):
        pass

    def draw(self, surface, eyes=False):
        pass

def drawGrid(w, rows, surface):
    sizeGaps = w // rows

    x = 0
    y = 0

    for k in range(rows):
        x += sizeGaps
        y += sizeGaps
        pygame.draw.line(surface, (255,255,255), (x,0), (x, w))     # (x,0) es donde empieza la linea y (x,w) es donde acaba la linea
        pygame.draw.line(surface, (255,255,255), (y,0), (w, y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def main():
    global width, rows
    width = 500
    rows = 20
    window = pygame.display.set_mode((width, width))
    #s = snake((255, 0, 0), (10,10))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(50)       # Esto regula lo el clock.tick para que la serpiente no vaya tan rapida (50milisec)
        clock.tick(10)              # Nos asegura que nuestro juego no se va a ejecutar a mas de 10 frames por segundo (la serpiente se movera en diez bloques en un segundo)

        redrawWindow(window)
