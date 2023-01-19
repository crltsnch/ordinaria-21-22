from enum import Enum
import random
from SerVivo import SerVivo
from escenarios import Escenarios

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
    
    def get_superheroe(self):
        return self.__superheroe
    
class Superheroes(SerVivo):
    numero_superheroes = 0

    def __init__(self, alias, identidad, tipo, esc):
        self.__identificador = Superheroes.numero_superheroes
        self.__alias = alias
        self.__identidadSecreta = identidad
        self.__movmientos = []
        self.__tipo = tipo
        if type(tipo) !=  Superheroe_Type:
            raise TypeError('Tipo inválido')
        if tipo.value:
            self.__parrilla_poderes = [random.randint(3,8),random.randint(1,7), random.randint(2,6), random.randint(2,6), random.randint(1,7), random.randint(1,8)]
        else:
            self.__parrilla_poderes = [random.randint(4,7),random.randint(1,8), random.randint(1,8), random.randint(3,8), random.randint(1,8), random.randint(3,7)]
        if type(esc) != Escenarios:
            raise TypeError('Escenario inválido')
        self.__coste = (esc.get_monedas()/esc.get_miembros_ekip())*(sum(self.__parrilla_poderes)/30) 
        self.__energia = (esc.get_energia_vital()*self.__parrilla_poderes[3])
        Superheroes.numero_superheroes += 1

        #identificar al siguiente superheroes en su posicion en la lista
    
    def get_identificador(self):
        return self.__identificador
    
    def get_alias(self):
        return self.__alias
    
    def get_movimientos(self):
        return self.__movmientos
    
    def get_tipo(self):
        return self.__tipo
    
    def get_parrilla_poderes(self):
        return self.__parrilla_poderes
    
    def get_coste(self):
        return self.__coste

    def set_movimientos(self, x):
        for movimiento in x:
            if movimiento.get_tipo().value:
                movimiento.set_daño((movimiento.get_daño()/10)*(0.8*self.__parrilla_poderes[1] + 0.25*self.__parrilla_poderes[2] + 0.75*self.__parrilla_poderes[5] + self.__parrilla_poderes[4]))
            else:
                movimiento.set_daño((movimiento.get_daño()/10)*(self.__parrilla_poderes[0] + 0.75*self.__parrilla_poderes[2] + 0.25*self.__parrilla_poderes[5] + 0.2*self.__parrilla_poderes[1]))
            self.__movimientos.append(movimiento)
    
    def fight_defense(self, daño):
        self._energia = self._energia - daño
        if self._energia <= 0:
            self.die()
            self._energia = 0
    
    def fight_attack(self, obj, ronda):
        obj.fight_defense(self.__movimientos[ronda].get_daño())
    
    def __str__(self):
        return str(self.get_identificador()) + "| Alias: " + self.get_alias() + "| Tipo:" + self.get_tipo().name + "| Coste:" + str(self.get_coste()) + "| Energia:" + str(self.get_energia()) + "\n"
 