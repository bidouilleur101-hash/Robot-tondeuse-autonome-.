"""Module définissant le robot tondeuse autonome."""

from enum import Enum
from tondeuse.config import AUTONOMIE_BATTERIE


class Direction(Enum):
    """Les quatre directions cardinales."""
    NORD = "N"
    EST = "E"
    SUD = "S"
    OUEST = "O"


# Mouvements associés à chaque direction (delta_x, delta_y)
DELTA = {
    Direction.NORD: (0, -1),
    Direction.EST: (1, 0),
    Direction.SUD: (0, 1),
    Direction.OUEST: (-1, 0),
}

# Ordre de rotation horaire
ROTATION_DROITE = [Direction.NORD, Direction.EST, Direction.SUD, Direction.OUEST]


class Robot:
    """Robot tondeuse autonome qui tond une pelouse en évitant les obstacles."""

    def __init__(self, pelouse, x_depart=0, y_depart=0):
        """Initialise le robot à la position de départ."""
        self.pelouse = pelouse
        self.x = x_depart
        self.y = y_depart
        self.x_base = x_depart
        self.y_base = y_depart
        self.direction = Direction.EST
        self.batterie = AUTONOMIE_BATTERIE
        self.en_marche = True

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    def tourner_droite(self):
        """Tourne de 90° vers la droite."""
        idx = ROTATION_DROITE.index(self.direction)
        self.direction = ROTATION_DROITE[(idx + 1) % 4]

    def tourner_gauche(self):
        """Tourne de 90° vers la gauche."""
        idx = ROTATION_DROITE.index(self.direction)
        self.direction = ROTATION_DROITE[(idx - 1) % 4]

    def avancer(self):
        """Avance d'une case dans la direction courante.

        Retourne True si le mouvement a réussi, False sinon.
        """
        dx, dy = DELTA[self.direction]
        nx, ny = self.x + dx, self.y + dy
        if self.pelouse.peut_avancer(nx, ny):
            self.x, self.y = nx, ny
            self.pelouse.tondre(self.x, self.y)
            self.batterie -= 1
            if self.batterie <= 0:
                self.en_marche = False
            return True
        return False

    # ------------------------------------------------------------------
    # Stratégie de tonte (balayage en zigzag)
    # ------------------------------------------------------------------

    def tondre_pelouse(self):
        """Tond toute la pelouse accessible avec une stratégie en zigzag."""
        # Marque la position de départ comme tondue
        self.pelouse.tondre(self.x, self.y)

        while self.en_marche:
            if not self._avancer_ou_tourner():
                break

    def _avancer_ou_tourner(self):
        """Essaie d'avancer; tourne si bloqué. Retourne False si coincé."""
        for _ in range(4):
            if self.avancer():
                return True
            self.tourner_droite()
        # Le robot est coincé dans toutes les directions
        return False

    # ------------------------------------------------------------------
    # Informations
    # ------------------------------------------------------------------

    @property
    def position(self):
        """Retourne la position courante sous forme de tuple (x, y)."""
        return (self.x, self.y)

    def __str__(self):
        return (
            f"Robot à ({self.x}, {self.y}) "
            f"direction={self.direction.value} "
            f"batterie={self.batterie}"
        )
