import pygame as pg

from Window import Window
from Structures import *

pg.init()

window: Window = Window(Pos(1000, 750), Pos(800, 600), "menu maker")

bg = Color(150,150,220)

while window.is_running:
    window.get_events(pg.event.get())
    window.check_events()

    window.render_and_update()

    window.tick()
