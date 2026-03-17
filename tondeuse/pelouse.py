"""Module représentant la pelouse et son état."""

from tondeuse.config import (
    LARGEUR_PELOUSE,
    HAUTEUR_PELOUSE,
    SYMBOLE_TONDEUSE,
    SYMBOLE_TONTE,
    SYMBOLE_NON_TONTE,
    SYMBOLE_OBSTACLE,
    SYMBOLE_BASE,
)


class Pelouse:
    """Grille représentant la pelouse avec ses zones tondes et obstacles."""

    # États internes des cellules
    NON_TONTE = 0
    TONTE = 1
    OBSTACLE = 2
    BASE = 3

    def __init__(self, largeur=LARGEUR_PELOUSE, hauteur=HAUTEUR_PELOUSE):
        """Crée une pelouse vide de taille largeur × hauteur."""
        self.largeur = largeur
        self.hauteur = hauteur
        self._grille = [
            [self.NON_TONTE for _ in range(largeur)] for _ in range(hauteur)
        ]

    # ------------------------------------------------------------------
    # Modification de la grille
    # ------------------------------------------------------------------

    def tondre(self, x, y):
        """Marque la cellule (x, y) comme tondue."""
        if self._dans_grille(x, y):
            self._grille[y][x] = self.TONTE

    def ajouter_obstacle(self, x, y):
        """Ajoute un obstacle en (x, y)."""
        if self._dans_grille(x, y):
            self._grille[y][x] = self.OBSTACLE

    def definir_base(self, x, y):
        """Définit la position de la base de rechargement."""
        if self._dans_grille(x, y):
            self._grille[y][x] = self.BASE

    # ------------------------------------------------------------------
    # Interrogation de la grille
    # ------------------------------------------------------------------

    def peut_avancer(self, x, y):
        """Retourne True si la cellule est accessible (dans la grille et sans obstacle)."""
        if not self._dans_grille(x, y):
            return False
        return self._grille[y][x] != self.OBSTACLE

    def est_tonte(self, x, y):
        """Retourne True si la cellule (x, y) est déjà tondue."""
        return self._dans_grille(x, y) and self._grille[y][x] in (
            self.TONTE,
            self.BASE,
        )

    def _dans_grille(self, x, y):
        """Vérifie que (x, y) est dans les limites de la grille."""
        return 0 <= x < self.largeur and 0 <= y < self.hauteur

    # ------------------------------------------------------------------
    # Statistiques
    # ------------------------------------------------------------------

    @property
    def pourcentage_tonte(self):
        """Pourcentage de la surface tondue (obstacles exclus)."""
        total = 0
        tondu = 0
        for ligne in self._grille:
            for cellule in ligne:
                if cellule != self.OBSTACLE:
                    total += 1
                    if cellule in (self.TONTE, self.BASE):
                        tondu += 1
        return (tondu / total * 100) if total > 0 else 0.0

    # ------------------------------------------------------------------
    # Affichage
    # ------------------------------------------------------------------

    def afficher(self, robot=None):
        """Affiche la pelouse dans le terminal."""
        symboles = {
            self.NON_TONTE: SYMBOLE_NON_TONTE,
            self.TONTE: SYMBOLE_TONTE,
            self.OBSTACLE: SYMBOLE_OBSTACLE,
            self.BASE: SYMBOLE_BASE,
        }
        lignes = []
        for y, ligne in enumerate(self._grille):
            ligne_str = ""
            for x, cellule in enumerate(ligne):
                if robot is not None and robot.x == x and robot.y == y:
                    ligne_str += SYMBOLE_TONDEUSE
                else:
                    ligne_str += symboles.get(cellule, "?")
            lignes.append(ligne_str)
        print("\n".join(lignes))
        print(f"Tonte : {self.pourcentage_tonte:.1f}%\n")
