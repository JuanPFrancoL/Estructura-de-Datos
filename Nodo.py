class Nodo:
    def __init__(self, prisionero):
        self._prisionero = prisionero
        self._siguiente = None
        self._anterior = None

    @property
    def nombre(self):
        return self._prisionero.nombre

    @property
    def edad(self):
        return self._prisionero.edad