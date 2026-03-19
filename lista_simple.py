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

    # Metodos
    def agregar_prisionero(self, prisionero):
        nuevo_nodo = Nodo(prisionero)

        if self._cabeza is None:
            self._cabeza = nuevo_nodo
        else:
            puntero = self._cabeza
            while puntero.siguiente is not None:
                puntero = puntero.siguiente
            puntero.siguiente = nuevo_nodo
        self._tamanio += 1

    def eliminar(self, nodo_anterior, nodo):
        if nodo_anterior is None:
            self._cabeza = nodo.siguiente
        else:
            nodo_anterior.siguiente = nodo.siguiente

        nodo.siguiente = None
        self._tamanio -= 1