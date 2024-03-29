import math
import random
import contextlib
import os
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    def __init__(self, start, dx = 1, dy = 0, color=(255, 0, 0)):
        self.pos = start
        self.dx = 1
        self.dy = 0
        self.color = color
        

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.pos = (self.pos[0]+ self.dx, self.pos[1]+ self.dy)

    def draw(self, surface, eyes=False):
        distance = width // rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*distance+1, j*distance+1, distance-2, distance-2))
        # Explicación: Si estamos en al posicion 1,3 queremos decir que estamos en la primera fila de cuadrados y en la tercera columna de cuadrados
        # asi que para que lo dibuje en la pantalla correctamente calculamos la distancia que hay entre cada linea y la multiplicamos por la posicion
        # en la que estamos. // // // Le sumamos uno y le restamos dos para que haya un pequeño hueco entre lo que estamos dibujando y la linea 
        # del cuadrado


        # Ahora maths para dibujar los ojos en el sitio correcto:

        if eyes:
            centre = distance//2
            radius = 3
            circleMiddle = (i*distance+centre-radius,j*distance+8)
            circleMiddle2 = (i*distance + distance -radius*2, j*distance+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dx = 0
        self.dy = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:            # Translation: if in keys, K_LEFT is true, then ...
                    self.dx = -1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif keys[pygame.K_RIGHT]:
                    self.dx = 1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif keys[pygame.K_UP]:
                    self.dx = 0
                    self.dy = -1
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

                elif keys[pygame.K_DOWN]:
                    self.dx = 0
                    self.dy = 1
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dx == -1 and c.pos[0] <= 0: c.pos = (rows-1, c.pos[1])
                elif c.dx == 1 and c.pos[0] >= rows-1: c.pos = (0,c.pos[1])
                elif c.dy == 1 and c.pos[1] >= rows-1: c.pos = (c.pos[0], 0)
                elif c.dy == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],rows-1)
                else: c.move(c.dx, c.dy)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dx = 0
        self.dy = 1


    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dx, tail.dy
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
        
        self.body[-1].dx = dx
        self.body[-1].dy = dy
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i==0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def drawGrid(w, rows, surface):
    sizeGaps = w // rows

    x = 0
    y = 0

    for k in range(rows):
        x += sizeGaps
        y += sizeGaps
        pygame.draw.line(surface, (255,255,255), (x,0), (x, w))     # (x,0) es donde empieza la linea y (x,w) es donde acaba la linea
        pygame.draw.line(surface, (255,255,255), (0,y), (w, y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    obst.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, snake):
    positions = snake.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x, y)

def randomObstacle(rows, snake, snackPos):
    positions = snake.body
    while True:
        x=random.randrange(rows)
        y=random.randrange(rows)

        if (len(list(filter(lambda z:z.pos == (x,y), positions))) > 0) or (snackPos == (x,y)):
            continue
        else:
            break
    return (x,y)

def messageBox(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global width, rows, s, snack, obst
    width = 500
    rows = 20
    window = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10,10))
    snack = cube(randomSnack(rows, s), color = (0, 255, 0))
    obst = cube(randomObstacle(rows, s, snack.pos), color = (0,0, 255))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(50)       # Esto regula lo del clock.tick para que la serpiente no vaya tan rapida (50milisec)
        clock.tick(10)              # Nos asegura que nuestro juego no se va a ejecutar a mas de 10 frames por segundo (la serpiente se movera diez bloques en un segundo)

        redrawWindow(window)
        s.move()
        if (s.body[0].pos == snack.pos):
            s.addCube()
            snack = cube(randomSnack(rows, s), color = (0, 255, 0))
        
        if (s.body[0].pos in list(map(lambda z:z.pos, s.body[1:]))) or (s.body[0].pos == obst.pos):
            print("Score: ", len(s.body))
            messageBox("You lost!", "Play Again...?")
            s.reset((10,10))

main()