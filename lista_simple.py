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

    def is_empty(self):
        return self._cabeza is None

    def insertar(self, indice, prisionero):
        nuevo_nodo = Nodo(prisionero)
        if indice == 0:
            nuevo_nodo.siguiente = self._cabeza
            self._cabeza = nuevo_nodo
            self._tamanio += 1
            return
        contador = 0
        puntero = self._cabeza
        while contador < (indice - 1) and puntero is not None:
            puntero = puntero.siguiente
            contador += 1
        aux = puntero.siguiente
        puntero.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = aux
        self._tamanio += 1

    def imprimir(self):
        puntero = self._cabeza

        while puntero is not None:
            print(puntero)
            puntero = puntero.siguiente


    # Primer detreto
    def ordenar(self):
        if self.is_empty():
            return
        intercambiado = True
        while intercambiado:
            intercambiado = False
            puntero = self._cabeza

            while puntero.siguiente is not None:
                if puntero.edad > puntero.siguiente.edad:
                    aux = puntero.prisionero
                    puntero.prisionero = puntero.siguiente.prisionero
                    puntero.siguiente.prisionero = aux
                    intercambiado = True

                puntero = puntero.siguiente


    # Acceder x indice
    def _nodo_en_indice(self, indice):
        anterior = None
        actual = self._cabeza
        for _ in range(indice):
            anterior = actual
            actual = actual.siguiente
        return anterior, actual

    # Segundo decreto - busq binaria y clemencia
