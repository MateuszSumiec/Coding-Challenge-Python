# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:13:40 2019

@author: Mateusz
"""

from common import square, cube, darkBlue, white
import numpy as np
import pygame as pg
import sys


class Render():

    def __init__(self, width=800, height=600):
        """Create window with given resolution"""
        pg.init()

        self.screen = pg.display.set_mode((width, height))

        self.screen.fill(darkBlue)
        self.clock = pg.time.Clock()

        self.vertices = square

        self.angle = 0

    def draw(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill(darkBlue)

            for vertex in self.vertices:
        #        screen.fill(white, (vertex[0], vertex[1], 10, 10))
#                projected_2d = np.matmul(vertex, projection_matrix.T).T
#                rotateX = rotationX(self.angle)
#                rotated = np.matmul(rotateX, vertex.T)
#                print(rotated)
        #        gfxdraw.filled_circle(screen, rotated[0], rotated[1], 8, white)
                self.screen.fill(white, (vertex[0], vertex[1], 8, 8))
            self.angle += 0.001

            pg.display.flip()
