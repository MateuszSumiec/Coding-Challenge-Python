# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:19:47 2019

@author: Mateusz
"""

import numpy as np

width = 640
height = 480

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)

square = np.array([(-100, -100, 0),
                   (-100, 100, 0),
                   (100, -100, 0),
                   (100, 100, 0)])

cube = np.array([(-1, -1, -1),
                 (-1, -1,  1),
                 (1, -1, -1),
                 (1, -1, 1),
                 (-1, 1, -1),
                 (-1, 1, 1),
                 (1, 1, -1),
                 (1, 1, 1)])
