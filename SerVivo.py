class SerVivo():
    def __init__(self, est):
        self.__energia = est
    
    def is_vivo(self):
        return self.__energia > 0

    def die(self):
        self.__energia = 0
    
    def get_energia(self):
        return self.__energia
    
    def set_energia(self, x):
        self.__energia = x