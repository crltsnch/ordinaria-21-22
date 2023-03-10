class Organizacion:
    def __init__(self, x, y):   #x es el nombre e y es la lista de superheroes
        if type(x) != str:
            raise TypeError('El nombre debe ser un string')  #con el raise se levanta la excepción
        if type(y) != list:
            raise TypeError('y debe ser una lista')
        if not y:
            raise ValueError('La lista no puede estar vacía, debe haber al menos un superhéroe')
        self.__nombre = x
        self.__superheroes = y

    def get_nombre(self):
        return self.__nombre

    def get_superheroes(self):
        return self.__superheroes

    def set_superheroes(self, x):
        self.__superheroes = x
    
    def is_undefeated(self):
        x = False
        for i in range(len(self.__superheroes)):
            if self.__superheroes[i].is_vivo():
                x = True
                break
        return x

    def surrender(self):
        for superheroe in self.__superheroes:
            superheroe.die()
    
    def __str__(self):
        tp = ""
        for superheroe in self.__superheroes:
            tp += str(superheroe.get_identificador) + '. Alias: ' + superheroe.get_alias() + ', Tipo: ' + superheroe.get_tipo().name + ', Coste: ' + str(superheroe.get_coste()) + ", Energia:" + str(superheroe.get_energia()) + "\n"
        return tp
    
    def __repr__(self):
        tr = ""
        for superheroe in self.__superheroes:
            tr += superheroe.get_identificador + '\t' + superheroe.get_tipo().name + '\t' + superheroe.get_movimientos() + '\n'
    
    def get_super_undefeated(self):
        super_vivos = []
        for i in range (0, len(self.__superheroes)):
            if self.__superheroes[i].is_vivo():
                super_vivos.append(self.__superheroes[i])
        return super_vivos
    