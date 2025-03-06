

class Scoreboard:
    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2
        self._player1Score = 0
        self._player2Score = 0
        self.isInitialized = False  # Para saber si ya fue asignado.

    # Getter para player1
    @property
    def player1(self):
        return self._player1

    # Setter para player1
    @player1.setter
    def player1(self, val):
        if self.isInitialized:
            raise AttributeError("Este atributo no cambia una vez asignado")
        self._player1 = val
        self.isInitialized = True  # Cambiar el estado a inicializado

    # Getter para player2
    @property
    def player2(self):
        return self._player2

    # Setter para player2
    @player2.setter
    def player2(self, val):
        if self.isInitialized:
            raise AttributeError("Este atributo no cambia una vez asignado")
        self._player2 = val
        self.isInitialized = True  # Cambiar el estado a inicializado

    # Getter para player1Score
    @property
    def player1Score(self):
        return self._player1Score

    # Setter para player1Score
    @player1Score.setter
    def player1Score(self, val):
        if self.isInitialized:
            raise AttributeError("Este atributo no cambia una vez asignado")
        self._player1Score = val
        self.isInitialized = True  # Cambiar el estado a inicializado

    # Getter para player2Score
    @property
    def player2Score(self):
        return self._player2Score

    # Setter para player2Score
    @player2Score.setter
    def player2Score(self, val):
        if self.isInitialized:
            raise AttributeError("Este atributo no cambia una vez asignado")
        self._player2Score = val
        self.isInitialized = True  # Cambiar el estado a inicializado

    # Método especial __iadd__ para manejar operaciones +=
    def __iadd__(self, other):
        if isinstance(other, (int, float)):  # Aceptamos solo enteros y flotantes
            if other == 1 or other == 0.5:
                self._player1Score += other
                return self
            else:
                raise ValueError("Solo se puede incrementar en 1 o 0.5.")
        else:
            raise ValueError("El valor a sumar debe ser un número (1 o 0.5).")

    # Método de actualización de marcador
    def updateScoreboard(self, c1, c2):
        if c1 == c2:
            self._player1Score += 0.5
            self._player2Score += 0.5
            return "Empate"

        if c1 == "P":
            if c2 == "T":
                self._player2Score += 1
                return self._player2
            self._player1Score += 1
            return self._player1
        if c2 == "P":
            if c1 == "T":
                self._player1Score += 1
                return self._player1
            self._player2Score += 1
            return self._player2
