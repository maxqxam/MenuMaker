import pygame as pg
from Enums import Errors


class Color :

    def __init__( self, red: float, green: float, blue: float, alpha: float = 255 ) :
        self.__red, self.__green, self.__blue, self.__alpha = red, green, blue, alpha
        if any( [(i < 0 or i > 255) for i in
            [self.__red, self.__green, self.__blue, self.__alpha]] ) :
            raise ValueError( Errors.InvalidColorValue )


    def copy( self ) :
        return Color( self.__red, self.__green, self.__blue, self.__alpha )


    def is_valid( self ) :
        return any(
            [(i < 0 or i > 255) for i in [self.__red, self.__green, self.__blue, self.__alpha]] )


    def check_value_validness( self ) :
        if not self.is_valid() : ValueError( Errors.InvalidColorValue )

    def get_pygame_color( self ):
        return pg.color.Color(self.get_tuple())

    def get_tuple( self ) :
        return self.__red, self.__green, self.__blue, self.__alpha


    def reset( self, r: float, g: float, b: float, a: float ) :
        self.__red, self.__green, self.__blue, self.__alpha = r, g, b, a
        self.check_value_validness()
        return self


    def transform( self, r_sum: float = 0, g_sum: float = 0, b_sum: float = 0, a_sum: float = 0 ) :
        self.__red += r_sum
        self.__green += g_sum
        self.__blue += b_sum
        self.__alpha += a_sum

        self.check_value_validness()
        return self


class Pos :

    def __init__( self, x: float, y: float ) :
        self.x = x
        self.y = y


    def __str__( self ) :
        return "[PosObject : ({},{})]".format( self.x, self.y )


    def copy( self ) :
        return Pos( self.x, self.y )


    def reset( self, new_x: float = 0, new_y: float = 0 ) :
        self.x, self.y = new_x, new_y


    def get_tuple( self ) :
        return self.x, self.y


    def transform( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        if not sum_first :
            self.x *= mult
            self.x += Sum
            self.y *= mult
            self.y += Sum
        else :
            self.x += Sum
            self.x *= mult
            self.y += Sum
            self.y *= mult

        return self


    def get_transformed_pos( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        return Pos( self.x, self.y ).transform( Sum, mult, sum_first )


    def get_transformed_tuple( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        return Pos( self.x, self.y ).transform( Sum, mult, sum_first ).get_tuple()


class Rect :

    def __init__( self, x: float, y: float, width: float, height: float ) :
        self.__x, self.__y, self.__width, self.__height = x, y, width, height
        self.__pos = Pos( self.__x, self.__y )
        self.__size = Pos( self.__width, self.__height )


    def __str__( self ) :
        return "[RectObject : ({},{},{},{})]".format( self.__x, self.__y, self.__width,
            self.__height )


    def copy( self ) :
        return Rect( self.__x, self.__y, self.__width, self.__height )


    def get_pygame_rect( self ) :
        return pg.rect.Rect( self.get_tuple() )


    def get_tuple( self ) :
        return self.__x, self.__y, self.__width, self.__height


    def get_pos( self ) :
        return self.__pos


    def get_size( self ) :
        return self.__size


    def transform_pos( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        self.__pos.transform( Sum, mult, sum_first )
        self.__x, self.__y = self.__pos.x, self.__pos.y
        return self


    def transform_size( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        self.__size.transform( Sum, mult, sum_first )
        self.__width, self.__height = self.__size.x, self.__size.y
        return self


    def render( self, surface: pg.surface.Surface, color: Color ) :
        pg.draw.rect( surface, color.get_tuple(), self.get_tuple() )
