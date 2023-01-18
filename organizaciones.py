class Organizacion:
    def __init__(self, x, y):   #x es el nombre e y es la lista de superheroes
        if type(x) != str:
            raise TypeError('El nombre debe ser un string')  #con el raise se levanta la excepción
        if type(y) != list:
            raise TypeError('y debe ser una lista')
        if not y:
            raise ValueError('La lista no puede estar vacía, debe haber al menos un superhéroe')
        self.nombre = x
        self.superheroes = y

    def get_nombre(self):
        return self.nombre

    def get_superheroes(self):
        return self.superheroes

    def set_superheroes(self, x):
        self.superheroes = x
    
    def is_undefeated(self):
        x = False
        for i in range(len(self.superheroes)):
            if self.superheroes[i].is_vivo():
                x = True
                break
        return x

    def surrender(self):
        for superheroe in self.superheroes:
            superheroe.die()
    
    