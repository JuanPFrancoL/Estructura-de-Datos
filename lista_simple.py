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

    def eliminar(self, nodo):
        if self._cabeza is nodo:
            self._cabeza = nodo.siguiente
            nodo.siguiente = None
            self._tamanio -= 1
            return

        puntero = self._cabeza
        while puntero is not None:
            if puntero.siguiente is nodo:
                puntero.siguiente = nodo.siguiente
                nodo.siguiente = None
                self._tamanio -= 1
                return
            puntero = puntero.siguiente

    def is_empty(self):
        return self._cabeza is None

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


    # Segundo decreto - busq binaria y clemencia
    def busqueda_binaria(self, edad_objetivo):
        inicio = 0
        fin = self.tamanio - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2

            nodo_medio = self.cabeza
            for _ in range(medio):
                nodo_medio = nodo_medio.siguiente

            if nodo_medio.edad == edad_objetivo:
                return nodo_medio
            elif nodo_medio.edad < edad_objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None

    def clemencia(self, edad_gracia):
        nodo = self.busqueda_binaria(edad_gracia)
        if nodo is None:
            return None
        self.eliminar(nodo)
        return nodo

    # Tercer / Cuarto decreto - Juego circulo
    def juego_circulo(self, k1, k2, ejecutados):
        total_inicial = self.tamanio
        mitad = total_inicial // 2
        eliminados_f1 = 0 # fase 1
        actual = self._cabeza

        # Fase 1: k1
        while eliminados_f1 < mitad:
            for _ in range(k1 - 1):
                actual = actual.siguiente
                if actual is None:
                    actual = self._cabeza

            ejecutados.agregar_prisionero(actual.prisionero)
            siguiente_vivo = actual.siguiente
            if siguiente_vivo is None:
                siguiente_vivo = self._cabeza
            self.eliminar(actual)
            eliminados_f1 += 1
            actual = siguiente_vivo
            if actual is None:
                actual = self._cabeza

        # Fase 2: k2
        while self._tamanio > 1:
            for _ in range(k2 - 1):
                actual = actual.siguiente
                if actual is None:
                    actual = self._cabeza

            ejecutados.agregar_prisionero(actual.prisionero)
            siguiente_vivo = actual.siguiente

            if siguiente_vivo is None:
                siguiente_vivo = self._cabeza
            self.eliminar(actual)
            actual = siguiente_vivo
            if actual is None:
                actual = self._cabeza

        return self._cabeza