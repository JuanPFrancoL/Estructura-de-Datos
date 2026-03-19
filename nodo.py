class Nodo:
    def __init__(self, prisionero):
        self._prisionero = prisionero
        self._siguiente = None

    @property
    def prisionero(self):
        return self._prisionero

    @prisionero.setter
    def prisionero(self, prisionero):
        self._prisionero = prisionero

    @property
    def nombre(self):
        return self._prisionero.nombre

    @property
    def edad(self):
        return self._prisionero.edad

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, siguiente):
        self._siguiente = siguiente