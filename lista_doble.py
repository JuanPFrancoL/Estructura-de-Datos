from nodo import Nodo

class ListaDoble:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._size = 0

    @property
    def cabeza(self):
        return self._cabeza

    @property
    def cola(self):
        return self._cola

    @property
    def size(self):
        return self._size

    @cabeza.setter
    def cabeza(self, cabeza):
        self._cabeza = cabeza

    @cola.setter
    def cabeza(self, cola):
        self._cola = cola

    @size.setter
    def size(self, size):
        self._size = size

    def agregar_prisionero(self, prisionero):
        nuevo_nodo = Nodo(prisionero)
        if self._cabeza is None:
            self._cabeza = nuevo_nodo
            self._cola = nuevo_nodo
        else:
            self._cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self._cola
            self._cola = nuevo_nodo
        self._tamaño += 1

    # Primer decreto
    def ordenar(self):
        if self.is_empty():
            return
        intercambiado = True
        while intercambiado:
            intercambiado = False
            puntero = self._cabeza
            while puntero.siguiente is not None:
                if puntero.edad > puntero.siguiente.edad:
                    puntero.prisionero, puntero.siguiente.prisionero = (
                        puntero.siguiente.prisionero, puntero.prisionero
                    )
                    intercambiado = True
                puntero = puntero.siguiente

    # Segundo decreto
    def clemencia(self, edad_gracia):
        inicio = 0
        fin = self.size - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            nodo_medio = self._nodo_en_indice(medio)

            if nodo_medio.edad == edad_gracia:
                return nodo_medio
            elif nodo_medio.edad < edad_gracia:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None

    def _nodo_en_indice(self, indice):
        """
        Accede al nodo en 'indice' eligiendo la dirección más corta
        gracias al puntero anterior.
        """
        if indice <= self.size // 2:
            actual = self.cabeza
            for _ in range(indice):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self.size - 1 - indice):
                actual = actual.anterior
        return actual

    def clean(self):
        self._cabeza = None
        self._tamaño = 0         
    def eliminar(self, nodo):
        if nodo.anterior is not None:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.cabeza = nodo.siguiente  # era la cabeza

        if nodo.siguiente is not None:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.cola = nodo.anterior  # era la cola

        nodo.siguiente = None
        nodo.anterior = None
        self.tamanio -= 1

    def insertar(self, index, valor):
        nuevo_nodo = Nodo(valor)
        if index == 0:
            nuevo_nodo.siguiente = self._cabeza
            self._cabeza = nuevo_nodo
            self._tamaño += 1    
            return
        contador = 0
        puntero = self._cabeza
        while contador < (index - 1):
            puntero = puntero.siguiente
            contador += 1
        aux = puntero.siguiente
        puntero.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = aux
        self._tamaño += 1         
    def is_empty(self):          
        return self._cabeza is None


    def imprimir(self):
        puntero = self._cabeza
        while puntero is not None:
            print(puntero.valor)
            puntero = puntero.siguiente