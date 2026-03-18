from nodo import Nodo

class ListaSimple:
    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    @property
    def cabeza(self):
        return self._cabeza

    @cabeza.setter
    def cabeza(self, cabeza):
        self._cabeza = cabeza

    @property
    def tamanio(self):
        return self._tamanio

