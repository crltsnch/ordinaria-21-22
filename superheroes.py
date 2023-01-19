from enum import Enum
import random

class Superheroe_Type(Enum):
    HUMANO = 1
    NOHUMAO = 0

    def from_str(x):
        superheroe = x.upper()
        e = None
        for tp in Superheroe_Type:
            if tp.name == superheroe:
                e = tp
                break
        
        if type(e) != Superheroe_Type:
            raise ValueError("No es un tipo de superheroe valido")
        return e

class Movimiento_Type(Enum):
    ATAQUE = 1
    DEFENSA = 0

class Movimiento_General(Enum):
    def __init__(self, x, a, daño):
        self.__nombre = x
        self.__tipo = a
        self.__daño = daño
    
    def get_nombre(self):
        return self.__nombre
    
    def get_tipo(self):
        return self.__tipo
    
    def get_daño(self):
        return self.__daño
    
    def set_daño(self, daño):
        self.__daño = daño

class Movimientos_Espedifico(Movimiento_General):
    def __init__(self, x, a, daño, superheroe):
        super().__init__(x, a, daño)
        self.__superheroe = superheroe
    
    def get_energia(self):
        return self.__energia
    
    def set_energia(self, e):
        self.__energia = e
