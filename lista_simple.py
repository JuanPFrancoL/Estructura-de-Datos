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

    # Metodo para agregar prisionero al final
    def agregar_prisionero(self, prisionero):
        nuevo_nodo = Nodo(prisionero)
        # Si la lista esta vacia el nuevo nodo es la cabeza
        if self._cabeza is None:
            self._cabeza = nuevo_nodo
        else:
            # Recorrer hasta el ultimo nodo
            puntero = self._cabeza
            while puntero.siguiente is not None:
                puntero = puntero.siguiente
            puntero.siguiente = nuevo_nodo
        # Aumentar el tamaño de la lista
        self._tamanio += 1

    # Metodo para eliminar un nodo de la lista
    def eliminar(self, nodo):
        # Si el nodo es la cabeza
        if self._cabeza is nodo:
            self._cabeza = nodo.siguiente
            nodo.siguiente = None
            self._tamanio -= 1
            return

        # Buscar el nodo anterior
        puntero = self._cabeza
        while puntero is not None:
            if puntero.siguiente is nodo:
                puntero.siguiente = nodo.siguiente
                nodo.siguiente = None
                self._tamanio -= 1
                return
            puntero = puntero.siguiente

    # Verificar si la lista esta vacia
    def is_empty(self):
        return self._cabeza is None

    # Imprimir los prisioneros de la lista
    def imprimir(self):
        puntero = self._cabeza

        while puntero is not None:
            print(puntero.nombre, puntero.edad)
            puntero = puntero.siguiente


    # Primer decreto
    def ordenar(self):
        if self.is_empty():
            return

        intercambiado = True
        while intercambiado:
            intercambiado = False
            puntero = self._cabeza
            while puntero.siguiente is not None:
                # Comparar las edades para ordenar
                if puntero.edad > puntero.siguiente.edad:
                    # Ordenar con bubble sort
                    aux = puntero.prisionero
                    puntero.prisionero = puntero.siguiente.prisionero
                    puntero.siguiente.prisionero = aux
                    intercambiado = True

                puntero = puntero.siguiente


    # Segundo decreto
    # Busqueda binaria
    def busqueda_binaria(self, edad_objetivo):
        inicio = 0
        fin = self.tamanio - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            # Recorrer hasta el nodo medio
            nodo_medio = self.cabeza
            for _ in range(medio):
                nodo_medio = nodo_medio.siguiente
            # Comparar edades
            if nodo_medio.edad == edad_objetivo:
                return nodo_medio
            elif nodo_medio.edad < edad_objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None
    # Clemencia del decreto 2
    def clemencia(self, edad_gracia):
        nodo = self.busqueda_binaria(edad_gracia)
        if nodo is None:
            return None
        self.eliminar(nodo)
        return nodo

    # Tercer / Cuarto decreto
    # Juego del circulo con las dos fases para k1 y para k2
    def juego_circulo(self, k1, k2, ejecutados):
        total_inicial = self.tamanio
        mitad = total_inicial // 2
        eliminados_f1 = 0 # fase 1
        # Comenzar desde la cabeza
        actual = self._cabeza

        # Fase 1 con k1
        while eliminados_f1 < mitad:
            # Avanzar k1 menos uno pasos
            for _ in range(k1 - 1):
                actual = actual.siguiente
                if actual is None:
                    actual = self._cabeza

            # Guardar el prisionero ejecutado
            ejecutados.agregar_prisionero(actual.prisionero)

            # Guardar el siguiente prisionero vivo
            siguiente_vivo = actual.siguiente
            if siguiente_vivo is None:
                siguiente_vivo = self._cabeza

            # Eliminar el nodo actual
            self.eliminar(actual)
            eliminados_f1 += 1

            # Continuar desde el nodo siguiente
            actual = siguiente_vivo
            if actual is None:
                actual = self._cabeza

        # Fase 2 con k2
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

        # Retornar el ultimo sobreviviente
        return self._cabeza