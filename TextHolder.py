import pygame as pg

import itertools
from Structures import *


class TextHolder :

    def __init__( self, text: str, font: pg.font.Font, max_width: float = None ) :
        self.__color = Color( 255, 255, 255 )
        self.__text = text
        self.__font = font
        self.__max_width = max_width

        self.__text_list = []
        self.__surface_list = []

        self.update_text()



    def update_text( self, text: str = None ) :
        if text is None : self.__text = self.__text

        self.generate_texts()
        self.generate_surfaces()


    def generate_texts( self ) :
        counter = 0

        if self.__max_width is None:
            self.__text_list.append(self.__text)
            return

        while counter <= len( self.__text ) :

            first = self.__text[:counter + 1]
            second = self.__text[counter + 1 :]
            next_step = self.__text[:counter + 2]

            if self.__font.size( next_step )[0] > self.__max_width :
                self.__text = second
                self.__text_list.append( first )
                counter = 0
            else :
                counter += 1

        if len( self.__text ) != 0 : self.__text_list.append( self.__text )


    def generate_surfaces( self ) :
        for i in self.__text_list :
            self.__surface_list.append(
                self.__font.render( i, True, self.__color.get_tuple()) )


    def render( self, surface:pg.surface.Surface , top_left_pos:Pos = None) :
        if top_left_pos is None: top_left_pos = Pos(0,0)

        for i in self.__surface_list:
            surface.blit(i,top_left_pos.get_tuple())
            top_left_pos.y += i.get_height()



