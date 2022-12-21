import pygame as pg

from Structures import *

class Menu:
    def __init__( self, surface_size:Pos , surface_pos:Pos = Pos(0,0) ):

        self.__surface_pos = surface_pos
        self.__surface_size = surface_size
        self.__surface = pg.surface.Surface(self.__surface_size.get_tuple()).convert_alpha()

        self.__surface_color = Color(0,0,0,0)

    def set_color( self , color:Color ):
        self.__surface_color = color


    def get_events( self, event_list=None ) :
        if event_list is None : event_list = list()

        if len( event_list ) == 0 : event_list = pg.event.get()

        for i in event_list :
            pass

    def check_events( self ):
        pass

    def render( self , surface:pg.surface.Surface):
        self.__surface.fill(self.__surface_color.get_tuple())

        surface.blit(self.__surface,self.__surface_pos.get_tuple())


    def run( self,surface:pg.surface.Surface,event_list: list = None ) :
        self.get_events( event_list )
        self.check_events()
        self.render(surface)


