import pygame as pg

from Window import Window
from Structures import *


color = Color(100,200,255,255)

rect = Rect(0,0,0,0)
rect.transform_pos(-120,3)
rect.transform_size(150,1.1)


print(rect.get_pos())